st = input()
to_digits = list(st)

cnt = 0

for c in to_digits:
    cnt += int(c)
    
print(cnt)