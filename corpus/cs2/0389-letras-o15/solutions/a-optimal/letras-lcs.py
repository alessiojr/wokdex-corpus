import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    s = data[0]
    n = len(s)
    
    # 1. Cria a cópia ordenada alfabeticamente
    s_sorted = "".join(sorted(s))
    
    # 2. Roda a DP do LCS otimizada em O(N) memória
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i-1] == s_sorted[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev = curr[:]
        
    print(curr[n])

if __name__ == '__main__':
    solve()
