input = __import__('sys').stdin.readline

n = int(input())
arr = [*map(int, input().split())]
dfd = __import__('collections').defaultdict(lambda : 0)
for i in range(n):
    dfd[arr[i]] += 1
s = input().strip()
flag = True
for i in range(n):
    if s[i] == ' ' and dfd[0]: dfd[0] -= 1;continue
    elif 1 <= (ord(s[i]) - ord('A') + 1) <= 26 and dfd[(ord(s[i]) - ord('A') + 1)]: dfd[(ord(s[i]) - ord('A') + 1)] -= 1;continue
    elif 27 <= (ord(s[i]) - ord('a') + 27) <= 52 and dfd[(ord(s[i]) - ord('a') + 27)]: dfd[(ord(s[i]) - ord('a') + 27)] -= 1; continue
    flag = False
if flag: print('y')
else: print('n')