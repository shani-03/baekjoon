import sys
input = sys.stdin.readline
N = int(input())

L = list(map(int, input().split()))
LS = set(L)
D = {}

M = int(input())

I = list(map(int, input().split()))


for num in L:
    if num in D:
        D[num] += 1
    else:
        D[num] = 1
        
for j in I:
    print(D.get(j, 0), end=' ')



