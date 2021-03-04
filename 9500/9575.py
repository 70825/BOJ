Z=input;X=map
for _ in range(int(input())):
    ans=0;D=[]
    Z();K=[*X(int,Z().split())]
    Z();L=[*X(int,Z().split())]
    Z();M=[*X(int,Z().split())]
    for x in K:
        for y in L:
            for z in M:
                S=str(x+y+z);e=0
                for w in range(len(S)):
                    if S[w] not in '58':e+=1
                if e==0 and S not in D:ans+=1;D.append(S)
    print(ans)