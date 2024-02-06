import math

N = int(input())

def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for i in range(N):
    A = int(input())
    while True:
        if prime(A):
            print(A)
            break
        else:
            A += 1
