n = int(input())
X = [*map(int,input().split())]
S = sorted(set(X))
D = {}
for i in range(len(S)):D[S[i]] = i
print(*[D[X[i]] for i in range(len(X))])