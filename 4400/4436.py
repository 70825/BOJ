while 1:
    try:
        D=[0,0,0,0,0,0,0,0,0,0]
        N=int(input())
        ans=1
        while min(D)==0:
            k=str(ans*N)
            for i in range(len(k)):
                D[int(k[i])]+=1
            ans+=1
        print(ans-1)
    except EOFError:break