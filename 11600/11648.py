N=str(input());d=0
while len(N)!= 1:
    s=1
    for i in range(len(N)):
        s*=int(N[i])
    N=str(s)
    d+=1
print(d)