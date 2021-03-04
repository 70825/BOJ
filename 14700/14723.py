N=int(input())
k=1
while 1:
    if k*(k-1)//2<N<=(k+1)*(k)//2:break
    k+=1
p=(N-(k*(k-1)//2))%(k+1)
print(k-p+1,p)