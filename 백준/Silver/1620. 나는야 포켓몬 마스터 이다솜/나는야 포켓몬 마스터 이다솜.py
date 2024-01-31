import sys
input = sys.stdin.readline
N,M = map(int,input().split())
book_name = {}
book_num = {}
for i in range(N):
    name = input().rstrip()
    book_name[name] = i+1
    book_num[i+1] = name
    
for j in range(M):
    Q = input().rstrip()
    try:
        Q = int(Q)  
        print(book_num[Q])
    except ValueError:
        print(book_name[Q])
    
    