s = input()
q = []
for i in range(len(s)):
    q.append(s[i])
    while len(q) >= 4 and q[len(q)-4:] == ['P', 'P', 'A', 'P']:
        for j in range(4): q.pop()
        q.append('P')
print(['NP','PPAP'][q == ['P']])