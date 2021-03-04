from collections import deque
n,b,w=map(int,input().split())
D=[*input()]
white=deque()
black=deque()
res=0
hi=0
while hi<n:
    if len(black)<=b:
        if D[hi]=='W':white.append(hi)
        else:black.append(hi)
        hi+=1
    else:
        t=black.popleft()
        while white:
            if t>white[0]:white.popleft()
            else:break
    if len(white)>=w and len(black)<=b:res=max(res,len(white)+len(black))
print(res)