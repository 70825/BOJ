N,K=map(int,input().split())
D=[]
for i in range(N):
    a,b,c,d=map(int,input().split())
    if D not in [b,c,d]:
        D.append([b,c,d])
    if K==a:
        S=[b,c,d]
D=sorted(D,reverse=True)
for i in range(len(D)):
    if D[i]==S:print(i+1);break