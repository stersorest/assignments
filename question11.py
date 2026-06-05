#Write a program to Find GCD of two numbers.
# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# gcd=1
# for i in range(1,min(a,b)+1):
#     if (a%i==0)and(b%i==0):
#         gcd=i
# print(gcd)


#or by using euclidean algo:

a=int(input("enter first number: "))
b=int(input("enter second number: "))
while(b!=0): #a%b==0
    a,b=b,a%b
    print("GCD is: ",a)
