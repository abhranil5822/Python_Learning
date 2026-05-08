#wap to check a given number is palindrome or not?
n=int(input("Enter Any number :"))
x=n
rev=0
while n>0:
    rev=(rev*10)+(n%10)
    n//=10
if (x==rev) :
    print ("Palindrome")
else :
    print ("Not Palindrome")