val = [*map(int, [*input()])]
arr = sorted([[*map(int, [*input()])] for _ in range(int(input()))], key=lambda x:[-(((val[0]-x[0])**2 + (val[1]-x[1])**2 + (val[2]-x[2])**2 + (val[3]-x[3])**2)
    * ((val[4]-x[4])**2 + (val[5]-x[5])**2) * ((val[6]-x[6])**2 + (val[7]-x[7])**2)), x])
print(''.join(map(str,arr[0])))