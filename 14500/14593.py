N=int(input())
memo1=[]
for i in range(N):
    a,b,c=map(int,input().split())
    memo1.append([-a,b,c,i+1])
print(sorted(memo1)[0][3])