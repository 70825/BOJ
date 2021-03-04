N=int(input())
D=[*map(int,input().split())]
def next_permutation(a,n):
    i=n-1
    while i>0 and a[i-1]>=a[i]:i-=1
    if i<=0:return [-1]
    j=n-1
    while a[j]<=a[i-1]:j-=1
    x=a[i-1];a[i-1]=a[j];a[j]=x
    j=n-1
    while i<j:
        x=a[i];a[i]=a[j];a[j]=x
        i+=1;j-=1
    return a
print(' '.join(map(str,next_permutation(D,N))))