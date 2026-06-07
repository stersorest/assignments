#Write a program to Check strong number.
#145=1!+4!+5!
n=int(input("enter a number: "))
temp=n
sum=0
while(n>0):
    digit=n%10
    fact=1
    total=0
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    n=n//10    
if(sum==temp):
    print("yes,strong number")
else:
    print("not a strong number")


