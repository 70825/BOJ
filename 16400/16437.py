def go(x):
    for nx in Children[x]:go(nx)
    p,num=Tree[x]
    if num>0:Tree[p][1]+=num
import sys
sys.setrecursionlimit(200000)
input=__import__('sys').stdin.readline
n=int(input())
Children=[[] for _ in range(n)]
Tree=[[-1,0] for _ in range(n)]
for i in range(1,n):
    a,b,c=input().split()
    b=int(b);c=int(c)
    Children[c-1].append(i)
    Tree[i]=[c-1,b] if a=='S' else [c-1,-b]
go(0)
print(Tree[0][1])