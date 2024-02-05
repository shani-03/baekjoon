import math

A,B = map(int, input().split())
C,D = map(int, input().split())

Nu = A*D+B*C
De = B*D

GCD = math.gcd(Nu,De)

Nu //= GCD
De //= GCD
print(Nu, De)