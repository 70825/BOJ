def find(x):
    if(p[x]==x):return x
    z=find(p[x])
    path[x]+=path[p[x]]
    p[x]=z
    return p[x]
def merge(x,y):
    p[x]=y
    path[x] = abs(x-y)%1000
input=__import__('sys').stdin.readline
for __ in range(int(input())):
    n=int(input())
    p=[i for i in range(n)]
    path=[0]*n
    while 1:
        INPUT=input().split()
        if INPUT[0]=='O':break
        if INPUT[0]=='I':
            z,a,b=INPUT
            a=int(a)-1;b=int(b)-1
            merge(a,b)
        else:
            a=int(INPUT[1])-1
            find(a);print(path[a])