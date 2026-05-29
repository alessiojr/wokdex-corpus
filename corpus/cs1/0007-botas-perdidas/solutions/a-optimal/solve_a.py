import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        while True:
            n = int(next(iterator))
            left = [0] * 65
            right = [0] * 65

            for _ in range(n):
                size = int(next(iterator))
                side = next(iterator)
                if side == 'E':
                    left[size] += 1
                else:
                    right[size] += 1

            pairs = 0
            for i in range(30, 61):
                pairs += min(left[i], right[i])
            print(pairs)
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()
