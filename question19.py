#Write a program to Print factors of a number.4=1,2,4
n=int(input("enter a number: "))
for i in range(1,n+1):
    if(n%i==0):
        print(i)
