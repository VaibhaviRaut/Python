#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to accept a string from user and convert it to lowercase and uppercase.
'''

word = input("Enter a word: ")

print(type(word))

if word.islower():
    print("UpperCase is ",word.upper())
elif word.isupper():
    print("LowerCase is ",word.lower())
else:
    print("Mix of both. Can't convert!")
    print("In that case: ",word.swapcase())

'''
Comments!
'''
