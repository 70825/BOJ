k = [*map(int, [*input()])]
if len(k) == 1: print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!'); exit()
val = k[1] - k[0]
for i in range(1, len(k)-1):
    if k[i+1] - k[i] != val:
        print('흥칫뿡!! <(￣ ﹌ ￣)>')
        exit()
print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')