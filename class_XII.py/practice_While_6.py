#wap to find sum of digits of a number
n=int(input("Enter Any number :"))
sum=0
while n>0:
    sum+=n%10
    n//=10
print (sum)