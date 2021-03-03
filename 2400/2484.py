N=int(input())
c=[0]*N
for i in range(N):
    B=input().split()
    C=[0,0,0,0,0,0]
    d=0;m=0;
    for j in range(4):
        for k in range(6):
            if int(B[j])==k+1:
                C[k]+=1
    for j in range(6):
        if max(C)==C[j]:
            d+=j+1;m+=1
    if max(C)==4:
        c[i] = 50000+d*5000
    elif max(C)== 3:
        c[i] = 10000+d*1000
    elif max(C)==2 and m==2:
        c[i] = 2000+d*500
    elif max(C)==2:
        c[i] = 1000+d*100
    elif max(C)==1:
        c[i] = int(max(B))*100
print(max(c))