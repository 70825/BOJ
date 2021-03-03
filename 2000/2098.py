def TSP(now, visited):
    if C[now][visited] != -1: return C[now][visited]
    if visited == (1<<n)-1:
        if D[now][0]!=0: return D[now][0]
        return Max
    C[now][visited] = Max
    for i in range(n):
        if visited & (1<<i) or D[now][i]==0:continue
        C[now][visited] = min(C[now][visited], TSP(i, visited | (1<<i)) + D[now][i])
    return C[now][visited]
Max=10**10
n=int(input())
D=[[*map(int,input().split())] for _ in range(n)]
C=[[-1]*(1<<n) for _ in range(n)]
print(TSP(0,1))