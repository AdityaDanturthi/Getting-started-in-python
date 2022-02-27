print("Calculator.py")
num1= int(input("Please input the first number: "))
num2= int(input("Please input the second number: "))
operator=input("Please select an operation: +, -, /, *: ")



def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2


def mul(num1, num2):
    return  num1*num2

def div(num1, num2):
    return num1/num2
    

if (operator == '+'):
    result= add(num1, num2)
elif (operator == '-'):
    result= sub(num1, num2)
elif (operator== '*'):
    result= mul(num1, num2)
elif (operator == '/' and num2 == 0):
    print("Error: Cannot perform division since the denominator is 0. Please try again")
    
    result= div(num1, num2)
else: print ("Invalid operator. Please try again.")

print(f"{num1} {operator} {num2} = {result}")

