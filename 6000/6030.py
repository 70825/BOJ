memo1=[]
memo2=[]
P,Q=map(int,input().split())
for i in range(1,P+1):
    if P%i==0:memo1.append(i)
for i in range(1,Q+1):
    if Q%i==0:memo2.append(i)
for i in memo1:
    for j in memo2:
        print(i,j)