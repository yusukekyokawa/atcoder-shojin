S = input()

ans = 0

while len(S) > 0:
    if S[0] == '0':
        if len(S) > 1 and S[1] =='0':
            S = S[1:]

    S = S[1:]
    ans += 1

print(ans)