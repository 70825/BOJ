from itertools import product, permutations
dfd = __import__('collections').defaultdict(lambda: 0)

S1, S2, S3 = map(int, input().split())
S1 = [i for i in range(1, S1+1)]
S2 = [i for i in range(1, S2+1)]
S3 = [i for i in range(1, S3+1)]
for per in permutations([S1, S2, S3]):
    for x, y, z in product(*per):
        dfd[x+y+z] += 1
print(sorted(dfd.items(), key=lambda x: [-x[1], x[0]])[0][0])