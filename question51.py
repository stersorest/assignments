#Write a program to Find largest and smallest element.
n=input("enter the array: ")
arr=n.split()
print(arr)
largest=int(arr[0])
smallest=int(arr[0])
for i in arr:
    num=int(i)
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
print(f"the largest={largest}")
print(f"the smallest={smallest}")