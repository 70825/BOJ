while 1:
    N=int(input())
    if N==0:break
    D=[[0.0,'a'] for i in range(N)]*N;t=[]
    for i in range(N):
        A,B=map(str,input().split())
        t.append(float(B))
        D[i][1]=A
        D[i][0]=float(B)
    for i in range(N):
        if max(t)==D[i][0]:print(D[i][1])