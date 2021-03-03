memo=['e','p','l','r','a','g','f','s','o','x','v','c','w','t','i','b','z','d','h','n','y','k','m','j','u','q']
sub_memo=[]
for i in range(26):
    sub_memo.append(memo[i].upper())
while 1:
    try:
        S=input()
        for i in range(len(S)):
            if 97<=ord(S[i])<=122:print(memo[ord(S[i])-97],end="")
            elif 65<=ord(S[i])<=90:print(sub_memo[ord(S[i])-65],end="")
            else:print(S[i],end="")
        print("")
    except EOFError:break