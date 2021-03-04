for _ in range(int(input())):
    N=int(input())
    ans,avg=0,0
    for i in range(N):
        a,b=map(float,input().split())
        ans+=a;avg+=b*a
    print(int(ans),'{0:.1f}'.format(avg/ans))