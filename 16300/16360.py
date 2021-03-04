memo=['a','i','y','l','n','o','r','t','u','v','w']
sub_memo=['as','ios','ios','les','anes','os','res','tas','us','ves','was']
for i in range(int(input())):
    S=str(input())
    k=0
    for j in range(11):
        if S[len(S)-1]==memo[j]:S=S[:len(S)-1:]+sub_memo[j];k=1
    if k!=1 and S[len(S)-2::]=='ne':S=S[:len(S)-2:]+'anes';k=1
    if k!=1:S+='us'
    print(S)