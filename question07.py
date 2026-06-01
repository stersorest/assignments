#products of a number
n=int(input("enter a number: "))
product=1
while(n>0):
    digit=n%10
    product=product*digit
    n=n//10
print(product)
  