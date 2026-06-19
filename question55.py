#Write a program to Second largest element.
n=input("enter the array: ")
arr=n.split()
max1=int(arr[0])
max2=int(arr[0])
for i  in arr:
    num=int(i)
    if num>max1:
       max2=max1
       max1=num
    elif num>max2 and max2!=max1:
        max2=num
print(f"the max is {max1} and the second max is {max2}")


    