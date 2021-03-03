def min_init(now,s,e):
    if s==e:
        min_tree[now]=D[s]
        return min_tree[now]
    else:
        min_tree[now]=min(min_init(now*2,s,(s+e)//2),min_init(now*2+1,(s+e)//2+1,e))
        return min_tree[now]
def max_init(now,s,e):
    if s==e:
        max_tree[now]=D[s]
        return max_tree[now]
    else:
        max_tree[now]=max(max_init(now*2,s,(s+e)//2),max_init(now*2+1,(s+e)//2+1,e))
        return max_tree[now]
def min_find(now,s,e,L,R):
    if s>R or e<L:return float('inf')
    if L<=s and e<=R:return min_tree[now]
    return min(min_find(now*2,s,(s+e)//2,L,R),min_find(now*2+1,(s+e)//2+1,e,L,R))
def max_find(now,s,e,L,R):
    if s>R or e<L:return 0
    if L<=s and e<=R:return max_tree[now]
    return max(max_find(now*2,s,(s+e)//2,L,R),max_find(now*2+1,(s+e)//2+1,e,L,R))
input=__import__('sys').stdin.readline
n,m=map(int,input().split())
D=[int(input()) for i in range(n)]
min_tree=[0]*(4*n)
max_tree=[0]*(4*n)
min_init(1,0,n-1)
max_init(1,0,n-1)
for i in range(m):
    a,b=map(int,input().split())
    a-=1;b-=1
    print(min_find(1,0,n-1,a,b),end=' ')
    print(max_find(1,0,n-1,a,b))