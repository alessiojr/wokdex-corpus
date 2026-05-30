import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n+1]]
    
    max_so_far = 0
    max_ending_here = 0
    min_so_far = 0
    min_ending_here = 0
    total_sum = 0
    
    for x in arr:
        total_sum += x
        
        max_ending_here += x
        if max_ending_here < 0:
            max_ending_here = 0
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            
        min_ending_here += x
        if min_ending_here > 0:
            min_ending_here = 0
        if min_ending_here < min_so_far:
            min_so_far = min_ending_here
            
    if total_sum == min_so_far:
        print(max_so_far)
    else:
        print(max(max_so_far, total_sum - min_so_far))

if __name__ == '__main__':
    solve()
