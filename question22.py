#Write a program to Convert binary to decimal.
#1010=0*2^0+1*2^1+0*2^2+1*2^3
n=input("enter a binary: ")
power=0
dec=0
for digit in reversed(n):
    dec=int(digit)*(2**power)
    power+=1
print("decimal value is: ",dec)
