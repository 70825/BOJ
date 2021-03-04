while 1:
    S=str(input())
    if S=='#':break
    s=[]
    D=['a','e','i','o','u']
    for i in range(len(S)):
        s.append(S[i])
    for i in range(len(S)):
        if s[0] not in D:
            s.append(s[0])
            s.pop(0)
        else:break
    print(''.join(map(str,s))+'ay')