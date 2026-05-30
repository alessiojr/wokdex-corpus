import sys

def main():
    input_data = sys.stdin.read().split()
    soma = 0
    for token in input_data:
        val = int(token)
        if val == -1:
            break
        soma += val
    print(f"A soma dos valores eh: {soma}")

if __name__ == '__main__':
    main()
