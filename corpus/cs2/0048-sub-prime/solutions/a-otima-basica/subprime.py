import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    results = []
    
    while idx < len(data):
        B = int(data[idx]); N = int(data[idx+1])
        idx += 2
        if B == 0 and N == 0:
            break
        
        saldo = [0] * (B + 1)
        for i in range(1, B + 1):
            saldo[i] = int(data[idx]); idx += 1
        
        for _ in range(N):
            D = int(data[idx]); C = int(data[idx+1]); V = int(data[idx+2])
            idx += 3
            saldo[D] -= V
            saldo[C] += V
        
        ok = all(saldo[i] >= 0 for i in range(1, B + 1))
        results.append("S" if ok else "N")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
