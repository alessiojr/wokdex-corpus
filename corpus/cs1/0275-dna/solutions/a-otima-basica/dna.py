import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    while idx < len(input_data):
        K = int(input_data[idx])
        idx += 1
        if K == 0:
            break
            
        s1 = input_data[idx]
        idx += 1
        s2 = input_data[idx]
        idx += 1
        
        n = len(s1)
        m = len(s2)
        
        match = [[0] * (m + 1) for _ in range(n + 1)]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        f = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i-1] == s2[j-1]:
                    match[i][j] = match[i-1][j-1] + 1
                else:
                    match[i][j] = 0
                    
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                f[i][j] = 0
                
                if match[i][j] >= K:
                    f[i][j] = max(dp[i-K][j-K] + K, f[i-1][j-1] + 1)
                    dp[i][j] = max(dp[i][j], f[i][j])
                    
        print(dp[n][m])

if __name__ == '__main__':
    solve()
