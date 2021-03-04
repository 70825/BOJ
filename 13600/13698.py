k=str(input());m=[1,0,0,2]
for i in range(len(k)):
    if k[i]=='A':t=m[0];m[0]=m[1];m[1]=t
    elif k[i]=='B':t=m[0];m[0]=m[2];m[2]=t
    elif k[i]=='C':t=m[0];m[0]=m[3];m[3]=t
    elif k[i]=='D':t=m[1];m[1]=m[2];m[2]=t
    elif k[i]=='E':t=m[1];m[1]=m[3];m[3]=t
    elif k[i]=='F':t=m[2];m[2]=m[3];m[3]=t
for i in range(4):
    if m[i]==1:print(i+1)
for i in range(4):
    if m[i]==2:print(i+1)