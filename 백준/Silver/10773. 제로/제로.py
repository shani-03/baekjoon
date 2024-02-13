import sys
input = sys.stdin.readline

K = int(input())
L = []
for i in range(K):
    n = int(input())
    
    if n == 0:
        del L[-1]
    
    else:
        L.append(n)
        
print(sum(L))
        