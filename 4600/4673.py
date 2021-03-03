#  b 리스트를 1~10000를 값으로 10000개를 저장해둠
b = [None] * 10001
for i in range(10001):
    b[i] = i

#  셀프넘버를 구함
def selfnumber(i):
    A = i
    total = 0
    B = A
    while B > 0:
        B, x = divmod(B,10)
        total += x
    total = A + total
    return total
# 이 셀프넘버가 나온 값을 c 리스트에 저장하고 b 리스트와 비교
c = [0] * 10001
for i in range(10001):
    if selfnumber(i+1) <= 10000:
        c[selfnumber(i+1)] = selfnumber(i+1)
for i in range(10001):
    if b[i] != c[i] and i != 0:
        print(b[i])