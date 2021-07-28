s = input()
ans = [0, 0]
x = s[0]
for i in range(1, len(s)):
    if x != s[i]:
        if x == '0': ans[0] += 1
        else: ans[1] += 1
        x = s[i]
if x == '0': ans[0] += 1
else: ans[1] += 1

print(min(ans))