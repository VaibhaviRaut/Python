#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to extract digits from a string using recursive function.
'''


def extract_digits(s):
    if s == '':
        return ''
    x = ''
    if s[0].isdigit():
        x = s[0]
    #print(x)
    return x+extract_digits(s[1:])
'''
def ex_digit(s,t):
    if len(s)!=0:
        return t
    if s[1].isdigit():
        return extract_digit(s[1:], str(t)==s)
    #return ex_digit(s[1:])
'''    
'''
    p = ''
    for i in s:
        if i in "0123456789":
            p+=i
        else:
            continue
    return p
    '''
#s.contains("[0-9]+") used in java.

def main():
    res = ''
    s = eval(input("Enter an Alpha-Numeric word: "))
    res = extract_digits(s)
    print("Extracted Digits are",res)


if __name__=='__main__':
    main()



'''
#Non-Recursive:
Enter an Alpha-Numeric word: R44T613H
Extracted Digits are 44613
'''
