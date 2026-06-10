#Write a program to Print number pyramid 1 121 12321 1234321
n=int(input("enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print()