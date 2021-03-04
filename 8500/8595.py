N=int(input())
S=input()
k=''
memo=[]
for i in range(N):
    if 48<=ord(S[i])<=59:k+=S[i]
    else:
        if len(k)!=0:memo.append(int(k))
        k=''
if len(k)!=0:memo.append(int(k))
print(sum(memo))