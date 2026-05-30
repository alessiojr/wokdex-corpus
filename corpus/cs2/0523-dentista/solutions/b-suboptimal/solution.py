import sys

def solve():
    # O(N^2) Solution - Naive selection
    # For each step, we look through ALL intervals that haven't been picked
    # and pick the one that ends earliest among those that start after ultimo_fim.
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    consultas = []
    for i in range(N):
        idx = 1 + 2 * i
        inicio = int(input_data[idx])
        fim = int(input_data[idx + 1])
        # [inicio, fim, picked]
        consultas.append([inicio, fim, False])
    
    atendidas = 0
    ultimo_fim = 0
    
    # In each iteration of the outer while loop, we pick exactly one appointment
    while True:
        best_idx = -1
        min_fim = float('inf')
        
        # O(N) scan for each choice
        for i in range(N):
            if not consultas[i][2] and consultas[i][0] >= ultimo_fim:
                if consultas[i][1] < min_fim:
                    min_fim = consultas[i][1]
                    best_idx = i
        
        if best_idx == -1:
            # No possible next appointment found
            break
            
        consultas[best_idx][2] = True
        atendidas += 1
        ultimo_fim = min_fim
            
    # Output the result
    print(atendidas)

if __name__ == "__main__":
    solve()
