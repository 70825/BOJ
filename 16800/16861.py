n=int(input())
while 1:
    k=str(n);z=0
    for i in range(len(k)):
        z+=int(k[i])
    if n%z==0:print(n);break
    else:n+=1