for i in range(int(input())):
    memo=[]
    N=int(input())
    k='';z=''
    S=str(input())
    for j in range(len(S)):
        if S[j]=='O':z+='0'
        else:z+='1'
        if len(z)%8==0:
            memo.append(int(z,2))
            z=''
    for j in range(len(memo)):
        k+=chr(memo[j])
    print("Case #{}: {}".format(i+1,k))