s = input()
b = input()
arr = [""]*len(s)
x, y = 0, 0
while x < len(s):
    arr[y] = s[x]
    if y >= len(b)-1 and s[x] == b[-1]:
        flag = True
        for i in range(len(b)):
            if b[-1-i] != arr[y-i]:
                flag = False; break
        if flag: y -= len(b)
    x += 1;y += 1
if y == 0:print('FRULA')
else: print(''.join(arr[:y]))