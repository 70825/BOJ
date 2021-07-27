D = {}
for i in range(26):
    D[chr(ord('A') + i)] = i

s = 'A' + input()
ans = 0

for i in range(1, len(s)):
    x = max(D[s[i]], D[s[i-1]])
    y = min(D[s[i]], D[s[i-1]])
    ans += min(x - y, abs(x - y - 26))
print(ans)