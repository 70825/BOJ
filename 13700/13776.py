D=''
for _ in range(int(input())):
    if len(D)==26:break
    S=input()
    for i in range(len(S)):
        if 65<=ord(S[i])<=90 and S[i] not in D:D+=S[i]
print(D)