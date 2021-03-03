N,L=map(int,input().split())
k=0
num=1
while k!=N:
    if str(L) not in str(num):k+=1
    num+=1
print(num-1)