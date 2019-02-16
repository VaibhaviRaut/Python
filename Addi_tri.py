#!C:Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to print
1  2  
2  4  6  
3  6  9  12  
4  8  12  16  20
'''

def double(n):
   for i in range(1,n+1):
       k = i
       for j in range(1,i+2):
           print(k," ",end='')
           k += i
       print()

def main():
    n = eval(input("Enter number: "))
    double(n)

if __name__=='__main__':
    main()


'''
OUTPUT:
Enter number: 4
1  2  
2  4  6  
3  6  9  12  
4  8  12  16  20  
'''
