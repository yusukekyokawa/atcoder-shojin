
def rec(n):
    sum = 0
    while (n > 0):
        sum += n % 10
        n = n//10
    return sum
    
if __name__ == "__main__":
    N, A, B = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        sum = rec(i)
        if (sum >= A) and (sum <=B):
            ans += i
    print(ans)
