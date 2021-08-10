n = int(input())
arr = sorted([int(input()) for _ in range(n)])
ans = 0
modok = 1
for i in range(n):
    if arr[i] > modok:
        ans += arr[i] - modok
        modok += 1
    elif arr[i] == modok:
        modok += 1
print(ans)