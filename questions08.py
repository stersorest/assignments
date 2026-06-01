#Write a program to Check whether a number is palindrome.
n=int(input("enter a number: "))
rev=0
x=n
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if(x==rev):
    print("yes the number is a palindrome")
else:
    print("not a palindrome")