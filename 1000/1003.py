T=int(input());
def fi(N):
    k=2;s=[1,0];d=[0,1];a=0;b=0
    while k<=N:
        a=s[0]+s[1]
        b=d[0]+d[1]
        s[0]=s[1];d[0]=d[1]
        s[1]=a;d[1]=b
        k+=1
    return print(a,b)
for i in range(T):
    N=int(input())
    if N==0:
        print('1 0')
    elif N==1:
        print('0 1')
    else:
        fi(N)