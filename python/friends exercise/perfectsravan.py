perfects = []
for n in range(101):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i

    if sum == n:
        perfects.append(n)

print(perfects)