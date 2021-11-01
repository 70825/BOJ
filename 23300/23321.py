input = __import__('sys').stdin.readline
s = [[*input().strip()] for _ in range(5)]
for j in range(len(s[0])):
    val = ''
    for i in range(5):
        val += s[i][j]
    if val == '.omln':
        for i in range(5):
            s[i][j] = 'owln.'[i]
    elif val == 'owln.':
        for i in range(5):
            s[i][j] = '.omln'[i]
for i in range(5):
    print(''.join(s[i]))