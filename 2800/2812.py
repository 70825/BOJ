n, k = map(int, input().split())
s = [*map(int, [*input()])]
q = []
for i in range(n):
    while k and q and q[-1] < s[i]:
        q.pop()
        k -= 1
    q.append(s[i])
print(''.join(map(str, q[:len(q)-k])))