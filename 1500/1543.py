a = input()
b = input()
ans = 0
i = len(b)
while 1:
    if i > len(a):break
    if a[i-len(b):i] == b:
        ans += 1
        i += len(b)
    else: i += 1
print(ans)