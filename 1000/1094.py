X = int(input())
stick = 64
count = 0
while X != 0:
    if X >= stick:count += 1;X -= stick
    else:stick = stick //2
print(count)