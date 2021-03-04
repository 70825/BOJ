for i in range(int(input())):
    a,b,c=map(int,input().split())
    ans=0
    print('Case #'+str(i+1)+':',end=" ")
    k=0
    for j in range(a):
        ans+=(b+k)//c
        if (b+k)%c!=0:ans+=1
        k=(b+k)%c
    print(ans)