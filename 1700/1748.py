N=input()
ans=0
for i in range(len(N)):
    if i+1!=len(N):
        ans+=(i+1)*(10**(i+1)-10**i)
    else:
        ans+=(i+1)*(int(N)-10**i+1)
print(ans)