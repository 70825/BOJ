input=__import__('sys').stdin.readline
N=int(input())
D=[*map(int,input().split())]
S=int(input())
p=0
for i in range(N):
    if D[i]!=0:
        if D[i]%S!=0:
            p+=((D[i]//S+1)*S)
        else:p+=(D[i]//S)*S
print(p)