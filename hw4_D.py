#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to accept two  strings from user and check whether the 2nd string is
rotation of the 1st one. Without using loop.
'''

s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")

c1 = len(s1)
c2 = len(s2)

if c1==c2:
    if s1[:1]==s2[c2-1:]:
        print("String 1: "+s1+"\nString 2: "+s2+"\nAre in Rotation!")
    else:
        print("String 1: "+s1+"\nString 2: "+s2+"\nAre NOT in Rotation!")
else:
    print("The words are different!")

   
'''
rotate in input(str1)+input(str2)
'''
