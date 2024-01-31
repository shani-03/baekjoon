import sys
count = int(sys.stdin.readline())
my_list = [int(sys.stdin.readline()) for _ in range(count)]
for i in sorted(my_list):
    print(i)