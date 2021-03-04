k=int(input())
memo1=input();memo2=input()
eq=0;di=0
ans=0
for i in range(len(memo1)):
    if memo1[i]==memo2[i]:eq+=1
    else:di+=1
if eq>=k:
    ans+=k
    ans+=di
else:
    ans+=eq
    ans+=di-(k-eq)
print(ans)