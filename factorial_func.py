#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to find factorial of a number using function.
'''

n = eval(input("Enter a number: "))

def factorial(n):
        if n==1:
                return n
        else:
                return n * factorial(n-1)
print("Factorial of ",n," is ",factorial(n))

#print statement should be out of the function.
