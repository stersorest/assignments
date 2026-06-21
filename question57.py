#Write a program to Reverse array.
n=input("enter the array: ")
arr=n.split()
reversed_array=[]
for i in range(len(arr)-1,-1,-1): #reversed counting of index
    reversed_array.append(arr[i])
print("the rev arr is: ",reversed_array)

