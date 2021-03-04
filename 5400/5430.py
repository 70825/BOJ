from collections import deque
input = __import__('sys').stdin.readline
def iinp():return int(input())
def sinp():return input().strip()

for _ in range(iinp()):
    p = sinp()
    n = iinp()
    k = sinp()
    if k=='[]':x = deque([])
    else:x = deque([*map(int,k[1:len(k)-1].split(','))])
    rev = 0
    flag = True
    for i in range(len(p)):
        if p[i] == 'R':rev^=1
        else:
            try:
                if rev:x.pop()
                else:x.popleft()
            except IndexError: flag = False;break
    if not flag:print('error')
    else:
        print('[',end='')
        if rev:print(','.join(map(str,list(x)[::-1])),end='')
        else:print(','.join(map(str,list(x))),end='')
        print(']')
