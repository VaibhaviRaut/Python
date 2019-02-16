#!C:Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to count the number of 0's in the given number.
Example:
i/p: 64 o/p:7
i/p: 63 o/p:3
'''

def count0(n):
    cnt = 0
    while n!=0:
        cnt+=1
        n = n&(n-1)
    return cnt


def main():
    n = eval(input("Enter a number: "))
    tot = 8                     #as in 8 bits
    a = count0(n)
    print("Number of 0's are ",(tot-a))

if __name__=='__main__':
    main()
