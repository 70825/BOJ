s=str(input())
k=str(input())
def p(s):
    for i in range(len(s)):
        if s[i]!=s[len(s)-1-i]:return 1
    return 0
if len(s)==1 or p(s)==0:print('YES')
else:print('NO')