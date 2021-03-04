int(input())
a=list(map(int,input().split()))
a.sort();k=0
for i in range(len(a)-1):
    k+=a[i]*a[i+1]
    a[i+1]=a[i]+a[i+1]
print(k)