n = int(input())
arr = [int(input()) for _ in range(n)]
plus = sorted([arr[i] for i in range(n) if arr[i] > 1])
minus = sorted([arr[i] for i in range(n) if arr[i] <= 0], reverse=True)
zero = [arr[i] for i in range(n) if arr[i] == 0]
one = [arr[i] for i in range(n) if arr[i] == 1]
ans = 0
while plus:
    x = plus.pop()
    if not plus: ans += x
    else: ans += x * plus.pop()
while len(minus) > 1:
    x = minus.pop()
    if minus: ans += x * minus.pop()
ans += len(one)
if not zero and minus: print(ans + minus[0])
else: print(ans)