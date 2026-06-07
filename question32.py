#Write a program to Print repeated-number pattern. 1 22 333
r=int(input("enter no of rows: "))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()