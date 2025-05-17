# define the Fibonaci_recursive
def Fibonaci_recursive(n) :
    """
    Fibonaci Function using recursion

    Parameters:
        n (int): represents the nth element of the Fibonaci sequence

    Returns:
        the the value of the nth element of the Fibonaci sequence

    """
        
    if n<0 :
        print(f"Wrong input , {n} < 0")
        return None

    elif n <= 1 :
        return n
    
    else :
        return ( Fibonaci_recursive(n-1) + Fibonaci_recursive(n-2) )



# define the Fibonaci_iterative
def Fibonaci_iterative(n) :

    """
    Fibonaci Function using iteration

    Parameters:
        n (int): represents the nth element of the Fibonaci sequence

    Returns:
        the the value of the nth element of the Fibonaci sequence

    """
    
    if n<0 :
        print(f"Wrong input , {n} < 0")
        return None
    
    elif n <= 1 :
            return n

    else :
        a, b = 0 , 1
        for x in range(2,n+1) :
            a, b = b, a + b
        return b
      

# main program 
print("Hello , wich element of the Fibonaci sequence do you want to see ?")
n = -1
while n < 0 :
    n = int(input())
    if n < 0 :
        print(f"Wrong input , {n} < 0")
    else : 
        print(f"The {n}th element of the Fibonaci sequence calculated with Fibonaci_iterative is : {Fibonaci_iterative(n)}")
        print(f"The {n}th element of the Fibonaci sequence calculated with Fibonaci_recursive is : {Fibonaci_recursive(n)}")
        break