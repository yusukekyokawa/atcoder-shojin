N = int(input())
A = list(map(int, input().split()))

cnt = 0
flag = True

while flag:
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] = A[i] / 2
        else:
            flag = False
            print(cnt)
            break
    cnt += 1
    