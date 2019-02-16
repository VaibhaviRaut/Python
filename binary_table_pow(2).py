#!C:Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to accept a number from user of 2's power and print it's binary table.
'''

def bin_table(n):
    for i in range(1,11):
        m = i*n
        if (m&3)==0:                #or even 2 can work instead of 3
            print(m," = ",'{0:08b}'.format(m))
        else:
            break
#2's pow: 2,4,8,16,32,64,128

def main():
    n = eval(input("Enter a number: "))
    bin_table(n)

if __name__=='__main__':
    main()
    

'''
OUTPUT:
Enter a number: 12
12  =  00001100
24  =  00011000
36  =  00100100
48  =  00110000
60  =  00111100
72  =  01001000
84  =  01010100
96  =  01100000
108  =  01101100
120  =  01111000

Enter a number: 16
16  =  00010000
32  =  00100000
48  =  00110000
64  =  01000000
80  =  01010000
96  =  01100000
112  =  01110000
128  =  10000000
144  =  10010000
160  =  10100000
'''
