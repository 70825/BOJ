input=__import__('sys').stdin.readline
for i in range(int(input())):
    K=int(input());k=[*map(int,input().split())];N=int(input());n=0;memo=[]
    for j in range(N):
        S=[*map(int,input().split())]
        if S[0] in k:
            if S[1]!=-1:
                if S[1]<6 or (S[1]==6 and S[2]==0):n+=1
                if len(memo)==0:memo.append([S[0],S[1],S[2]])
                else:
                    if S[1]<memo[0][1] or (S[1]==memo[0][1] and S[2]<memo[0][2]):memo.pop(0);memo.append([S[0],S[1],S[2]])
    print(memo[0][0], n)