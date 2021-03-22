gugu = []
for i in range(2, 10):
    gu = []
    for j in range(1, 10):
        if not ((i * j) % 3 == 0 or (i * j) % 7 == 0):
            gu.append(i * j)
    gugu.append(gu)

print(gugu)
