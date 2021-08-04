def pm():
    global ans
    if flag: ans -= int(val)
    else: ans += int(val)

s = input()
flag = False
ans = 0
val = ''
for i in range(len(s)):
    if s[i] in ['+', '-']:
        pm()
        val = ''
        if s[i] == '-': flag = True
    else: val += s[i]
else: pm()
print(ans)