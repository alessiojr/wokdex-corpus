import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    L, D = int(input_data[0]), int(input_data[1])
    K, P = int(input_data[2]), int(input_data[3])
    
    cost = 0
    # Simulate each km
    for km in range(1, L + 1):
        cost += K
        if km % D == 0:
            cost += P
            
    print(cost)

if __name__ == '__main__':
    solve()
