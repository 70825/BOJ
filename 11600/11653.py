n=int(input())
k=2
D=[]
while n!=1:
    if n%k==0:D.append(k);n//=k
    else:k+=1
for i in range(len(D)):
    print(D[i])