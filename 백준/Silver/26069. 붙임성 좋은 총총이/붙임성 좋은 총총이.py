import sys
input = sys.stdin.readline
S = set()
S.add("ChongChong")
N = int(input())
for i in range(N):
    A,B = input().rstrip().split()
    if A in S:
        S.add(B)
    elif B in S:
        S.add(A)
print(len(S))
        
    