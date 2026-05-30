import sys

def solve():
    # Reading all input at once into a list of strings
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    while idx < len(input_data):
        try:
            n_str = input_data[idx]
            n = int(n_str)
        except (ValueError, IndexError):
            break
        idx += 1
        
        if n == 0:
            break
        
        mary = 0
        john = 0
        # Process N results
        for _ in range(n):
            if idx >= len(input_data):
                break
            res = input_data[idx]
            if res == '0':
                mary += 1
            elif res == '1':
                john += 1
            idx += 1
            
        print(f"Mary won {mary} times and John won {john} times")

if __name__ == "__main__":
    solve()
