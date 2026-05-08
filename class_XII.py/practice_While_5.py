#wap to find number of digits in a number
n=int(input("Enter Any number :"))
dig=0
while n>0:
    dig+=1
    n//=10
print (dig)