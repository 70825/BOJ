N=int(input())
s=0
for i in range(N):
    A,B=map(int,input().split())
    s+=A*B
print(s)