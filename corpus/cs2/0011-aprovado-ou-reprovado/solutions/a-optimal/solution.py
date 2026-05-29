import sys

def main():
    data = sys.stdin.read().split()
    if len(data) >= 2:
        a = float(data[0])
        b = float(data[1])
        media = (a + b) / 2.0
        
        if media >= 7.0:
            print("Aprovado")
        elif media >= 4.0:
            print("Recuperacao")
        else:
            print("Reprovado")

if __name__ == "__main__":
    main()
