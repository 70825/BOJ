D={};k=0;Sum=0
while 1:
    try:
        S=input();k+=1
        if S not in D:D[S]=1
        else:D[S]+=1
    except EOFError:break
for i in D.values():Sum+=(i/k)**2
print(1-Sum)