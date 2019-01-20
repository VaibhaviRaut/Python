#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to accept 3 no.s from user and print the min out of them.
'''

a,b,c = eval(input("Enter three numbers: "))

if(a<b and a<c):
    print("Minimum: ",a)
elif(b<c):
    print("Minimum: ",b)
else:
    print("Minimum: ",c)
