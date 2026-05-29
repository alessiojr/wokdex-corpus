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
            
            # Sub-optimal simulation logic O(L*C)
            # This will TLE for large inputs (e.g., L, C = 10^5)
            index = 0
            found = False
            for i in range(l):
                for j in range(c):
                    if i == x and j == y:
                        found = True
                        break
                    index += 1
                if found:
                    break
            
            if index % 2 == 0:
                print("Direita")
            else:
                print("Esquerda")
        except (ValueError, EOFError):
            break

if __name__ == "__main__":
    solve()
