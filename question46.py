#Write a program to Write function for Armstrong.
def func_arm(n):
    digit=0
    arm=0
    count = 0
    t = n
    while t > 0:
        count += 1
        t = t // 10
        temp=n
    while n>0:
        digit=n%10
        arm=arm+digit**count
        n=n//10
    if(arm==temp):
        return True
    else:
        return False
    
result= func_arm(153)   
if result:
    print("yes")
else:
    print("no")