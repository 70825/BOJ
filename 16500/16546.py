N=int(input())
D=sum([*map(int,input().split())])
print(N*(N+1)//2-D)