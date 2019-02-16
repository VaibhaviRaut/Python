#!C:Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
3-2-19
WAP to accept a string from user and print count of consonants in it.
'''

def count(s):
    l = len(s)
    cnt = 0
    v = 0
    for x in s:
        if x in "aeiouAEIOU":#x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
            v +=1#continue
        else:
            cnt+=1
    print("Vowels: ",v)
    return cnt
            
def main():
    s = input("Enter a String: ")
    y = count(s)
    print("Count of Consonants in String: ",y)

if __name__=='__main__':
    main()
