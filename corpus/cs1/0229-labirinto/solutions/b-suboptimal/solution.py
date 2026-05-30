import sys

def solve():
    # Sub-optimal solution with O(N^2) behavior due to repeated string concatenation
    # and inefficient parsing logic. Matches construtor.c logic.
    input_data = sys.stdin.read()
    lines = input_data.splitlines()
    
    for line in lines:
        if not line:
            continue
            
        maze_str = "" 
        i = 0
        n = len(line)
        tem_saida = False
        
        while i < n:
            if line[i] == '!':
                maze_str += '\n'
                tem_saida = True
                i += 1
                continue
            
            total = 0
            while i < n and '0' <= line[i] <= '9':
                total += int(line[i])
                i += 1
            
            if i < n and line[i] == '!':
                maze_str += '\n'
                tem_saida = True
                i += 1
            elif total > 0 and i < n:
                char_to_repeat = ' ' if line[i] == 'b' else line[i]
                
                # Inefficiently adding character by character
                for _ in range(total):
                    maze_str += char_to_repeat
                    tem_saida = True
                i += 1
            else:
                i += 1
                
        # Correct output order: maze content then error if needed
        sys.stdout.write(maze_str)
        if not tem_saida:
            sys.stdout.write("Entrada errada")
        sys.stdout.write("\n-------------\n")

if __name__ == "__main__":
    solve()
