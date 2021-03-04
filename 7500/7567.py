S=input()
ans=10
for i in range(1,len(S)):
    if S[i-1]!=S[i]:ans+=10
    else:ans+=5
print(ans)