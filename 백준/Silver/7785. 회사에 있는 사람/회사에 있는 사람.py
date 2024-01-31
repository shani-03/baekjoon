import sys
input = sys.stdin.readline

N = int(input())
L = set()

for _ in range(N):
    name, log = input().strip().split()
    
    if log == 'enter':
        L.add(name)
    else:  
        L.discard(name)

result = sorted(L, reverse=True)

for name in result:
    print(name)