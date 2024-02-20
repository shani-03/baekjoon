N,K = map(int, input().split())

que = [i for i in range(1, N+1)]

id = 0
result = []

while que:
    id += K - 1
    if id >= len(que):
        id %= len(que)
    result.append(str(que.pop(id)))  

print("<", ", ".join(result), ">", sep="")