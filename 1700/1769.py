N=str(input());k=0
while len(N)!=1:
    s=0
    for i in range(len(N)):s+=int(N[i])
    N=str(s);k+=1
print(k)
if int(N)%3==0:print('YES')
else:print('NO')