a = list(map(int, input().split()))

i = 0
count = 0

while i < len(a):
    if a[i] > 0:
        count += 1
    i += 1

print(count)