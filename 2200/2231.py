N=int(input())
ans=0
for i in range(1,N):
    D=i
    for j in range(len(str(i))):
        D+=int(str(i)[j])
    if D==N:ans=i;break
print(ans)