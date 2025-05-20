def sum_function(expr1, expr2):
    """
    Sum_Function using two arguments

    Parameters:
       expr1 , expr2 (int , float): the two operands , only numbers are accepted

    Returns:
        the sum of the numbers 
    """    
    sum = expr1 + expr2
    return sum

def subtract_function(expr1, expr2):
    """
    Subtract_Function using two arguments

    Parameters:
       expr1 , expr2 (int , float): the two operands , only numbers are accepted

    Returns:
        the difference of the numbers
    """    
    sub = expr1 - expr2
    return sub

def multiply_function(expr1, expr2):
    """
    Multiply_Function using two arguments

    Parameters:
       expr1 , expr2 (int , float): the two operands , only numbers are accepted

    Returns:
        the product of the numbers
    """    
    mult = expr1 * expr2
    return mult

def divide_function(expr1, expr2):
    """
    Divide_Function using two arguments

    Parameters:
       expr1 , expr2 (int , float): the two operands , only numbers are accepted
                                    also , expr2 should not be 0          

    Returns:
        the quotient of the numbers
        if expr2 is 0 , it will return an error message
    """    
    if expr2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        div = expr1 / expr2
        return div

def modulus_function(expr1, expr2):
    """
    Modulus_Function using two arguments

    Parameters:
       expr1 , expr2 (int , float): the two operands , only numbers are accepted
                                    also , expr2 should not be 0          

    Returns:
        the modulus of the numbers
        if expr2 is 0 , it will return an error message
    """    
    if expr2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        mod = expr1 % expr2
        return mod

def power_function(expr1, expr2):
    """
    Power_Function using two arguments

    Parameters:
       expr1 , expr2 (int , float): expr1 is the base and expr2 is the exponent
                                    only numbers are accepted          

    Returns:
        the exrp1 to the power of expr2
    """    
    pow = expr1 ** expr2
    return pow

def calculate(expr1, operator, expr2):
    """
    Calculate_function performs an arithmetic operation on two numbers.

    Parameters:
        expr1 , expr2 (int , float): the two operands, only numbers are accepted.
        operator (str): Operator symbol ('+', '-', '*', '/', '%', '**', '^').

    Returns:
         the result of the operation, or an error message for invalid operations 
    """
    if operator == "+":
        result = sum_function(expr1, expr2)
    elif operator == "-":
        result = subtract_function(expr1, expr2)
    elif operator == "*":
        result = multiply_function(expr1, expr2)
    elif operator == "/":
        result = divide_function(expr1, expr2)
    elif operator == "%":
        result = modulus_function(expr1, expr2)
    elif operator == "**" or operator == "^":
        result = power_function(expr1, expr2)
    return result

#user input
expression = input("Enter the expression: ")
if not expression:
    print("Error: Empty expression.")
    exit()

expression = expression.replace(" ", "")
#based on expected input , sort the input into two lists
expected_input = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "%", ".", "^", "**"]

input_list = []
trash_list = []

for i in expression:
    if i in expected_input:
        input_list.append(i)
    else:
        trash_list.append(i)

print("input_list = ", input_list)
print("trash_list = ", trash_list)

#separate numbers and operators
numbers_list_temp = []
operators_list = []

temp_number = ""
i = 0
expecting_number = True  

while i < len(expression):
    ch = expression[i]

    if ch.isdigit() or ch == ".":
        temp_number += ch
        i += 1
        expecting_number = False  
    else:
        if temp_number:
            numbers_list_temp.append(temp_number)
            temp_number = ""

       
        if ch == "*" and i + 1 < len(expression) and expression[i + 1] == "*":
            if expecting_number:
                trash_list.append("**")
            else:
                operators_list.append("**")
            i += 2
            expecting_number = True
        elif ch in ["+", "-", "*", "/", "%", "^"]:
            if expecting_number:
                trash_list.append(ch) 
            else:
                operators_list.append(ch)
            i += 1
            expecting_number = True
        else:
            trash_list.append(ch)
            i += 1


if temp_number:
    numbers_list_temp.append(temp_number)
elif expecting_number:
    
    if operators_list:
        trash_list.append(operators_list.pop())

numbers_list = []
for x in numbers_list_temp:
    if x != "":
        numbers_list.append(x)


print("numbers_list", numbers_list)
print("operators_list", operators_list)

#calculate the result iterating through the operators list
while len(operators_list) > 0:
    for x in operators_list:
        if x == "**" or x == "^":
            index = operators_list.index(x)
            expr1 = float(numbers_list[index])
            expr2 = float(numbers_list[index + 1])
            result = calculate(expr1, x, expr2)
            numbers_list[index] = result
            numbers_list.pop(index + 1)
            operators_list.pop(index)

    for x in operators_list:
        if x == "*" or x == "/" or x == "%":
            index = operators_list.index(x)
            expr1 = float(numbers_list[index])
            expr2 = float(numbers_list[index + 1])
            result = calculate(expr1, x, expr2)
            if isinstance(result, str):  
                print(result)
                exit()
            numbers_list[index] = result
            numbers_list.pop(index + 1)
            operators_list.pop(index)

    for x in operators_list:
        if x == "+" or x == "-":
            index = operators_list.index(x)
            expr1 = float(numbers_list[index])
            expr2 = float(numbers_list[index + 1])
            result = calculate(expr1, x, expr2)
            numbers_list[index] = result
            numbers_list.pop(index + 1)
            operators_list.pop(index)

#print the final result
print("result = ", numbers_list[0])
