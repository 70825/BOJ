s = [*input()]
t = [*input()]
while len(s) != len(t):
    if t[-1] == 'A': t.pop()
    else: t.pop(); t = t[::-1]
flag = True
for i in range(len(s)):
    if t[i] != s[i]: flag = False
print([0, 1][flag])