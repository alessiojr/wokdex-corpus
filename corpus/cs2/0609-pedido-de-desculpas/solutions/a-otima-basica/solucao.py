import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    teste = 1
    
    while idx < len(input_data):
        C = int(input_data[idx])
        F = int(input_data[idx+1])
        idx += 2
        
        if C == 0 and F == 0:
            break
            
        dp = [0] * (C + 1)
        
        for _ in range(F):
            N = int(input_data[idx])
            D = int(input_data[idx+1])
            idx += 2
            
            for j in range(C, N - 1, -1):
                if dp[j - N] + D > dp[j]:
                    dp[j] = dp[j - N] + D
                    
        print(f"Teste {teste}")
        print(dp[C])
        print()
        teste += 1

if __name__ == '__main__':
    solve()
