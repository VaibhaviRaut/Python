#!C:\Users\Vaibhavi Raut\AppData\Local\Programs\Python\Python37

'''
WAP to accept a string from user and return the first and the last two characters
of the input string.
'''

word = input("Enter a word: ")
l = len(word)
#res = word[2:]
res = word[:2] 
res += word[l-2:]

print("Output: ",res)



'''
OUTPUT:
case 1:
-res = word[2:]
-res = word[:2]
Enter a word: spring
Output:  ringsp

case 2:
-res = word[2:]
Enter a word: spring
Output:  ring

case3:
-res = word[:2]
Enter a word: spring
Output:  sp

case 4: FINAL OUTPUT
-res = word[:2] 
-res += word[l-2:]
Enter a word: spring
Output:  spng
'''
