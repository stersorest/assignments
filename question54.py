#Write a program to Frequency of an element.
n=input("enter the array: ")
arr=n.split()
key=int(input("enter the required element: "))
count=0
for i in arr:  #i is the elements in arr.
    if int(i)==key:
        count+=1
print(f"the frequency of {key} is {count}")
