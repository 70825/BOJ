D=['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
for i in range(int(input())):
    S=str(input())
    print('Case #'+str(i+1)+':',end=" ")
    for j in range(len(S)):
        if 97<=ord(S[j])<=122:print(D[ord(S[j])-97],end="")
        else:print(S[j],end="")
    print("")