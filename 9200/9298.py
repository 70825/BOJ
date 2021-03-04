input=__import__('sys').stdin.readline
for i in range(int(input())):
    X=[];Y=[]
    for j in range(int(input())):
        x,y=map(float,input().split())
        X.append(x);Y.append(y)
    H=max(X)-min(X)
    V=max(Y)-min(Y)
    print('Case '+str(i+1)+': Area '+str(H*V)+', Perimeter '+str(2*H+2*V))