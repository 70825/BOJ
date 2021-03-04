from collections import deque
N,C=map(int,input().split())
Dict={}
D=[*map(int,input().split())]
for i in range(N):
    if D[i] in Dict:Dict[D[i]]+=1
    else:Dict[D[i]]=1
Dict=deque(sorted(Dict.items(),key=lambda x:x[1],reverse=True))
while Dict:
    a,b=Dict.popleft()
    for i in range(b):print(a,end=' ')