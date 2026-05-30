import sys

def solve():
    for line in sys.stdin:
        # Note: construtor.c used scanf(" %[^\n]", labirinto)
        # which skips leading whitespace.
        line = line.strip('\r\n')
        if not line:
            continue
            
        i = 0
        n = len(line)
        tem_saida = False
        
        while i < n:
            if line[i] == '!':
                sys.stdout.write('\n')
                tem_saida = True
                i += 1
                continue
            
            total = 0
            while i < n and '0' <= line[i] <= '9':
                total += int(line[i])
                i += 1
            
            if i < n and line[i] == '!':
                sys.stdout.write('\n')
                tem_saida = True
                i += 1
            elif total > 0 and i < n:
                atual = line[i]
                if atual == 'b': atual = ' '
                sys.stdout.write(atual * total)
                tem_saida = True
                i += 1
            elif i < n:
                i += 1
                
        if not tem_saida:
            sys.stdout.write("Entrada errada")
        sys.stdout.write("\n-------------\n")

if __name__ == "__main__":
    solve()
