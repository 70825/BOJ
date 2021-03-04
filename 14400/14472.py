n,m,k=map(int,input().split());a=0
D=[list(map(str,[*input()])) for _ in range(n)]
for t in  range(2):
    if t==1:D=[*zip(*D[::-1])]
    for i in range(len(D)):
        for j in range(0,len(D[i])-k+1,1):
            if '#' not in D[i][j:j+k]:a+=1
print(a)