#Write a program to Find duplicates in array.
n = input("enter the array: ")
arr = n.split()
for i in range(len(arr)):
    count = 0
    
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    
    if count > 1 and arr[i] not in arr[:i]:
        print(arr[i])