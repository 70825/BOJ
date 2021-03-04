N=int(input())
D=[*map(int,input().split())]
def prev_permutation(a,n):
    i=n-1
    while i>0 and a[i-1]<=a[i]:i-=1
    if i<=0:return [-1]
    j=n-1
    while a[j]>=a[i-1]:j-=1
    a[i-1],a[j]=a[j],a[i-1]
    j=n-1
    while i<j:
        a[i],a[j]=a[j],a[i]
        i+=1;j-=1
    return a
print(' '.join(map(str,prev_permutation(D,N))))