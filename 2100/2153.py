N=str(input())
ans=0
for i in range(len(N)):
    if 65<=ord(N[i])<=90:
        ans+=ord(N[i])-65+27
    else:
        ans+=ord(N[i])-96
p=0
for i in range(2,ans):
    if ans%i==0:p=1;break
if ans in (1,2,3) or p==0:print('It is a prime word.')
else:print('It is not a prime word.')