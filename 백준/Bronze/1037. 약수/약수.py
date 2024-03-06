N = int(input())
L = list(map(int, input().split()))
L.sort()
min = L[0]
max = L[-1]

print(min*max)