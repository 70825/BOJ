N=int(input());k=0;m=0;D=[]
A=input().split()
for i in range(1,N):
    if int(A[k])>int(A[i]):m+=1
    elif int(A[k])<int(A[i]):D.append(m);m=0;k=i
D.append(m)
print(max(D))