import sys

N, M = map(int, sys.stdin.readline().split())

nlist = {sys.stdin.readline().strip() for _ in range(N)}
mlist = [sys.stdin.readline().strip() for _ in range(M)]

print(sum(1 for i in mlist if i in nlist))
