T=int(input())
for i in range(T):
    a=0;A=0;B=0;C=0
    M=int(input())
    N=str(input())
    for j in range(M):
        if 65<=ord(N[j])<=90:A+=1
        elif 97<=ord(N[j])<=122:a+=1
        elif 48<=ord(N[j])<=57:B+=1
        else:C+=1
    if M>=12 and min(a,A,B,C)>0:print('valid')
    else:print('invalid')