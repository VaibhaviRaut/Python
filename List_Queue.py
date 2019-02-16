#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to implement queue data structure using list.
'''

def enque(x,n):
    x.append(n)
    return x
    
def dequeue(x):
    return x.pop(0)

def is_empty(x):
    return len(x)==''

def is_full(x):
    return len(x)==11

def peep(x):
    return x[-1]

def main():
    x = eval(input("Enter the List: "))
    ch = ''
    while ch!=0:
        print("MENU\n1. Enqueue\n2. Dequeue\n3. Is_Empty\n4. Is_Full\n5. Peep\n6. Exit")
        ch = eval(input("Enter Choice: "))
        if ch==1:
            n = eval(input("Enter the number: "))
            enque(x,n)
            print("Queue: ",x)
            print("\n")
        elif ch==2:
            print("Element: ",dequeue(x))
            print("Queue: ",x)
            print("\n")
        elif ch==3:
            if is_empty(x)==True:
                print("Queue is EMPTY!")
            else:
                print("Queue is NOT Empty!")
            print("\n")
        elif ch==4:
            if is_full(x)==True:
                print("Queue is FULL!")
            else:
                print("Queue is NOT Full!")
            print("\n")
        elif ch==5:
            print("First element: ",peep(x))
            print("\n")
        elif ch==6:
            ch=0
            print("\n")
        else:
            print("Wrong Choice!\n")
            print("Do you wish to continue? (Enter 0 to exit)\n")
            ch = eval(input("Enter Choice: "))

if __name__=='__main__':
    main()


'''
OUTPUT:
Enter the List: [1,3,2,4,5,6]
MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 1
Enter the number: 7
Queue:  [1, 3, 2, 4, 5, 6, 7]


MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 1
Enter the number: 8
Queue:  [1, 3, 2, 4, 5, 6, 7, 8]


MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 2
Element:  1
Queue:  [3, 2, 4, 5, 6, 7, 8]


MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 2
Element:  3
Queue:  [2, 4, 5, 6, 7, 8]


MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 3
Queue is NOT Empty!


MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 4
Queue is NOT Full!


MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 1
Enter the number: 1
Queue:  [2, 4, 5, 6, 7, 8, 1]


MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 1
Enter the number: 2
Queue:  [2, 4, 5, 6, 7, 8, 1, 2]


MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 1
Enter the number: 5
Queue:  [2, 4, 5, 6, 7, 8, 1, 2, 5]


MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 1
Enter the number: 7
Queue:  [2, 4, 5, 6, 7, 8, 1, 2, 5, 7]


MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 1
Enter the number: 9
Queue:  [2, 4, 5, 6, 7, 8, 1, 2, 5, 7, 9]


MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 4
Queue is FULL!


MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 5
First element:  9


MENU
1. Enqueue
2. Dequeue
3. Is_Empty
4. Is_Full
5. Peep
6. Exit
Enter Choice: 6

'''
