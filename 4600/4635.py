while 1:
    N=int(input())
    if N==-1:break
    speed=[]
    time=[]
    ans=0
    for i in range(N):
        s,t=map(int,input().split())
        speed.append(s)
        time.append(t)
    ans+=speed[0]*time[0]
    for i in range(N-1):
        ans+=speed[i+1]*(time[i+1]-time[i])
    print(ans,'miles')