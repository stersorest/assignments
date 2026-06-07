#Write a program to Find x^n without pow().2^3=1*2*2^2
x=int(input("enter the base value: "))
n=int(input("enter the power: "))
result=1
while(n>0):
    result=result*x
    n=n-1
print("answer is: ",result)
    