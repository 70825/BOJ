input=__import__('sys').stdin.readline
k=1
s=[]
while True:
    N=int(input())
    if N==0:break
    D=[[] for i in range(N)]
    for i in range(N):
        D[i].append(str(input()))
    for i in range(2*N-1):
        a,b=input().split()
        a=int(a)
        D[a-1].append(b)
    for i in range(N):
        if len(D[i])<3:
            c=D[i][0]
            break
    s.append([k,c])
    k+=1
for i in range(len(s)):
    print(s[i][0],s[i][1],end="")