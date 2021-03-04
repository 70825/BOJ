import sys
def go(t,v,Max):
    if t>=len(k):
        for i in range(1,Max+1):
            if D[i]==0:return
        for i in range(1,v):
            for j in range(51):
                if D[j]==i:print(j,end=' ')
        sys.exit(0)
    a=int(k[t])
    if a==0:return
    if D[a]==0:D[a]=v;Max=max(Max,a);go(t+1,v+1,Max);D[a]=0
    a=int(k[t:t+2])
    if a==0:return
    if a<=50 and D[a]==0:D[a]=v;Max=max(Max,a);go(t+2,v+1,Max);D[a]=0
k=input()
D=[0]*51
go(0,1,0)