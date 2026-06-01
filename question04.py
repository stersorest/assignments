#Write a program to Count digits in a number.
n=int(input("enter a number: "))
count=0
if (n==0):
    count=1
else:
    while(n>0):
        n=n//10
        count+=1
print(count)

