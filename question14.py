#Write a program to Find nth Fibonacci term.
n=int(input("enter the nth term: "))
a=0
b=1
i=1
while(i<=n):
    if(i==n):
            print("the nth term is:",a)
    print(a)
    a,b=b,a+b
    i+=1
