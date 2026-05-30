import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    n_str = data[0]
    
    # multiply by 100 and round to nearest int to avoid float imprecision
    cents = round(float(n_str) * 100)
    
    notes = [10000, 5000, 2000, 1000, 500, 200]
    coins = [100, 50, 25, 10, 5, 1]
    
    print("NOTAS:")
    for note in notes:
        qty = cents // note
        cents %= note
        print(f"{qty} nota(s) de R$ {note // 100}.00")
        
    print("MOEDAS:")
    for coin in coins:
        qty = cents // coin
        cents %= coin
        print(f"{qty} moeda(s) de R$ {coin // 100}.{coin % 100:02d}")

if __name__ == '__main__':
    solve()
