for _ in range(int(input())):
    N=int(input())
    D=[*map(int,input().split())]
    check=[False]*N;check[0]=True
    ans=0;q=[0]
    while q:
        x=q.pop()
        y=D[x]-1
        if check[y]==False:
            q.append(y)
            check[y]=True
        else:
            ans+=1
            for i in range(N):
                if check[i]==False:
                    q.append(i)
                    break
    print(ans)