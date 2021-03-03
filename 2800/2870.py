D=[]
for _ in range(int(input())):
    S=input()
    a=''
    for i in range(len(S)):
        if 48<=ord(S[i])<58:a+=S[i]
        else:
            if len(a)>0:D.append(int(a));a=''
    if len(a)>0:D.append(int(a))
print('\n'.join(map(str,sorted(D))))