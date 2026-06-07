#Write a program to Print repeated character pattern.  A BB CCC DDDD
r=int(input("enter no of rows: "))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()