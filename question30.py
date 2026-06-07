#Write a program to Print number triangle.1..12..123...1234
r=int(input("enter no of rows: "))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()