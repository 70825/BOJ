n = int(input())
a = [*map(int, input())]
b = [*map(int, input())]
s = a[:]
ans1 = 0
for i in range(n-1):
    if s[i] != b[i]:
        for j in range(i, i+3):
            if j < n: s[j] = 1 - s[j]
        ans1 += 1
flag1 = True if s == b else False
s = a[:]
s[0], s[1] = 1-s[0], 1-s[1]
ans2 = 1
for i in range(n-1):
    if s[i] != b[i]:
        for j in range(i, i+3):
            if j < n: s[j] = 1 - s[j]
        ans2 += 1
flag2 = True if s == b else False

print(min(ans1, ans2) if flag1 and flag2 else ans1 if flag1 else ans2 if flag2 else -1)