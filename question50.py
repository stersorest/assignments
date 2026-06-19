#Write a program to Find sum and average of array.
n=input("enter the array: ")
arr=n.split()
print(arr)
sum=0
for i in arr:
    sum=sum+int(i)
avg=sum/len(arr)
print(f"total={sum}")
print(f"the avg={avg}")
