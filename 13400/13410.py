N,K=map(int,input().split())
D=[]
for i in range(K):
    S=str(N*(i+1))
    a=''
    for j in range(len(S)):a+=S[len(S)-1-j]
    D.append(int(a))
print(max(D))