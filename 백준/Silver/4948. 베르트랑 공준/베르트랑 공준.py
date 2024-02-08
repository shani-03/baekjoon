import sys
input = sys.stdin.readline
num = 123456 * 2 + 1
numL = [1] * num

for i in range(2, int(num**0.5) + 1):
    if numL[i] == 1:
        for j in range(i * i, num, i):
            numL[j] = 0

while True:
    N = int(input())
    
    if N == 0:
        break
    
    prime = 0
    for i in range(N + 1, 2 * N + 1):
        prime += numL[i]
    
    print(prime)
