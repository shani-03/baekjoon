from collections import deque

mydeque = deque([])

N = int(input())

mydeque.extend(range(1, N+1))

while len(mydeque) != 1:
    mydeque.popleft()
    mydeque.append(mydeque.popleft())

print(mydeque[0])
