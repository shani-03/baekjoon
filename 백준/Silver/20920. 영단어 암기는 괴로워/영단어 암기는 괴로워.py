import sys
input = sys.stdin.readline
N, M = map(int, input().split())
D = dict()


for _ in range(N):
    x = input().rstrip()
    
    if len(x) < M:
        continue
    
    if x not in D:
        D[x] = 1
    else:
        D[x] += 1

D = sorted(D.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in D:
    print(i[0])

