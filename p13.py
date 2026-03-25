n=int(input("Enter a Number:"))
sum=0
product=1
temp=n
while temp>0:
    digit=temp%10
    sum=sum+digit
    product=product*digit
    temp=temp//10
if sum==product:
        print(n,"is a spy number")
else:
        print(n,"is not a spy number")