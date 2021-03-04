m=int(input())
n=m+1
while 1:
    k=(n*(n+1)//2+m*(m-1)//2)**0.5
    if k==int(k):break
    n+=1
print(m,int(k),n)