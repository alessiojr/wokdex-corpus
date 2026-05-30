import sys

def main():
    lines = sys.stdin.read().split()
    if len(lines) < 2: return
    n = int(lines[0])
    values = [int(x) for x in lines[1:n+1]]
    
    max_so_far = float('-inf')
    current_max = 0
    
    for v in values:
        current_max += v
        if current_max > max_so_far:
            max_so_far = current_max
        if current_max < 0:
            current_max = 0
            
    print(max_so_far)

if __name__ == "__main__":
    main()
