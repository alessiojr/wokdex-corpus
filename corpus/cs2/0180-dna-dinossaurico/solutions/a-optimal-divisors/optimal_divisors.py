import sys

def solve():
    s = sys.stdin.read().split()
    if not s:
        return
    s = s[0]
    n = len(s)
    
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    divisors.sort()
    
    for k in divisors:
        d = n // k
        valid = True
        for i in range(d // 2):
            if s[i * k : (i + 1) * k] != s[(d - 1 - i) * k : (d - i) * k]:
                valid = False
                break
        if valid:
            print(d)
            return

if __name__ == '__main__':
    solve()
