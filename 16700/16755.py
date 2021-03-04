S=input()
j=0;D='HONI';ans=0
for i in range(len(S)):
    if S[i]==D[j]:j+=1
    if j==4:ans+=1;j=0
print(ans)