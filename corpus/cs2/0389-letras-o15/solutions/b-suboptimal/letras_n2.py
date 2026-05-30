import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    s = data[0]
    n = len(s)
    dp = [1] * n
    ans = 0 if n == 0 else 1
    for i in range(n):
        for j in range(i):
            if s[j] <= s[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        if dp[i] > ans:
            ans = dp[i]
    print(ans)

if __name__ == '__main__':
    solve()
