#!C:Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to print the following pattern:
patternQ.docx
'''

'''
def pattern1(n):
    print("PATTERN 1")
    for i in range(1,n+1):
        for _ in range(1,i+1):
            print(" ",end='')
        for _

        in range(1,n-i+2):
            print("*",end='')
        print()

def pattern2(n):
    print("PATTERN 2")
    for i in range(1,n+1):
        for _ in range(1,n-i+2):
            print("*",end='')
        for _ in range(1,i+1):
            print(" ",end='')
        print()

def pattern3(n):
    print("PATTERN 3")
    for i in range(1,n+1):
        x = i
        for _ in range(1,n-i+1):
            print(" ",end='')
        for j in range(1,i*2):
            print(chr(x+64),end='')
            if j<i:
                x -=1
            else:
                x+=1     
        print()'''
        
    #y = ord('B')#chr(65)
    #print(y)
def pattern4(n):
    print("PATTERN 4")
    for i in range(1,n+1):
        for _ in range(1,n-i+1):
            print("*",end='')
        for _ in range(1,i*2):
            print(" ",end='')
        print()
        for k in range(1,n+i):
            for _ in range(1,k+1):
                print(" ",end='')
            for _ in range(1,n-k+2):
                print("*",end='')
            print()

'''
def pattern5(n):
    print("\nPATTERN 5")
    if n > 0:              
        for i in range(n):
            for s in range (n - i) :    
                print(" ", end="")
            for j in range((i * 2) - 1):
                print("*", end="")
            print()
        for i in range(n, 0, -1):
            for s in range (n - i) :
                print(" ", end="")
            for j in range((i * 2) - 1):
                print("*", end="")
            print()
'''
            

def main():
    n = eval(input("Enter the number: "))
    '''
    pattern1(n)
    pattern2(n)
    pattern3(n)
    pattern5(n)
    '''    
    pattern4(n)


if __name__=='__main__':
    main()
