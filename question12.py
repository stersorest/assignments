#Write a program to Find LCM of two numbers.
a=int(input("enter first number: "))
b=int(input("enter second number: "))
x,y=a,b #storing og val
while(b!=0): #a%b==0
    a,b=b,a%b 
print("GCD is: ",a)
GCD=a
LCM=(x*y)//GCD
print("LCM is: ",LCM)