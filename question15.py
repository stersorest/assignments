#Write a program to Check Armstrong number.
#153=1+125+27
n=int(input("enter a number: "))
k=n
count=0
t=n
while(t>0):
    t=t//10
    count+=1
sum=0
t=n
while t>0:
    r=t%10
    sum+=r**count
    t=t//10
if sum==k:
    print("yes armstrong")
else:
    print("no")