N, Y = map(int, input().split())

x, y, z = -1, -1, -1

for i in range(N + 1):
    for j in range(N + 1):
        k = N - (i + j)
        if k>=0 and ((10000 * i + 5000 * j + 1000 * k) == Y):
            x, y, z = i, j, k
        else:
            continue


print(x, y, z)
