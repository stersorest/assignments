#Write a program to Print reverse star pattern.
r=int(input("enter no of rows: "))
for i in range(r,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()