N = int(input())

A = list(map(int, input().split()))
A = sorted(A, reverse=True)

sum = 0
for i in range(N):
    if i % 2 ==0:
        sum += A[i]
    else:
        sum -= A[i]

print(sum)