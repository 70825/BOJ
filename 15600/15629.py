T=int(input())
D=[];k=0;so=0
for i in range(T):
    A=str(input())
    D.append(A)
for i in range(T):
    if D[i]=='ethiopia' or D[i]=='tanzania' or D[i]=='kenya':k+=50
    elif D[i]=='south-africa':so=1
    elif D[i]=='namibia' and so==1:k+=40
    elif D[i]=='namibia' and so==0:k+=140
    elif i>=1 and D[i]=='zambia' and D[i-1]=='zimbabwe':k+=20
    elif i>=1 and D[i]=='zimbabwe' and D[i-1]=='zambia':k+=0
    elif D[i]=='zambia':k+=50
    elif D[i]=='zimbabwe':k+=30
print(k)