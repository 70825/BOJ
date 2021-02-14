input=__import__('sys').stdin.readline
q=[]
n=int(input())
for i in range(n):
    q.append([int(input()),i])
q.sort()
cnt=0
for i in range(n):
    cnt=max(q[i][1]-i,cnt)
print(cnt+1)