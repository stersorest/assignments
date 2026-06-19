#Write a program to Write function for perfect number.
n=int(input("enter a number: "))
def func_perf(n):
    total=0
    for i in range(1,n):
            if n%i==0:
                total+=i
    if total==n:
         return True
    else:
         return False
result=func_perf(n)
if result:
     print("yes")
else:
     print("false")
