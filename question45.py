#Write a program to Write function for palindrome.
n=int(input("enter a number:"))
def func_palindrome(n):
    temp=n
    rev=0
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if temp==rev:
       return True
    else:
       return False
result = func_palindrome(n)
if result:
    print("yes")
else:
    print("no")