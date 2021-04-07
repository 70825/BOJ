n = int(input())
s = input()
d = {chr(i+65):int(input()) for i in range(n)}
q = []
for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90: q.append(d[s[i]])
    else:
        y, x = q.pop(),q.pop()
        if s[i] == '+': q.append(x+y)
        if s[i] == '-': q.append(x-y)
        if s[i] == '*': q.append(x*y)
        if s[i] == '/': q.append(x/y)
print('{:.2f}'.format(q[0]))