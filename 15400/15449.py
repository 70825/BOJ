D=[*map(int,input().split())]
ans=0
D.sort()
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            if D[k]<D[i]+D[j]:ans+=1
print(ans)