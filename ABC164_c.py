# https://atcoder.jp/contests/abc164/tasks/abc164_c

N = int(input())

kind = set()
for i in range(N):
    s = input()
    kind.add(s)

print(len(list(kind)))