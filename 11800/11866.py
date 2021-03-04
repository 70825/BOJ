N,M=map(int,input().split())
D=[(i+1) for i in range(N)]
Jo=[];k=-1
while D:
    k=(k+M)%len(D)
    Jo.append(D.pop(k))
    k-=1
print('<{}>'.format(', '.join(map(str,Jo))))