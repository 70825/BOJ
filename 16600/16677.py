m=input()
memo=[]
score=[]
for i in range(int(input())):
    w,g=map(str,input().split())
    k=0
    for j in range(len(w)):
        if m[k]==w[j]:k+=1
        if k==len(m):break
    if k==len(m):
        memo.append([int(g)/(len(w)-len(m)),w])
        score.append(int(g)/(len(w)-len(m)))
if len(memo)==0:print('No Jam')
else:
    sub_memo=[]
    for i in memo:
        if i[0]==max(score):
            sub_memo.append(i[1])
    print(sub_memo[0])