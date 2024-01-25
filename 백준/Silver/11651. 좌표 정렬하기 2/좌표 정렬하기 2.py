import sys
N = int(sys.stdin.readline())
L = []
for _ in range(N):
    [a,b] = map(int, sys.stdin.readline().split()) 
    L.append([a,b])

for i in range(len(L)):
    L[i][0], L[i][1] = L[i][1],L[i][0]

L.sort()

for j in L:
    print(j[1], j[0])
    
    