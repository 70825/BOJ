from collections import defaultdict as dd
n = int(input())
name = sorted(input().split())
up = dd(lambda: [])
family = dd(lambda: [0,[]])
for i in range(int(input())):
    a,b = input().split()
    up[a].append(b)
    family[a][0] += 1
root = list(set(name) - set(up.keys()))
for child in up.keys():
    x = family[child][0]
    for parent in up[child]:
        if x - 1 == family[parent][0]:
            family[parent][1].append(child)
print(len(root))
print(*sorted(root))
for x in name:
    print(x,len(family[x][1]),*sorted(family[x][1]))