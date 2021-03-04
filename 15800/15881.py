N=int(input())
S=str(input());k=0;i=0
if N<=3:print(0)
else:
    while i<=len(S)-4:
        if S[i]+S[i+1]+S[i+2]+S[i+3]=='pPAp':k+=1;i+=4
        else:i+=1
    print(k)