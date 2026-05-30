import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return
    n = float(data[0])
    
    notes = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0]
    coins = [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]
    
    print("NOTAS:")
    for note in notes:
        qty = int(n / note)
        n -= qty * note
        print(f"{qty} nota(s) de R$ {note:.2f}")
        
    print("MOEDAS:")
    for coin in coins:
        qty = int(n / coin)
        n -= qty * coin
        print(f"{qty} moeda(s) de R$ {coin:.2f}")

if __name__ == '__main__':
    solve()
