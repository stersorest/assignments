#Write a program to Count set bits in a number.
n=int(input("enter a number: "))
count=0
binr=""
while(n>0):
    rem=n%2
    binr=str(rem)+binr
    if(rem==1):
        count+=1
    n=n//2
print("the binr val is: ",binr)
print("the set bits: ",count)

