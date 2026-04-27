# A program to calculate the sum of squares from 1 to n
n=int(input("Enter a num: "))
sum=0
for i in range(1,n+1):
	sum+= i*i
print ("Sum of 1^2 to ",n,"^2 = ",sum)