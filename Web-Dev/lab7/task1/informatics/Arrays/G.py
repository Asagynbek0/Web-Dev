a = list(map(int, input().split()))

max_val = a[0]
max_index = 0

i = 1
while i < len(a):
    if a[i] > max_val:
        max_val = a[i]
        max_index = i
    i += 1

print(max_val, max_index)