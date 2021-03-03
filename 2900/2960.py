N,K=map(int,input().split())
memo=[]
trash=[]
for i in range(2,N+1):
    memo.append(i)
for i in range(2,N+1):
    n=1
    if i in memo:
        while n*i<=N:
            if n*i in memo:
                trash.append(i*n)
                memo.remove(i*n)
            n+=1
print(trash[K-1])