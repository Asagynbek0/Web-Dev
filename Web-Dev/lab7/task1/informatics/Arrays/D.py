a = list(map(int, input().split()))

i = 1
while i < len(a):
    if a[i] > a[i - 1]:
        print(a[i], end=' ')
    i += 1