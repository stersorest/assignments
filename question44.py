#Write a program to Write function to find factorial.
def f_fact(n):
    if(n<=0 or n==1):
        return 1
    else :
        result=n*f_fact(n-1)
        return result
result=f_fact(4)
print(result)
    

    