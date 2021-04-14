ans = False
n = int(input())
for k in range(2,11):
    x = n
    num = []
    while x != 0:
        num.append(x%k)
        x//=k
    s = ''.join(map(str,num[::-1]))
    flag = True
    for i in range(len(s)):
        if s[i] != s[-1-i]: flag = False
    if flag:
        ans = True
        print(k,s)
if not ans: print('NIE')