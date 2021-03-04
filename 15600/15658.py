N=int(input())
num=[*map(int,input().split())]
a,b,c,d=map(int,input().split())
def step(D,index,cur,a,b,c,d):
    if index == len(D):return (cur,cur)
    res=[]
    if a>0:res.append(step(D,index+1,cur+D[index],a-1,b,c,d))
    if b>0:res.append(step(D,index+1,cur-D[index],a,b-1,c,d))
    if c>0:res.append(step(D,index+1,cur*D[index],a,b,c-1,d))
    if d>0:
        if cur>=0:res.append(step(D,index+1,cur//D[index],a,b,c,d-1))
        else:res.append(step(D,index+1,-(-cur//D[index]),a,b,c,d-1))
    ans=(
        max(t[0] for t in res),
        min(t[1] for t in res)
    )
    return ans
ans=step(num,1,num[0],a,b,c,d)
print(ans[0])
print(ans[1])