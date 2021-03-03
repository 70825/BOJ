while 1:
    a,b=map(str,input().split())
    if a==b=='0':break
    memo_a=[int(a[i]) for i in reversed(range(len(a)))]
    memo_b=[int(b[i]) for i in reversed(range(len(b)))]
    if len(a)>=len(b):
        for i in range(len(a)-len(b)):
            memo_b.append(0)
    else:
        for i in range((len(b)-len(a))):
            memo_a.append(0)
    memo_sum=[0]*max(len(a),len(b))
    ans=0
    for i in range(len(memo_sum)):
        memo_sum[i]+=memo_a[i]+memo_b[i]
        if memo_sum[i]>=10:
            if i!=len(memo_sum)-1:
                memo_sum[i]-=10
                memo_sum[i+1]+=1
                ans+=1
            else:ans+=1
    print(ans)