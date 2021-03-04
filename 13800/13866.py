a=list(map(int,input().split()))
a.sort()
print(abs(a[3]+a[0]-a[1]-a[2]))