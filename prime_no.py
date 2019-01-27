#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to accept a number from the user and check if it is prime or not.
'''

def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print(n,"is not a Prime number.")
                break
        else:
            print(n,"is a Prime number.")
    else:
        print(n,"is not a Prime number.")
        
def main():
    num = eval(input("Enter a number: "))
    prime(num)

if __name__=="__main__":
    main()


'''
OUTPUT:
===== RESTART: C:\Users\Vaibhavi Raut\Desktop\PythonPrg\H.W\prime_no.py =====
Enter a number: 23
23 is a Prime number.
>>> 
===== RESTART: C:\Users\Vaibhavi Raut\Desktop\PythonPrg\H.W\prime_no.py =====
Enter a number: 2
2 is a Prime number.
>>> 
===== RESTART: C:\Users\Vaibhavi Raut\Desktop\PythonPrg\H.W\prime_no.py =====
Enter a number: 12
12 is not a Prime number.
>>> 
===== RESTART: C:\Users\Vaibhavi Raut\Desktop\PythonPrg\H.W\prime_no.py =====
Enter a number: 4
4 is not a Prime number.
>>> 
===== RESTART: C:\Users\Vaibhavi Raut\Desktop\PythonPrg\H.W\prime_no.py =====
Enter a number: 5
5 is a Prime number.
>>> 
'''
