#!C:User\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to accept a number from user and check whether it is a palindrome or not.
'''

def palindrome(s):
    t=s
    rev=0
    while t>0:
        d=t%10
        rev = rev*10+d
        t=t//10
    if s==rev:
        print(s," is a Palindrome!")
    else:
        print(s," is not a Palindrome!")

def main():
    s = eval(input("Enter a string: "))
    palindrome(s)

if __name__=="__main__":
    main()

'''
OUTPUT:
=== RESTART: C:/Users/Vaibhavi Raut/Desktop/PythonPrg/H.W/palindrome_no.py ===
Enter a string: 121
121  is a Palindrome!
>>> 
=== RESTART: C:/Users/Vaibhavi Raut/Desktop/PythonPrg/H.W/palindrome_no.py ===
Enter a string: 654
654  is not a Palindrome!
>>> 
=== RESTART: C:/Users/Vaibhavi Raut/Desktop/PythonPrg/H.W/palindrome_no.py ===
Enter a string: 122454221
122454221  is a Palindrome!
>>> 
'''
