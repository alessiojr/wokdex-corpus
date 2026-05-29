import sys

def solve():
    # Mapeamento: 0: N, 1: L, 2: S, 3: O
    dirs = ['N', 'L', 'S', 'O']
    
    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        try:
            line = lines[i].strip()
            if not line:
                i += 1
                continue
                
            N = int(line)
            if N == 0:
                break
            
            i += 1
            if i >= len(lines):
                break
                
            commands = lines[i].strip()
            i += 1
            
            current_dir = 0 # Norte
            
            for cmd in commands:
                if cmd == 'D':
                    current_dir = (current_dir + 1) % 4
                elif cmd == 'E':
                    current_dir = (current_dir - 1 + 4) % 4
            
            print(dirs[current_dir])
            
        except ValueError:
            i += 1
            continue

if __name__ == "__main__":
    solve()
