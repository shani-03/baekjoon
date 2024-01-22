n = str(input())
L = []
S = ''
for i in range(len(n)):
    L.append(n[i])
    
L.sort(reverse=True)

for i in range(len(L)):
    S += str(L[i]) 
print(int(S))
    