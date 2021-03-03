n=int(input())
D=[*map(int,input().split())]
Min=D
Max=D
for i in range(1,n):
    D=[*map(int,input().split())]
    nMin=[0]*3;nMax=[0]*3
    for j in range(3):
        nMin[j]=Min[1]
        nMax[j]=Max[1]
        if j!=2:
            nMin[j]=min(Min[0],nMin[j])
            nMax[j]=max(Max[0],nMax[j])
        if j!=0:
            nMin[j]=min(Min[2],nMin[j])
            nMax[j]=max(Max[2],nMax[j])
        nMin[j]+=D[j]
        nMax[j]+=D[j]
    Min=nMin;Max=nMax
print(max(Max),min(Min))