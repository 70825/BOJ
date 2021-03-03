D=[0]*10
S=input()
for i in range(len(S)):
    a=int(S[i])
    if a==6 or a==9:
        if D[6]>=D[9]:D[9]+=1
        else:D[6]+=1
    else:D[a]+=1
print(max(D))