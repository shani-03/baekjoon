import sys
input = sys.stdin.readline

N = int(input())
data = []
sum = 0
count = dict()
for i in range(N):
    x = int(input())
    data.append(x)
    sum += x
    
    if x not in count:
        count[x] = 1
    else: 
        count[x] += 1
        
data.sort()
# 평균
print(round(sum/N))

#중앙값
print(data[N//2])

#최빈값
freq = max(count.values())
numbers = []
for key, value in count.items():
    if value == freq:
        numbers.append(key)

if len(numbers) == 1:
    print(numbers[0])
else:
    print(sorted(numbers)[1])

# 범위
print(data[-1] - data[0])
