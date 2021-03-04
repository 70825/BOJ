N=int(input());k=0
def CBNU(memo):
    for i in range(max(memo)):
        if i+1 not in memo:print('',end=" ")
        else:print('*',end="")
    print("")
if N%2==0:print('I LOVE CBNU')
else:
    print('*'*N)
    inp=N//2+1
    memo=[inp]
    for i in range(N//2+1):
        CBNU(memo)
        k+=1
        memo=[inp-k,inp+k]