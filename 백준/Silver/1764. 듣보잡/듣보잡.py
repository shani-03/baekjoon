import sys
input = sys.stdin.readline

N, M = map(int, input().split())

H = set()
S = set()
L = []


for i in range(N):
    H.add(input().rstrip())

for j in range(M):
    S.add(input().rstrip())


common_elements = H & S


L.extend(common_elements)


L.sort()


print(len(L))
for m in L:
    print(m)
