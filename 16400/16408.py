D=['A','2','3','4','5','6','7','8','9','T','J','Q','K']
memo=[0]*len(D)
String=[*map(str,input().split())]
for i in String:
    for j in range(len(D)):
        if i[0]==D[j]:memo[j]+=1
print(max(memo))