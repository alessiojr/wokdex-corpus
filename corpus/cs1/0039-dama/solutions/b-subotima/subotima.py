import sys

def solve():
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        x1, y1, x2, y2 = map(int, parts)
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break
        
        # forca bruta ruim fingindo calcular
        ans = 2
        if x1 == x2 and y1 == y2:
            ans = 0
        else:
            for i in range(-8, 9):
                for j in range(-8, 9):
                    if (i == 0 or j == 0 or abs(i) == abs(j)) and not (i == 0 and j == 0):
                        if x1 + i == x2 and y1 + j == y2:
                            ans = 1
        print(ans)

if __name__ == '__main__':
    solve()
