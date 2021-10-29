s = input()
space = int(input())
count = [*map(int, input().split())]

if s[0].isupper() and count[ord(s[0]) - ord('A')]: count[ord(s[0]) - ord('A')] -= 1
elif s[0].islower() and count[ord(s[0]) - ord('a')]: count[ord(s[0]) - ord('a')] -= 1
else: print(-1); exit()

prev = s[0]
for i in range(1, len(s)):
    if ord(prev) == ord(s[i]): continue
    if s[i] == ' ':
        if space: space -= 1; prev = s[i]; continue
        else: print(-1); exit()
    if s[i].isupper() and count[ord(s[i]) - ord('A')]:
        count[ord(s[i]) - ord('A')] -= 1
    elif s[i].islower() and count[ord(s[i]) - ord('a')]:
        count[ord(s[i]) - ord('a')] -= 1
    else: print(-1); exit()
    prev = s[i]

z = [*s.upper().split()]
for i in range(len(z)): z[i] = z[i][0]

if count[ord(z[0]) - ord('A')]: count[ord(z[0]) - ord('A')] -= 1
else: print(-1); exit()

prev = z[0]
for i in range(1, len(z)):
    if ord(prev) == ord(z[i]): continue
    elif count[ord(z[i]) - ord('A')]: count[ord(z[i]) - ord('A')] -= 1
    else: print(-1); exit()

print(''.join(z))