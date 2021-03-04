D={}
for i in range(int(input())):
    A,B=map(str,input().split())
    if B=='enter':D[A]=1
    else:D[A]=0
B=sorted([*D.keys()],reverse=True)
for i in B:
    if D[i]==1:print(i)