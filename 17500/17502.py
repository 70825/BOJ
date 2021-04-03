n = int(input())
s = list(input())
for i in range(len(s)//2+1):
    if s[i] == '?' and s[len(s)-1-i] == '?':
        s[i],s[len(s)-1-i] = 'a','a'
    elif s[i] == '?':
        s[i] = s[len(s)-1-i]
    else:
        s[len(s)-1-i] = s[i]
print(''.join(s))