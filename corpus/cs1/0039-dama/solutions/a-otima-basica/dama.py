import sys

def solve():
    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        x1, y1, x2, y2 = map(int, parts)
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break
        
        if x1 == x2 and y1 == y2:
            print(0)
        elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            print(1)
        else:
            print(2)

if __name__ == '__main__':
    solve()
