input=__import__('sys').stdin.readline
K,L=map(int,input().split())
D={}
for i in range(L):
    S=input().rstrip()
    D[S]=i
for i in sorted(D,key=lambda k:D[k])[:K]:
    print(i)