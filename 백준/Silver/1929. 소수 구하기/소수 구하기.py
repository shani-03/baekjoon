import math
M,N = map(int, input().split())
L = []
def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for i in range(M,N+1):
    if prime(i):
        L.append(i)
        

    
for n in L:
    print(n)