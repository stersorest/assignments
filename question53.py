#Write a program to Linear search.
n=input("enter the array: ")
arr=n.split()
key=int(input("enter the element to find: "))
Found=False
for i in range(len(arr)):
    if int(arr[i])==key:
        print(f"element found at index: {i}")
        Found=True
        break
if Found==False:
    print("element not found")