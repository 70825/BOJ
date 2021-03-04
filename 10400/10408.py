S=str(input())
memo=[]
k=0
while k<len(S):
    if k!=len(S)-1 and S[k]+S[k+1]=='10':
        memo.append(10);k+=1
    else:memo.append(int(S[k]))
    k+=1
print("{0:.2f}".format(sum(memo)/len(memo)))