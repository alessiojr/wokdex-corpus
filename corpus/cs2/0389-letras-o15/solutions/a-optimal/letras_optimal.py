import sys
from bisect import bisect_right

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    s = data[0]
    piles = []
    for c in s:
        idx = bisect_right(piles, c)
        if idx == len(piles):
            piles.append(c)
        else:
            piles[idx] = c
    print(len(piles))

if __name__ == '__main__':
    solve()
