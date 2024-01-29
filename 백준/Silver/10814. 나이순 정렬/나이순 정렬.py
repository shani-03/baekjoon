import sys

N = int(sys.stdin.readline())
L = []
id = 0

for i in range(N):
    id += 1
    age, name = map(str, sys.stdin.readline().split())
    L.append([int(age), name, id])

L.sort(key = lambda x: (x[0], x[2]))

for j in L:
    print(j[0], j[1])
