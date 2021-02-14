Dict={}
z=9;ans=0
for i in range(int(input())):
    k=input()
    for j in range(len(k)):
        if k[j] not in Dict:Dict[k[j]]=10**(len(k)-j-1)
        else:Dict[k[j]]+=10**(len(k)-j-1)
D=sorted(Dict.values(),reverse=True)
for i in D:ans+=i*z;z-=1
print(ans)