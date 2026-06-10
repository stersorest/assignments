#Write a program to Print reverse pyramid.
n=int(input("enter no of rows: "))
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,2*(n-i)+2):
        print("*",end="")
    print()