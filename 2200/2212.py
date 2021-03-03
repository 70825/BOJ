n=int(input())
k=int(input())
D=sorted(set([*map(int,input().split())]))
length=sorted([D[i]-D[i-1] for i in range(1,len(D))])[::-1]
print(sum(length)-sum(length[:k-1]))