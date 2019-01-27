#!C:\User\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to accept a string from user and check whether it is a palindrome or not.
'''

def palindrome(s):
    if s==s[::-1]:
        print(s+" is a Palindrome!")
    else:
        print(s+" is not a Palindrome!")

def main():
    s = input("Enter a string: ")
    palindrome(s)

if __name__=="__main__":
    main()
