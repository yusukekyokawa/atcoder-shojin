# https://atcoder.jp/contests/abc118/tasks/abc118_b
N, M = map(int,input().split()) 

exists = [0] * (M + 1)
for i  in range(N):
    tmp = list(map(int, input().split()))
    for j, val in enumerate(tmp):
        if j == 0:
            continue
        exists[val] += 1
ans = 0
for i in exists:
    if i == N:
        ans += 1

print(ans)