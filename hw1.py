#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37
''' 6/1/19
W.A.P. to take two numbers input and perform the following oprations:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponential
'''

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
print("Number 1: ",a,"Number 2:",b)
'''sum = int(a)+int(b)'''
sum = a + b
sub = a - b
mul = a * b
div = a / b
exp = pow(a,b)
print("The operations: ")
print("Addition: ",sum)
print("Subtraction: ",sub)
print("Multiplication: ",mul)
print("Division: ",div)
print("Exponential: ",exp)
print("\n")
