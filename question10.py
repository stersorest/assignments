#Write a program to Print prime numbers in a range.

start=int(input("enter the first number: "))
end=int(input("enter the last number: "))
for n in range(start,end+1):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         print(n,end=" ")
# or
    if (n>1):
        for i in range(2,int(n**0.5)+1):
            if (n%i==0):
                break
        else:
            print(n, end=" ")
