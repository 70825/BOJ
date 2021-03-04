n=int(input())+1
k=str(n)
for i in range(len(k)-1,-1,-1):
    if k[i]=='0':n+=10**(len(k)-i-1)
print(n)