#!C:Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to accept 2 numbers from user, accept the bit position and accept number of
bits to be swapped at the corresponding bit position form the given numbers.
Example:
->Input:
n1: 01001100 n2: 001101101
pos = 6  bits = 3
->Output:
n1: 01_101_100  n2: 001_001_101
''' 

def swap(x,y,p,b):
    mask = (1<<b)-1
    mask = mask<<(p-b)
    x_part = x & mask
    y_part = y & mask
    x = x & ~mask
    y = y & ~mask
    x = x | y_part
    y = y | x_part
    return x,y
    

def main():
    a = eval(input("Enter a Number 1: "))
    b = eval(input("Enter a Number 2: "))
    pos = eval(input("Enter a bit position: "))
    bits = eval(input("Enter a number of bits: "))
    x,y = swap(a,b,pos,bits)
    print("After Swapping: ")
    print("Number 1: ",x)
    print("Number 2: ",y)

if __name__=='__main__':
    main()


'''
OUTPUT:
Enter a Number 1: 1512
Enter a Number 2: 1234
Enter a bit position: 7
Enter a number of bits: 4
After Swapping: 
Number 1:  1488
Number 2:  1258
'''
