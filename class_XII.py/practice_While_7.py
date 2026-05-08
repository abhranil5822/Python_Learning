#wap to find reverse of a number
n=int(input("Enter Any number :"))
rev=0
while n>0:
    rev=(rev*10)+(n%10)
    n//=10
print (rev)