dp_x = [0]*100
dp_y = [0]*100
dp_x[1] = 1
dp_y[0] = 1; dp_y[1] = 1

for i in range(2,100):
    dp_x[i] = dp_x[i-1] + dp_x[i-2]
    dp_y[i] = dp_y[i-1] + dp_y[i-2]

while 1:
    a, b, c = map(int,input().split())
    if a == b == c == 0: break
    if c >= 100: print(0); continue
    print(dp_x[c]*a + dp_y[c]*b)