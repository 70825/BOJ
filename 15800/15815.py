s = input()
q = []
for i in range(len(s)):
    if s[i] in ['+', '-', '*', '/']:
        y, x = q.pop(), q.pop()
        q.append(x+y if s[i] == '+' else x-y if s[i] == '-' else x*y if s[i] == '*' else x//y)
    else: q.append(int(s[i]))
print(q[0])