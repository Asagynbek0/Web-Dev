def power(a, n):
    result = 1
    i = 0
    while i < n:
        result *= a
        i += 1
    return result


a, n = input().split()
a = float(a)
n = int(n)

print(power(a, n))