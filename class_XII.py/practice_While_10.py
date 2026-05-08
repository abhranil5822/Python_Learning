#wap to find factors of a number
n=int(input("Enter Any number :"))
i=1
while i<=(n//2):
    if n%i==0 :
        print (i, end=" ")
    i+=1
print (n)