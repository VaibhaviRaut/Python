#!C:Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
3-2-19
"Foundation"
WAP to accept a number for user and a bit position  to turn off from the given
number. Print number in decimal after turning off the bit. If already off then let
it be
Example: 16 bit=5 answer:0
Note: turn off always lsb to msb
the no. and create no. with inverse of that binary no. ex: 0001000 and
inverse: 1110111
'''

def bit_change(n,b):
    t = n
    x = 1
    x = x<<(b-1)
    x = ~x
    r = t & x
    return r

def main():
    n = eval(input("Enter a number: "))
    b = eval(input("Enter the bit position: "))
    print("Binary of n: ",bin(n))
    print("Number: ",n,"Bit Position: ",b)
    r = bit_change(n,b)
    print("Answer: ",r)
    print("Binary of answer: ",bin(r))


if __name__=='__main__':
    main()


'''
OUTPUT:
Enter a number: 16
Enter the bit position: 5
Number:  16 Bit Position:  5
Answer:  0

bin():
Enter a number: 16
Enter the bit position: 5
Binary of n:  0b10000
Number:  16 Bit Position:  5
Answer:  0
Binary of answer:  0b0
'''
