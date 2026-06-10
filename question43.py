#Write a program to Write function to check prime.
n=int(input("enter a number:  "))
def fxn_prime(n):
    prime=1
    for i in range(2,n//2+1):
        if(n%i==0):
            return "not prime"
    return "prime"
result=fxn_prime(n)
print(result)