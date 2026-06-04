#check prime
n=int(input("enter a number: "))
prime=1
if(n<=1):
    print("invalid")
else:
    i=2
    while(i<= n**0.5):
        if(n%i==0):
            prime=0
            i+=1
            break
if(prime==0):
     print("not prime")
else:
    print("prime")
