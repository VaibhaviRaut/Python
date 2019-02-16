#!C:Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to accept a no from the user and check whether it is divisible by 8 using
bitwise operations.
'''


import math  

def method1(n):
    print("METHOD 1:")
    if (n & 7)== 0:
        print("YES!")
    else:
        print("NO!")

def method2(n): 
    print("METHOD 2:")  
    return (((n >> 3) << 3) == n) 
  
def main():
    n = eval(input("Enter the number: "))
    method1(n)
    if (method2(n)): 
        print("YES") 
    else: 
        print("NO") 

if __name__=='__main__':
    main()

'''
OUTPUT:
Enter the number: 88
METHOD 1:
YES!
METHOD 2:
YES

Enter the number: 23
METHOD 1:
NO!
METHOD 2:
NO
'''
