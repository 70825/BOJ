r,c,n=map(int,input().split())
if r%n==0:k=r//n
else:k=r//n+1
if c%n==0:l=c//n
else:l=c//n+1
print(k*l)