D=[[*input()] for _ in range(4)]
A='ABCDEFGHIJKLMNO.'
ans=0
for i in range(4):
    for j in range(4):
        if D[i][j]=='.':continue
        z=A.find(D[i][j])
        x,y=z//4,z%4
        ans+=abs(x-i)+abs(j-y)
print(ans)