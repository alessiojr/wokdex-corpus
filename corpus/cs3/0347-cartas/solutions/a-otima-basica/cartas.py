import sys

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) >= 3:
        a = int(input_data[0])
        b = int(input_data[1])
        c = int(input_data[2])
        if a == b:
            print(c)
        elif a == c:
            print(b)
        else:
            print(a)

if __name__ == '__main__':
    main()
