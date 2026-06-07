#Write a program to Find largest prime factor.
n = int(input("enter a number: "))

largest = -1

for i in range(2, n + 1):
    if n % i == 0:
        
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        
        if is_prime:
            largest = max(largest, i)

print("largest prime factor:", largest)