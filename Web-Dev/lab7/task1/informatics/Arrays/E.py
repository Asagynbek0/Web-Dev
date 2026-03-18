a = list(map(int, input().split()))

i = 0
while i < len(a) - 1:
    if a[i] * a[i + 1] > 0:
        print(a[i], a[i + 1])
        break
    i += 1