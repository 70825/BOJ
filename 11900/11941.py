n, k = map(int, input().split())
s = [*input()]
p = []
h = []
for i in range(n):
    if s[i] == 'H': h.append(i)
    else: p.append(i)

ans = 0
while p and h:
    if p[-1] - k <= h[-1] <= p[-1] + k:
        ans += 1
        h.pop()
        p.pop()
    elif p[-1] - k > h[-1]: p.pop()
    else: h.pop()
print(ans)