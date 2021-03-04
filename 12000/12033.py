from collections import Counter
for _ in range(int(input())):
    n=int(input())
    D=[*map(int,input().split())]
    S=dict(Counter(D))
    Q=[]
    for i in range(len(D)):
        if S[D[i]]>0 and int((D[i]/3*4)) in S:
            Q.append(D[i])
            S[D[i]]-=1
            S[int(D[i]/3*4)]-=1
        if len(Q)==n:break
    print('Case #{}: {}'.format(_+1,' '.join(map(str,Q))))