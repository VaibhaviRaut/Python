#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to accept a number from user and print it's table.
'''

n = eval(input("Enter a number:"))
t = eval(input("Till what number do you want the table: "))     
r = t+1
for x in range(r):
    ans = x*n
    print(x,"*",n,"=",ans)
    
'''
line 10, in <module>
    for x in n:
TypeError: 'int' object is not iterable .............?????
Answer to the ERROR: in print(): '+' is used for string to concatanate and
',' is used for integers.
OUTPUT with #:

Enter a number:2
0 * 2 = 0
1 * 2 = 2
2 * 2 = 4
3 * 2 = 6
4 * 2 = 8
5 * 2 = 10
6 * 2 = 12
7 * 2 = 14
8 * 2 = 16
9 * 2 = 18
>>>
Enter a number:2
0 * 2 = 0
1 * 2 = 2
2 * 2 = 4
3 * 2 = 6
4 * 2 = 8
5 * 2 = 10
6 * 2 = 12
7 * 2 = 14
8 * 2 = 16
9 * 2 = 18
10 * 2 = 20

OUTPUT without #:

=== RESTART: C:/Users/Vaibhavi Raut/Desktop/PythonPrg/H.W/forLoop_Table.py ===
Enter a number:4
Till what number do you want the table: 10
0 * 4 = 0
1 * 4 = 4
2 * 4 = 8
3 * 4 = 12
4 * 4 = 16
5 * 4 = 20
6 * 4 = 24
7 * 4 = 28
8 * 4 = 32
9 * 4 = 36
10 * 4 = 40
>>> 
'''
