N = input()
l = len(N)
L = set()
for i in range(l):
    for j in range(i+1, l+1):
        res = N[i:j]
        L.add(res)
        
print(len(L))
 
    
    