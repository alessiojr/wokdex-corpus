import sys

for line in sys.stdin:
    n, f = map(int, line.split())
    if n == 0 and f == 0:
        break
    litros = (f * 50) / (n * 1000)
    print(f"{litros:.2f}")
