k=0
while 1:
    S=[*map(int,input().split())]
    if len(S)==1:break
    if k!=0:print('')
    N=S[0];S.pop(0)
    for a in range(N-5):
        for b in range(a+1,N-4):
            for c in range(b+1,N-3):
                for d in range(c+1,N-2):
                    for e in range(d+1,N-1):
                        for f in range(e+1,N):
                            print(S[a],S[b],S[c],S[d],S[e],S[f])
    k+=1