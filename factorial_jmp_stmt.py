#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to find the factorial of a number.
'''
n = eval(input("Enter a number: "))

fact = 1
while n>0:
    fact = fact * n
    n-=1
print(fact)
'''
fact = n*(n-1)
'''


