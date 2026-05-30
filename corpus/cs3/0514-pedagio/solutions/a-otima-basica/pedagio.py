import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    L, D = int(input_data[0]), int(input_data[1])
    K, P = int(input_data[2]), int(input_data[3])
    
    cost = (L * K) + ((L // D) * P)
    print(cost)

if __name__ == '__main__':
    solve()
