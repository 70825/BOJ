a = 'qwertyasdfgzxcvb'
b = 'uiophjklnm'

s = [*input()]
l, r, etc = 0, 0, 0
for x in s:
    if x == ' ': etc += 1
    elif x.islower():
        if x in a: l += 1
        else: r += 1
    else:
        etc += 1
        if x.lower() in a: l += 1
        else: r += 1
p = abs(l-r)
if p >= etc:
    if l < r: l += etc
    else: r += etc
else:
    etc -= abs(l - r)
    if l < r: l += abs(l - r)
    else: r += abs(l - r)
    if etc % 2:
        l += etc//2 + 1
        r += etc//2
    else:
        l += etc//2
        r += etc//2
print(l, r)