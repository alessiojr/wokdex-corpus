import sys

def solve():
    """Solução bruta: para cada lado, testa removendo caixa a caixa, uma por vez,
    simulando o processo real ao invés de calcular diretamente."""
    data = sys.stdin.read().split()
    idx = 0
    results = []
    
    while idx < len(data):
        N = int(data[idx]); P = int(data[idx+1])
        idx += 2
        if N == 0 and P == 0:
            break
        
        piles = []
        for i in range(P):
            Q = int(data[idx]); idx += 1
            pile = []
            for j in range(Q):
                pile.append(int(data[idx])); idx += 1
            piles.append(pile)
        
        # Tenta pela esquerda: simula removendo caixas até a caixa 1 ficar acessível
        def simulate(piles_copy):
            count = 0
            while True:
                # Encontra caixa 1
                tp, tr = -1, -1
                for i, p in enumerate(piles_copy):
                    for j, v in enumerate(p):
                        if v == 1:
                            tp, tr = i, j
                            break
                    if tp >= 0:
                        break
                
                # Caixa 1 está no topo?
                if tr == len(piles_copy[tp]) - 1:
                    # Tem lado livre?
                    left_free = (tp == 0) or (len(piles_copy[tp-1]) < len(piles_copy[tp]))
                    right_free = (tp == len(piles_copy)-1) or (len(piles_copy[tp+1]) < len(piles_copy[tp]))
                    if left_free or right_free:
                        return count
                
                # Remove alguma caixa que está bloqueando (guloso: qualquer uma removível)
                removed = False
                # Primeiro tenta remover de cima da caixa 1
                if tr < len(piles_copy[tp]) - 1:
                    top_idx = len(piles_copy[tp]) - 1
                    left_ok = (tp == 0) or (len(piles_copy[tp-1]) < len(piles_copy[tp]))
                    right_ok = (tp == len(piles_copy)-1) or (len(piles_copy[tp+1]) < len(piles_copy[tp]))
                    if left_ok or right_ok:
                        piles_copy[tp].pop()
                        count += 1
                        removed = True
                
                if not removed:
                    # Remove das pilhas vizinhas que bloqueiam
                    for i in range(len(piles_copy)):
                        if i == tp:
                            continue
                        if len(piles_copy[i]) > 0:
                            top_h = len(piles_copy[i])
                            left_ok = (i == 0) or (len(piles_copy[i-1]) < top_h)
                            right_ok = (i == len(piles_copy)-1) or (len(piles_copy[i+1]) < top_h)
                            if left_ok or right_ok:
                                piles_copy[i].pop()
                                count += 1
                                removed = True
                                break
                
                if not removed:
                    return -1  # impossível (não deveria acontecer)
        
        import copy
        results.append(str(simulate(copy.deepcopy(piles))))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
