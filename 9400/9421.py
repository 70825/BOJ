def primelist(n):
    s=[True]*(n+1)
    for i in range(2,int((n)**0.5)+1):
        if s[i]:
            for j in range(i+i,n+1,i):
                s[j]=False
    return [i for i in range(2,n+1) if s[i]]
def sangguen(x):
    arr=[x]
    while True:
        a=[*str(x)]
        ans=0
        for i in range(len(a)):
            ans+=int(a[i])**2
        if ans==1:return 1
        elif ans in arr:return 0
        else:arr.append(ans)
        x=ans
n=int(input())
D=primelist(n)
answer=[]
for i in range(len(D)):
    if sangguen(D[i])==1:answer.append(D[i])
print('\n'.join(map(str,answer)))