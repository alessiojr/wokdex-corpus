import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    results = []
    
    while idx < len(data):
        N = int(data[idx]); P = int(data[idx+1])
        idx += 2
        if N == 0 and P == 0:
            break
        
        piles = []
        target_pile = -1
        target_row = -1
        
        for i in range(P):
            Q = int(data[idx]); idx += 1
            pile = []
            for j in range(Q):
                val = int(data[idx]); idx += 1
                pile.append(val)
                if val == 1:
                    target_pile = i
                    target_row = j
            piles.append(pile)
        
        above = len(piles[target_pile]) - target_row - 1
        
        # Custo pela esquerda
        cost_left = above
        for i in range(target_pile - 1, -1, -1):
            h = len(piles[i])
            if h > target_row:
                cost_left += h - target_row
            else:
                break
        
        # Custo pela direita
        cost_right = above
        for i in range(target_pile + 1, P):
            h = len(piles[i])
            if h > target_row:
                cost_right += h - target_row
            else:
                break
        
        results.append(str(min(cost_left, cost_right)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
