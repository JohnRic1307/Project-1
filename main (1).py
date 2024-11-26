def Add(num1, num2):
    print(f"The sum  is {num1 + num2}")

def Sub(num1, num2):
    print(f"The difference  is {num1 - num2}")

def Mul(num1, num2):
    print(f"The product is {num1 * num2}")

def  Div(num1, num2):
    if num2 != 0:
        print(f"The quotient is {num1 / num2}")
    else:
        print(" Error ")

num1 = int(input("Enter 1st no.:  "))
num2 = int(input("Enter 2nd no.:  "))
operation = input(" OPERATION (A for Addition, S for Subtraction, M for Multiplication, D for Division): ").upper()

if operation == 'A':
    Add(num1, num2)
 
 
elif operation == 'M':
    Mul(num1, num2)
    
elif operation == 'S':
    Sub(num1, num2)
    
elif operation == 'D':
    Div(num1, num2)
else:
    print("Error!")