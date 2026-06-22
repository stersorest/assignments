#Write a program to Move zeroes to end.
# n=input("enter the array: ")
# arr=list(map(int,n.split()))
# result=[]
# for num in arr:
#     if num!=0:
#         result.append(num)
# zeros=len(arr)-len(result)
# result+=[0]*zeros
# print("the resultant array is: ",result)

 #Write a program to Move zeroes to end.
n=input("enter the array: ")
arr=list(map(int,n.split()))
j=0 #for locking 0
for i in range(len(arr)): #0 to len-1
    if arr[i]!=0:
        arr[j],arr[i]=arr[i],arr[j] #909>900
        j+=1
print("the resultant array is: ",arr)

