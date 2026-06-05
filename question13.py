#Write a program to Generate Fibonacci series.
#0,1,1,2,3,5,8...
n=int(input("enter the nummber of terms: "))
a1=0
a2=1
i=1
while(i<=n):
    print(a1,end=" ")
    a1,a2= a2,a1+a2 #a1 is current no,a2 is next number
    i+=1


# 01
# 11
# 12
# 23
# 35