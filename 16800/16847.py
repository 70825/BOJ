n=int(input())
for _ in range(1,n+1):
    a,b=map(int,input().split())
    D=input();ans=0
    s=[[] for _ in range(b)]
    for i in range(a):
        z=input()
        for j in range(len(z)):
            s[j].append(z[j])
    for i in range(b):
        if D[i] not in s[i]:ans+=1
    print('Data Set {}:'.format(_))
    print('{}/{}'.format(ans,b))
    if _!=n:print()