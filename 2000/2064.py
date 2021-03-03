IP_memo=[]
N=int(input())
for i in range(N):
    IP=[*map(int,input().split('.'))]
    ans=''
    for j in range(4):
        k=bin(IP[j])[2::]
        ans+='0'*(8-len(k))+k
    IP_memo.append(ans)
k=-1
for i in range(32):
    for j in range(1,N):
        if IP_memo[0][i]!=IP_memo[j][i]:
            k=i;break
    if k!=-1:
        break
min_IP=IP_memo[0][:k:]+'0'*(32-k)
Answer_IP=[]
Mask='1'*k+'0'*(32-k)
if k==-1:
    Mask='1'*32
    min_IP=IP_memo[0]
Answer_Mask=[]
for i in range(0,32,8):
    Answer_IP.append(int(min_IP[i:i+8:],2))
    Answer_Mask.append(int(Mask[i:i+8:],2))
print('.'.join(map(str,Answer_IP)))
print('.'.join(map(str,Answer_Mask)))