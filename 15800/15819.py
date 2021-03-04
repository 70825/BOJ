N,K=map(int,input().split())
D=[]
for i in range(N):
    S=str(input())
    D.append(S)
D.sort()
print(D[K-1])