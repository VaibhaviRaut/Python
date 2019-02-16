#!C:Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to count the number of 1 bits in a number using recursive function and
bitwise operators.
'''

def count1(n):
    if n==0:
        return 0
    return 1+count1(n&(n-1))


'''
    cnt = 0
    while n!=0:
        cnt+=1
        n = n&(n-1)
    return cnt
'''

def main():
    n = eval(input("Enter the number: "))
    c = count1(n)
    print("Count:",c)


if __name__=='__main__':
    main()
