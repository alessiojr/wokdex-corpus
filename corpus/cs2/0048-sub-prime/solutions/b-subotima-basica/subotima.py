import sys

def solve():
    """Solução bruta: simula rodadas de pagamento até estabilizar."""
    data = sys.stdin.read().split()
    idx = 0
    results = []
    
    while idx < len(data):
        B = int(data[idx]); N = int(data[idx+1])
        idx += 2
        if B == 0 and N == 0:
            break
        
        reservas = [0] * (B + 1)
        for i in range(1, B + 1):
            reservas[i] = int(data[idx]); idx += 1
        
        debentures = []
        for _ in range(N):
            D = int(data[idx]); C = int(data[idx+1]); V = int(data[idx+2])
            idx += 3
            debentures.append((D, C, V))
        
        # Simula: tenta pagar debêntures em rodadas
        caixa = list(reservas)
        pendentes = list(debentures)
        
        for _ in range(100):  # limite de rodadas
            novas_pendentes = []
            for D, C, V in pendentes:
                if caixa[D] >= V:
                    caixa[D] -= V
                    caixa[C] += V
                else:
                    novas_pendentes.append((D, C, V))
            if not novas_pendentes:
                break
            if len(novas_pendentes) == len(pendentes):
                break  # nenhum progresso
            pendentes = novas_pendentes
        
        results.append("S" if not pendentes else "N")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
