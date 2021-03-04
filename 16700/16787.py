n=int(input())
S=input();t=0;ans=0
while t<=n-1:
    if t+1<=n-1 and S[t]+S[t+1] in ['OX','XO']:ans+=1;t+=2
    else:t+=1
print(ans)