input=__import__('sys').stdin.readline
n,q=map(int,input().split())
D=[*map(int,input().split())]
k=[]
for i in range(q):
    S=[*map(int,input().split())]
    if S[0]==1:
        k.append(sum(D[S[1]-1:S[2]]))
        s=D[S[1]-1];D[S[1]-1]=D[S[2]-1];D[S[2]-1]=s
    else:k.append(sum(D[S[1]-1:S[2]])-sum(D[S[3]-1:S[4]]))
for i in range(q):print(k[i])