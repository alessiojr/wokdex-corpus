def main():
    try:
        # Reading all input at once allows handling newlines flexibly
        import sys
        input_data = sys.stdin.read().split()
        
        if not input_data:
            return

        op = input_data[0]
        a = float(input_data[1])
        b = float(input_data[2])

        if op == 'M':
            res = a * b
        elif op == 'D':
            res = a / b
        
        print(f"{res:.2f}")
    except Exception:
        pass

if __name__ == "__main__":
    main()
