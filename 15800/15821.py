from sys import stdin
K,N=map(int,stdin.readline().split())
E=[]
for i in range(K):
    P=int(stdin.readline())
    memo=[]
    xy=[*map(int,stdin.readline().split())]
    E.append(max(xy[2*j]**2+xy[2*j+1]**2 for j in range(len(xy)//2)))
E.sort()
print("{0:.2f}".format(E[N-1]))