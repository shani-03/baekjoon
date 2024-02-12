import sys
input = sys.stdin.readline

N = int(input())
S = []
for i in range(N):
    a = input().split()
    if a[0] == '1':
        S.append(a[1])
    
    elif a[0] == '2':
        if S:
            print(S.pop())
        else:
            print(-1)
    elif a[0] == '3':
        print(len(S))
    
    elif a[0] == '4':
        if S:
            print(0)
        else:
            print(1)
            
    elif a[0] == '5':
        if S:
            print(S[-1])
            
        else:
            print(-1)