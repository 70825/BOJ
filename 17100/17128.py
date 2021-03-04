n,q=map(int,input().split())
A=[*map(int,input().split())]
Q=[*map(int,input().split())]
D=[]
S=[[] for _ in range(n)]
for i in range(n):
    D.append(A[i%n]*A[(i+1)%n]*A[(i+2)%n]*A[(i+3)%n])
    for j in range(4): S[(i+j)%n].append(i)
ans=sum(D)
for x in Q:
    for y in S[x-1]:
        D[y]=-D[y];ans+=2*D[y]
    print(ans)