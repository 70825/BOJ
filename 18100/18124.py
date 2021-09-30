n = int(input())
expo = 0
while 2**expo < n: expo+=1
val = 2 ** expo
print(val - (val - n) // 2 - 1)