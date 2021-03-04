T=int(input())
for i in range(T):
    N=int(input())
    if N==1:
        print('#')
    elif N==2:
        print('##')
        print('##')
    else:
        A=[[]*N for i in range(N)]
        for j in range(N):
            for k in range(N):
                if j==0 or j==N-1:print('#',end="")
                else:
                    if k==0 or k==N-1:print('#',end="")
                    else:print('J',end="")
            print("")
    print("")