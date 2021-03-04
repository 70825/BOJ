X,Y,M=map(int,input().split())
MAX=0
for i in range(M//X,-1,-1):
    k=0
    while 1:
        k+=1
        if X*i+Y*k>M:k-=1;break
    if X*i+Y*k>MAX:MAX=X*i+Y*k
print(MAX)