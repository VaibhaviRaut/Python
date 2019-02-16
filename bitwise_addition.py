#!C:Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to add two numbers using bitwise operators.
'''

def bit_add(a,b):
    while b!=0:
        t = a & b
        a = a ^ b
        b = t << 1
    return a

def main():
    a,b = eval(input("Enter two numbers: "))
    ans = bit_add(a,b)
    print("Addition: ",ans)

if __name__=='__main__':
    main()


'''
OUTPUT:
Enter two numbers: 7,5
Addition:  12
'''
