#Write a program to Rotate array left.
n = input("enter the array: ")
arr = n.split()

d = int(input("enter d: "))

d = d % len(arr)

arr = arr[d:] + arr[:d]

print("Rotated array:", arr)