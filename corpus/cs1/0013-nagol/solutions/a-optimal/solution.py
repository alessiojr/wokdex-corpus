import sys

def solve():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            parts = line.split()
            if len(parts) < 4:
                break
            l, c, x, y = map(int, parts)
            index = x * c + y
            if index % 2 == 0:
                print("Direita")
            else:
                print("Esquerda")
        except (ValueError, EOFError):
            break

if __name__ == "__main__":
    solve()
