#Write a program to Calculate sum of first N natural numbers.
#1)using recursion-
def func_sum(N):
    if N==0:
        return 0
    else:
        return func_sum(N-1)+N
print(func_sum(3))

#2)while loop-
N=int(input("enter a number: "))
i=0
sum=0
while i<=N:
    sum=sum+i
    i+=1
print("the sum:",sum)

