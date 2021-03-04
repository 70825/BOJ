n,m = map(int,input().split())
ans = 1
if n > 2 and m >= (n-1)//3 + 1: ans += 1
if n > 1 and m >= n//2 : ans += 1
if n > 1 and m >= (n+1)//2 : ans += 1
if m >= n: ans += 1
if n > 2 and m >= n + (n-1)//3 + 1: ans += 1
if n > 2 and m >= n//2 + (n-1)//3 + 1: ans += 1
if n > 2 and m >= (n+1)//2 + (n-1)//3 + 1 : ans += 1
print(ans)