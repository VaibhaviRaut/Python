#!C:Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to check whether the given number is a multiple of 512 using bitwise
operations.
'''


def check(n):
    if(n&7)==0:
        return True
    else:
        return False

def main():
    n = eval(input("Enter a number: "))
    if(check(n)):
        print("Number ",n,"is a multiple of 512!")
    else:
        print("Number ",n,"is NOT a multiple of 512!")

if __name__=='__main__':
    main()


'''
OUTPUT:
Enter a number: 23
Number  23 is NOT a multiple of 512!

Enter a number: 44
Number  44 is NOT a multiple of 512!

Enter a number: 1024
Number  1024 is a multiple of 512!

Enter a number: 5120
Number  5120 is a multiple of 512!

Enter a number: 3584
Number  3584 is a multiple of 512!

Enter a number: 13
Number  13 is NOT a multiple of 512!
'''
