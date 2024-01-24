import sys
N = int(sys.stdin.readline())
L = []
for i in range(N):
    [a, b] = map(int, sys.stdin.readline().split())
    L.append([a, b])
L.sort()
for i in L:
    print(i[0], i[1])