a=[*map(int,input().split())]
b=[*map(int,input().split())]
memo=[]
for i in [0,1,2,]:
    for j in [0,1,2,3,4,5,6]:
        memo.append([round(a[i]/b[j],2),i+1,j+1])
memo.sort()
for i in range(21):
    print("{0:.2f}".format(memo[i][0]),memo[i][1],memo[i][2])