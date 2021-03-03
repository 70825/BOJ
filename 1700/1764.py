N,M=map(int,input().split())
n=[];m=[];s=0
for i in range(N):S=str(input());n.append(S)
for i in range(M):S=str(input());m.append(S)
K=list(set(n)&set(m))
print(len(K))
K.sort()
for i in range(len(K)):
    print(K[i])