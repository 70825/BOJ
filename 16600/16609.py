N=int(input())
D=sorted([*map(int,input().split())])
for a,b in zip(range(1,N+1),D):D[a-1]=b/a
print('impossible' if max(D)>1 else min(D))