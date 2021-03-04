input=__import__('sys').stdin.readline
memo=[]
k=1
for i in range(int(input())):
    S=input().split()
    if S[0]=='A':
        if S[1]=='L':memo.insert(0,k)
        else:memo.append(k)
        k+=1
    else:
        if S[1]=='L':memo=memo[int(S[2])::]
        else:memo=memo[:len(memo)-int(S[2]):]
print('\n'.join(map(str,memo)))