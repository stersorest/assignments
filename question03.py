#factorial
n=int(input("enter the number: "))
fact=1
if (n==0 or n==1):
    print("1")
else:
        i=1
        while (i<=n):
            fact=fact*i
            i+=1
        print(fact)
