s = input()
k = input()
x, y = 0, len(k)

ans = 0
while y <= len(s):
    if k == s[x:y]:x += len(k);y += len(k);ans += 1
    else:x += 1;y += 1
print(ans)