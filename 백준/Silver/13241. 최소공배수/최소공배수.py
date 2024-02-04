def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A, B = map(int, input().split())


gcd_value = gcd(A, B)


lcm = abs(A * B) // gcd_value

print(lcm)
