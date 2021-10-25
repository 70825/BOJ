for _ in range(int(input())):
    n = int(input()) % 28
    if n > 15 : n = 30 - n
    elif n == 0: print('VV딸기V');continue
    val = '0' * (4 - len(bin(n)[2:])) + bin(n)[2:]
    ans = ['딸기' if val[i]=='1' else 'V' for i in range(len(val))]
    print(''.join(ans))