t=int(input())
sum=0
a=t
while t>0:
	c=t%10
	sum=sum+c*c*c
	t=t//10
if a==sum:
	print("yes")
else:
	print("no")
