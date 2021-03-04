A=int(input());k=-1;s=0
B=input().split()
for i in range(A):
    if k==-1 and int(B[i])==0:k=0;s+=1
    if k==0 and int(B[i])==1:k=1;s+=1
    elif k==1 and int(B[i])==2:k=2;s+=1
    elif k==2 and int(B[i])==0:k=0;s+=1
print(s)