#!C:\User\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to print the following pattern:
*
* *
* * *
* * * *
'''

def pattern(r):
    
    for i in range(r):
        for y in range(0,i+1):
            print("*",end=' ')
        print("\n")

def main():
    rows = eval(input("Enter the number of rows you wish: "))
    pattern(rows)

if __name__=="__main__":
    main()

'''
OUTPUT:

===== RESTART: C:\Users\Vaibhavi Raut\Desktop\PythonPrg\H.W\pattern1.py =====
Enter the number of rows you wish: 5
* 

* * 

* * * 

* * * * 

* * * * * 

>>>
'''
