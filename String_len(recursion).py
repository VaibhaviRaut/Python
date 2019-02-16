#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to find the length of a string using recursive function.
'''

def length_recur(s):
    if s=='':
        return 0
    return 1+length_recur(s[1:])

'''
    for i in s:
        if s!='':
            cnt+=1
        else:
            break
'''

def main():
    s = input("Enter a string: ")
    l = length_recur(s)
    print("Length of the string is ",l)


if __name__=='__main__':
    main()


'''
OUTPUT:
Enter a string: PYTHON
Length of the string is  6
'''
