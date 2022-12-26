# https://atcoder.jp/contests/abc154/tasks/abc154_c
N = int(input())
A = list(map(int, input().split()))

if len(set(A)) != len(A):
    print("NO")
else:
    print("YES")