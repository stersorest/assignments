#Write a program to Print character triangle.A AB ABC ABCD
r=int(input("enter no of rows: "))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
