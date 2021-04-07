n = int(input())
D = [*map(int,input().split())]
q = []
x = 1
for i in range(len(D)):
    if D[i] == x: x+=1
    else: q.append(D[i])
    while q:
        if q[-1] != x: break
        q.pop();x += 1
print(['Nice','Sad'][bool(q)])