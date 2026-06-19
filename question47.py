#Write a program to Write function for Fibonacci.....0,1,1,2,3,5
n=int(input("enter the number of terms: "))
def func_fib(n):
    a1=0
    a2=1
    for i in range(n):
        print(a1,end=" ")
        temp=a1+a2 #a1,a2=a2,a1+a2
        a1=a2
        a2=temp
func_fib(n)
