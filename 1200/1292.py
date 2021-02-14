A,B=map(int,input().split())
u=0;D=[];k=1
while u!=B:
    for i in range(k):
        D.append(k);u+=1
        if u==B:break
    if u==B:break
    k+=1
print(sum(D[A-1:B:1]))