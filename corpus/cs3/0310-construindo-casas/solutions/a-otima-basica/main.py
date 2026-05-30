import sys
import math

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    while idx < len(input_data):
        a = int(input_data[idx])
        idx += 1
        if a == 0:
            break
        b = int(input_data[idx])
        c = int(input_data[idx+1])
        idx += 2
        
        area = a * b
        total = (area * 100) // c
        side = int(math.sqrt(total))
        print(side)

if __name__ == '__main__':
    main()
