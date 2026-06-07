#Write a program to Convert decimal to binary.
n=int(input("enter a number in decimal: "))
binary=""
while(n>0):
    rem=n%2
    binary=str(rem)+binary
    n=n//2
print("the value in binary is: ",binary)
