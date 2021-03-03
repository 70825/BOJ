N=int(input());k=1
for i in range(N):
    k*=(i+1)
k=str(k)
for i in reversed(range(len(k))):
    if k[i]!='0':print(k[i]);break