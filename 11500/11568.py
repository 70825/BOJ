n = int(input())
D = [*map(int,input().split())]
ans = [1]*n
for i in range(n-1,-1,-1):
    for j in range(i-1,-1,-1):
        if D[i] > D[j]: ans[j] = max(ans[j],ans[i]+1)
print(max(ans))