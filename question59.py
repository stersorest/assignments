#Write a program to Rotate array right.
n=input("enter the array: ")
arr=n.split()
d=int(input("enter d: "))
d=d%len(arr)
arr=arr[-2:]+arr[:-2]
print("rotated array: ",arr)