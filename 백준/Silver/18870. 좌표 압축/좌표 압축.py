import sys

N = int(sys.stdin.readline())


L = list(map(int, sys.stdin.readline().split()))

L_idx = sorted(list(set(L)))

D = {}

for i in range(len(L_idx)):
    D[L_idx[i]] = i

for j in L:
    print(D[j], end = ' ')


 



