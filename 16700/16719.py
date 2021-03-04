S=[*input()]
D=['']*len(S)
b=''
for i in range(len(S)):
    q=[]
    for j in range(len(S)):
        if D[j]=='':
            D[j]=S[j];p=D+[]
            q.append(''.join(map(str,p)))
            D[j]=''
    q.sort();print(q[0])
    for j in range(len(S)):
        if D[j]=='':
            D[j]=S[j]
            if ''.join(map(str,D))==q[0]:break
            D[j]=''