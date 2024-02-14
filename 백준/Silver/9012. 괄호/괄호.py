N = int(input())

for i in range(N):
    vps = list(input())
    
    sum = 0
    
    for j in range(len(vps)):
        if vps[j] == '(':
            sum += 1
        else:
            sum -= 1
        
        if sum < 0:
            print("NO")
            break
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")