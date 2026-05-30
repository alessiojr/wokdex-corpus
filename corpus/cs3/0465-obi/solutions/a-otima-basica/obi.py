import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    n = int(input_data[0])
    p = int(input_data[1])
    
    idx = 2
    pass_count = 0
    for _ in range(n):
        if idx + 1 >= len(input_data):
            break
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        if x + y >= p:
            pass_count += 1
        idx += 2
        
    print(pass_count)

if __name__ == '__main__':
    main()
