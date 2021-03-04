def init(now,s,e):
    if s==e:
        tree[now]=D[s]
        return tree[now]
    else:
        tree[now]=min(init(now*2,s,(s+e)//2),init(now*2+1,(s+e)//2+1,e))
        return tree[now]
def find(now,s,e,L,R):
    if s>R or e<L:return float('inf')
    if L<=s and e<=R:return tree[now]
    return min(find(now*2,s,(s+e)//2,L,R),find(now*2+1,(s+e)//2+1,e,L,R))
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[int(input()) for i in range(n)]
tree=[0]*(4*n)
init(1,0,n-1)
for i in range(m):
    a,b=map(int,input().split())
    print(find(1,0,n-1,a-1,b-1))