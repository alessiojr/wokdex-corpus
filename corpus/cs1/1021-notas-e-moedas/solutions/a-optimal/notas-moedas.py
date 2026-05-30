import sys

def solve():
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        
        for val_str in input_data:
            n = float(val_str)
            
            # Convert to centavos to avoid precision issues
            # We use round() or int(n * 100 + 0.5) to handle float imprecision
            centavos = int(n * 100 + 0.5)

            print("NOTAS:")
            notas = [10000, 5000, 2000, 1000, 500, 200]
            for nota in notas:
                qtd = centavos // nota
                centavos %= nota
                print(f"{qtd} nota(s) de R$ {nota//100}.00")

            print("MOEDAS:")
            moedas = [100, 50, 25, 10, 5, 1]
            for moeda in moedas:
                qtd = centavos // moeda
                centavos %= moeda
                print(f"{qtd} moeda(s) de R$ {moeda/100:.2f}")

    except EOFError:
        pass

if __name__ == "__main__":
    solve()
