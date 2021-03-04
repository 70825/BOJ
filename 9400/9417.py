def gcd(a,b):
    mod = a%b
    while mod>0:a=b;b=mod;mod=a%b
    return b
for i in range(int(input())):
    D=[]
    N=[*map(int,input().split())]
    for j in range(0,len(N)-1):
        for k in range(j+1,len(N)):
            D.append(gcd(N[j],N[k]))
    print(max(D))