#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to sort the given list in ascending order using Insertion Sort.
'''

def insertion_sort(x,n):
    for i in range(1,n):
        temp = x[i]
        j=i-1
        while (temp<x[j] and j>=0):
            x[j+1]=x[j]
            j-=1
        x[j+1]=temp
        print(x)
    return x

def main():
    x = eval(input("Enter a List: "))
    print("Iteraions: ")
    print("Sorted List: ",insertion_sort(x,len(x)))

if __name__=='__main__':
    main()
    
