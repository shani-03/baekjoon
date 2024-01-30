import sys

N = int(sys.stdin.readline())
card = set(map(int, sys.stdin.readline().split()))  

M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

result = [1 if i in card else 0 for i in num]  
print(*result, end=' ')
