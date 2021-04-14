s = input()
lsum = 0
rsum = 0
for i in range(len(s)//2):
    lsum += int(s[i])
for i in range(len(s)//2,len(s)):
    rsum += int(s[i])
if lsum == rsum:print('LUCKY')
else:print('READY')