while 1:
    A=[*map(int,input().split())]
    if A[0]==0:break
    ans=1
    for i in range(1,len(A),2):
        ans=ans*A[i]-A[i+1]
    print(ans)