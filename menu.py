#!C:\User\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
Convert the arithmatic.py into a menu driven program.
'''

def add(a,b):
    return a+b+10

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def main():
    ch =''
    while ch!="no":
        print("MENU")
        print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
        n=eval(input("Enter choice: "))
        if n==1:
            a,b = eval(input("Enter two numbers: "))
            print("Addition: ",add(a,b))
            #break
        elif n==2:
            a,b = eval(input("Enter two numbers: "))
            print("Subtraction: ",sub(a,b))
            #break
        elif n==3:
            a,b = eval(input("Enter two numbers: "))
            print("Multiplication: ",mul(a,b))
            #break
        elif n==4:
            a,b = eval(input("Enter two numbers: "))
            print("Division: ",div(a,b))
            #break
        else:
            print("Wrong Choice!")
        print("Do you wish to continue? (yes/no)")
        ch = input("=> ")
        continue

if __name__=="__main__":
    main()

'''
OUTPUT:

======= RESTART: C:/Users/Vaibhavi Raut/Desktop/PythonPrg/H.W/menu.py =======
MENU
1. Addition 
2. Subtraction 
3. Multiplication 
4. Division
Enter choice: 1
Enter two numbers: 45,70
Addition:  125
Do you wish to continue? (yes/no)
=> yes
MENU
1. Addition 
2. Subtraction 
3. Multiplication 
4. Division
Enter choice: 4
Enter two numbers: 90,2
Division:  45.0
Do you wish to continue? (yes/no)
=> yes
MENU
1. Addition 
2. Subtraction 
3. Multiplication 
4. Division
Enter choice: 2
Enter two numbers: 125,67
Subtraction:  58
Do you wish to continue? (yes/no)
=> yes
MENU
1. Addition 
2. Subtraction 
3. Multiplication 
4. Division
Enter choice: 121,88
Wrong Choice!
Do you wish to continue? (yes/no)
=> yes
MENU
1. Addition 
2. Subtraction 
3. Multiplication 
4. Division
Enter choice: 3
Enter two numbers: 121,88
Multiplication:  10648
Do you wish to continue? (yes/no)
=> no
>>>
'''
