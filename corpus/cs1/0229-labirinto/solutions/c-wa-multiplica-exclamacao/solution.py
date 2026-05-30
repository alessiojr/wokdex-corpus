import sys

def solve():
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
            
            if total > 0 and i < n:
                char_to_repeat = ' ' if line[i] == 'b' else line[i]
                
                # BUG: Multiplica a exclamacao ignorando a regra do problema
                if char_to_repeat == '!':
                    char_to_repeat = '\n'
                
                for _ in range(total):
                    maze_str += char_to_repeat
                    tem_saida = True
                i += 1
            elif i < n:
                i += 1
                
        sys.stdout.write(maze_str)
        if not tem_saida:
            sys.stdout.write("Entrada errada")
        sys.stdout.write("\n-------------\n")

if __name__ == "__main__":
    solve()
