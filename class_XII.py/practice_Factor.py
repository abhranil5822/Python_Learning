# A program to calculate the factor of any num
n=int(input("Enter a num: "))
mid=n//2
for i in range(1,mid+1):
	if (n%i==0):
		print (i, end =" ")