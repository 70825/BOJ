input=__import__('sys').stdin.readline
for _ in range(int(input())):
    n=int(input())
    D=sorted([*map(int,input().split())])
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            left=j+1;right=n-1
            while left<=right:
                mid=(left+right)//2
                if D[j]-D[i]==D[mid]-D[j]:ans+=1;break
                elif D[j]-D[i]<D[mid]-D[j]:right=mid-1;
                else:left=mid+1
    print(ans)