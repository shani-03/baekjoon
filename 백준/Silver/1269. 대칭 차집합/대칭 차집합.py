import sys
input = sys.stdin.readline
A, B = map(int, input().split())

As = set(map(int, input().split()))
Bs = set(map(int, input().split()))

print(len(As-Bs) + len(Bs-As))