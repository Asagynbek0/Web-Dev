a = list(map(int, input().split()))

i = 1
count = 0

while i < len(a) - 1:
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        count += 1
    i += 1

print(count)