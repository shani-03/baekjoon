N,K = map(int, input().split())

U = 1
D = 1
if K != 0: 
    for i in range(N-K+1,N+1):
        U *= i
    
    for j in range(1,K+1):
        D *= j
    
    print(U//D)
    
else:
    print(1)