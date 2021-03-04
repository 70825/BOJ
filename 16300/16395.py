n,k=map(int,input().split())
if n==1 and k==1:print('1')
else:
    n-=1;k-=1
    a=1;b=1;c=1
    for i in range(n):a*=(i+1)
    for i in range(k):b*=(i+1)
    for i in range(n-k):c*=(i+1)
    print(int(a/(b*c)))