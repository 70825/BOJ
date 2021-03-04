memo={'O':15.9994,'C':12.011,'H':1.00794,'S':32.066,'N':14.00674}
N=int(input())
for j in range(N):
    S=str(input())
    a = '';num = '';ans = 0;err=0
    for i in range(len(S)):
        if 48<=ord(S[i])<=57:num+=S[i]
        elif S[i] not in memo:err+=1
        else:
            if len(a)==0:a+=S[i]
            elif len(a)==1:
                if len(num)==0:ans+=memo[a]
                else:ans+=memo[a]*int(num)
                a=S[i];num=''
    if len(num)==0:ans+=memo[a]
    else:ans+=memo[a]*int(num)
    if err==0:print("{0:.4f}".format(ans))
    else:print('Invalid formula')