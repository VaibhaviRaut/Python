#!C:Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to print:
1]

1
1 2
1 2 3
1 2 3 4
1 2 3
1 2
1
'''

def pattern1(n):
    print("PATTERN 1:")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print()
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(j,end='')
        print()

def pattern2(n):
    print("PATTERN 2:")
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(n-j-i+2,end='')
        for j in range(1,i+1):
            print("*",end='')
        print()
    #Numbers are reversed
'''
for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(n-i,end='')
        for j in range(1,i+1):
            print("*",end='')
        print()
FOR THIS SNIPPET OUTPUT IS:
3333*
222**
11***
0****
'''
def main():
    n = eval(input("Enter a number: "))
    pattern1(n)
    pattern2(n)


if __name__=='__main__':
    main()


'''
OUTPUT:
Enter a number: 4
PATTERN 1:
1
12
123
1234
123
12
1

PATTERN 2:
4321*
321**
21***
1****
'''
