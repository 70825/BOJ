t=input()
p=input()
n,m=len(t),len(p)
fail = [0]*m
result = []
i,j=1,0
while i<m:
    if p[i]==p[j]:j+=1;fail[i]=j;i+=1
    else:
        if j!=0:j=fail[j-1]
        else:fail[j]=0;i+=1
i,j=0,0
while i<n:
    if p[j]==t[i]:i+=1;j+=1
    if j==m:result.append(i-j+1);j=fail[j-1]
    elif i<n and p[j]!=t[i]:
        if j!=0: j=fail[j-1]
        else:i+=1
print(len(result))
print(' '.join(map(str,result)))