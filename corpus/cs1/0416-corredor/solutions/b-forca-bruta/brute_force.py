import sys

def main():
    lines = sys.stdin.read().split()
    if len(lines) < 2: return
    n = int(lines[0])
    values = [int(x) for x in lines[1:n+1]]
    
    max_so_far = float('-inf')
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += values[j]
            if current_sum > max_so_far:
                max_so_far = current_sum
                
    print(max_so_far)

if __name__ == "__main__":
    main()
