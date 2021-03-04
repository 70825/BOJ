for i in range(int(input())):
    GOLDEN={'G':0,'O':0,'L':0,'D':0,'E':0,'N':0}
    S=input()
    for j in range(len(S)):
        if S[j] in GOLDEN:
            GOLDEN[S[j]]+=1
    print(GOLDEN[min(GOLDEN,key=GOLDEN.get)])