#Write a program to Count even and odd elements.
n=input("enter the array: ")
arr=n.split()
print(arr)
even=0
odd=0
for i in arr:
    num=int(i)
    if num%2==0:
        even+=1
    else:
        odd+=1
print(f"odd={odd}")
print(f"even={even}")