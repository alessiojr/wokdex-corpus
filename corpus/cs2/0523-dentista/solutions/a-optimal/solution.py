import sys

def solve():
    # Performance hint: Read entire stdin at once for faster processing
    all_input = sys.stdin.read().split()
    if not all_input:
        return
    
    # Input structure: N, then N pairs of (X, Y)
    # Be careful with large inputs.
    N = int(all_input[0])
    consultas = []
    
    # all_input[1:] contains the flattened pairs
    for i in range(N):
        idx = 1 + 2 * i
        inicio = int(all_input[idx])
        fim = int(all_input[idx + 1])
        consultas.append((inicio, fim))
    
    # Sort by finishing time (greedy criterion)
    # If finishing times are equal, sorting by starting time can be done but it's not strictly necessary.
    consultas.sort(key=lambda x: x[1])
    
    atendidas = 0
    ultimo_fim = 0
    
    for inicio, fim in consultas:
        if inicio >= ultimo_fim:
            atendidas += 1
            ultimo_fim = fim
            
    print(atendidas)

if __name__ == "__main__":
    solve()
