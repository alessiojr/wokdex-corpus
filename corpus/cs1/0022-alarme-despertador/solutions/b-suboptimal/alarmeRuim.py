import sys

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            tokens = list(map(int, line.split()))
            if not tokens:
                continue
            h1, m1, h2, m2 = tokens[:4]
            if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
                break
            
            cnt = 0
            cur_h, cur_m = h1, m1
            # Ineficiente O(N) onde N é o número de minutos
            while cur_h != h2 or cur_m != m2:
                cnt += 1
                cur_m += 1
                if cur_m == 60:
                    cur_m = 0
                    cur_h += 1
                    if cur_h == 24:
                        cur_h = 0
            
            print(cnt)
        except Exception:
            pass

if __name__ == "__main__":
    main()
