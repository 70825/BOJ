C,K,P=map(int,input().split())
k=0
for i in range(1,C+1):
    k+=K*i+P*i**2
print(k)