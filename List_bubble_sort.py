#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to accept a list of integers from user to sort them using bubble sort.
it checks adjacent numbers in per iteration 
'''

'''
def sort_recur(x,n):
    if n==1:
        return
    for i in range(n+1):
        if(x[i]>x[i+1]):
            #swap(x[i],x[j]) #swap func won't work becoz it is swap by value not reference.
            temp = x[i]
            x[i] = x[i+1]
            x[i+1] = temp
        print(x)
    return sort_recur(x,n-1)
'''
def sort(x,n):
    for i in range(n):
        for j in range(0,n-i-1):
            if(x[j]>x[j+1]):
                #swap(x[i],x[j]) #swap func won't work becoz it is swap by value not reference.
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
            print(x)
    return x

def main():
    x = eval(input("Enter an integer List: "))
    print("Iterations:")
    print("Sorted List: ",sort(x,len(x)))
    #print("Sorted List: ",)

if __name__=='__main__':
    main()


'''
Enter an integer List: [3,2,4,1,5]
Iterations:
[2, 3, 4, 1, 5]
[2, 3, 4, 1, 5]
[2, 3, 1, 4, 5]
[2, 3, 1, 4, 5]
[2, 3, 1, 4, 5]
[2, 1, 3, 4, 5]
[2, 1, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
Sorted List:  [1, 2, 3, 4, 5]
'''
