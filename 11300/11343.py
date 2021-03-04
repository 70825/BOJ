memo=['RRR','YYY','OOO','BBB','GGG','PPP']
for i in range(int(input())):
    str(input())
    n,m=map(int,input().split())
    D=[[] for k in range(n)]
    for j in range(n):
        D[j]=[*map(str,input().split())]
    find=0
    for j in range(n):
        for k in range(m-2):
            if D[j][k]+D[j][k+1]+D[j][k+2] in memo:
                k+=1;j+=1
                print(j,k,j,k+1,j,k+2)
                find=1
                break
        if find==1:break
    if find==0:
        for j in range(n-2):
            for k in range(m):
                if D[j][k]+D[j+1][k]+D[j+2][k] in memo:
                    j+=1;k+=1
                    print(j,k,j+1,k,j+2,k)
                    find=1
                    break
            if find==1:break
    if find==0:
        print('no set found')