n=int(input())
s=list(map(int,input().split()))[:n]
a=s.sort()
middleIndex =int( (len(s))/2)
print(s[middleIndex])
