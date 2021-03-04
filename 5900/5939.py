memo=[]
for i in range(int(input())):
    memo.append([*map(int,input().split())])
memo.sort()
for i in memo:print(i[0],i[1],i[2])