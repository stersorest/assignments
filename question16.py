# Write a program to print Armstrong numbers in a range

start = int(input("enter the lower limit: "))
end = int(input("enter the upper limit: "))
for i in range(start, end + 1):
    k = i
    count = len(str(i))
    temp = i
    sum = 0
    while temp > 0:
        r = temp % 10
        sum += r ** count
        temp = temp // 10
    if sum == k:
        print(i)