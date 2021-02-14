def go(x):
    global leaf
    if len(Children[x])==0:leaf+=1;return
    for nx in Children[x]:go(nx)
n=int(input())
D=[*map(int,input().split())]
Del=int(input())
Children=[[] for _ in range(n)]
Parent=[-1]*n
root=-1
leaf=0
for i in range(n):
    if D[i]==-1:root=i;continue
    Children[D[i]].append(i)
    Parent[i]=D[i]
if Del==root:print(0)
else:
    for i in range(len(Children[Parent[Del]])):
        if Del==Children[Parent[Del]][i]:
            Children[Parent[Del]].pop(i);break
    go(root)
    print(leaf)