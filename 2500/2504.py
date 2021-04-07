s = input()
q = []
flag = False
for i in range(len(s)):
    if s[i] in '([': q.append(s[i])
    elif len(q):
        if q[-1]+s[i] == '()': q.pop()
        elif q[-1]+s[i] == '[]':q.pop()
        else: flag = True
    else: flag = True
if flag or q: print(0);exit()
for i in range(len(s)):
    if s[i] in '([': q.append(s[i])
    else:
        if s[i] == ')':
            if q[-1] == '(':
                q.pop()
                q.append(2)
            else:
                x = q.pop()
                q.pop()
                q.append(2*x)
        else:
            if q[-1] == '[':
                q.pop()
                q.append(3)
            else:
                x = q.pop()
                q.pop()
                q.append(3*x)
    if len(q) >= 2 and type(q[-1]) == type(q[-2]) == int:
        q.append(q.pop()+q.pop())
print(q[0])