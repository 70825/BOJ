m=input();N=[]*len(m)
for i in range(len(m)):
    N.append(m[i])
for i in range(len(N)-1,0,-1):
    if int(N[i])>=5:
        N[i]='0'
        N[i-1]=str(int(N[i-1])+1)
    else:
        N[i]='0'
        N[i-1]=str(int(N[i-1]))
for i in range(len(N)):
    print(N[i],end="")