a,b,n=map(int,input().split());D=[]
for i in range(1,n+1):D.append((a+b)*i+a*(n-i))
print(*sorted(D))