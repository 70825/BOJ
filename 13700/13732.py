from collections import deque
n,m=map(int,input().split())
D=[list(map(str,[*input()])) for _ in range(n)]
for i in range(m):
    Box=deque()
    z=n-1
    for j in range(n-1,-1,-1):
        if D[j][i]=='#':Box.append(j)
        elif D[j][i]=='a':
            if len(Box)==0:
                if z!=j:D[j][i]='.';D[z][i]='a'
            elif Box[0]<j and z!=j:
                if z!=j:D[j][i]='.';D[z][i]='a'
            else:
                while Box[0]>j:
                    z=Box.popleft()-1
                    if len(Box)==0:break
                if z!=j:D[j][i]='.';D[z][i]='a'
            z-=1
for i in range(n):print(''.join(D[i]))