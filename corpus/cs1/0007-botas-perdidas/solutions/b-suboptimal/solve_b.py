import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        while True:
            n = int(next(iterator))
            boots = []
            for _ in range(n):
                size = int(next(iterator))
                side = next(iterator)
                boots.append({'size': size, 'side': side, 'used': False})

            pairs = 0
            for i in range(n):
                if boots[i]['used']:
                    continue
                
                for j in range(i + 1, n):
                    if not boots[j]['used']:
                        if boots[i]['size'] == boots[j]['size'] and boots[i]['side'] != boots[j]['side']:
                            pairs += 1
                            boots[i]['used'] = True
                            boots[j]['used'] = True
                            break
            print(pairs)
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()
