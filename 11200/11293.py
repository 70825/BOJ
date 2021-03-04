for _ in range(int(input())):
    D=[]
    for i in range(int(input())):
        S=input()
        K=''
        for j in range(len(S)):
            if 65<=ord(S[j])<=90:K+=S[j]
        D.append(K)
    print('Customer',_+1)
    for i in range(int(input())):
        a,b,c,d,e=map(str,input().split())
        if D[int(a)-1][int(b)-1]==d and D[int(a)-1][int(c)-1]==e:print('correct')
        else:print('error')