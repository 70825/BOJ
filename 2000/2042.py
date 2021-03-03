def init(now, s, e):
    if s==e:
        tree[now] = D[s]
        return tree[now]
    else:
        tree[now] = init(now*2, s, (s+e)//2) + init(now*2+1, (s+e)//2+1,e)
        return tree[now]
def Sum(now,s,e,L,R):
    if L > e or R < s:return 0
    if L <= s and e <= R:
        return tree[now]
    return Sum(now*2, s, (s+e)//2, L,R) + Sum(now*2+1,(s+e)//2+1,e,L,R)
def update(now,s,e,idx,val):
    if idx < s or idx > e: return
    tree[now] += val
    if s!=e:
        update(now*2, s, (s+e)//2, idx, val)
        update(now*2+1, (s+e)//2+1,e, idx, val)
input=__import__('sys').stdin.readline
n,m,k=map(int,input().split())
D=[int(input()) for i in range(n)]
tree=[0]*(4*n)
init(1,0,n-1)
for i in range(m+k):
    a,b,c=map(int,input().split())
    b-=1
    if a==1:
        val=c-D[b]
        D[b]=c
        update(1, 0, n-1, b, val)
    else:print(Sum(1,0,n-1,b,c-1))