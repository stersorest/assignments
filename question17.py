#Write a program to Check perfect number. 6=1+2+3
n=int(input("enter a number: "))
sum=0
for i in range(1,int(n/2)+1):
    if(n%i==0):
        sum+=i
    
if(sum==n):
    print("yes,perfect number")
else:
    print("no")