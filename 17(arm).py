m=int(input())
sum=0
a=m
while m>0:
	c=m%10
	sum=sum+c*c*c
	m=m//10
if a==sum:
	print("yes")
else:
	print("no")
