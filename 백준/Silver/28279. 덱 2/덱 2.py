from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
myque = deque([])

for i in range(N):
    cmd = list(map(int,input().split()))
    a = cmd[0]
    
    if a == 1:
        myque.appendleft(cmd[1])
    elif a == 2:
        myque.append(cmd[1])
    elif a == 3:
        if len(myque) == 0:
            print(-1)
        else:
            print(myque.popleft())
    elif a == 4:
        if len(myque) == 0:
            print(-1)
        else:
            print(myque.pop())
    elif a == 5:
        print(len(myque))
    elif a == 6:
        if len(myque) == 0:
            print(1)
        else:
            print(0)
    elif a == 7:
        if len(myque) == 0:
            print(-1)
        else:
            print(myque[0])
    elif a == 8:
        if len(myque) == 0:
            print(-1)
        else:
            print(myque[-1])
        
       
        
        