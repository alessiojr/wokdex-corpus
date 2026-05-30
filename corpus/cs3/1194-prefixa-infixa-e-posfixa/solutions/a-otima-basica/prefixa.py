import sys

def solve_tree(pre, inf):
    if not pre:
        return ""
        
    root = pre[0]
    pos = inf.find(root)
    
    in_left = inf[:pos]
    in_right = inf[pos+1:]
    
    pre_left = pre[1:pos+1]
    pre_right = pre[pos+1:]
    
    return solve_tree(pre_left, in_left) + solve_tree(pre_right, in_right) + root

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    C = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(C):
        N = int(input_data[idx])
        S1 = input_data[idx+1]
        S2 = input_data[idx+2]
        idx += 3
        
        out.append(solve_tree(S1, S2))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
