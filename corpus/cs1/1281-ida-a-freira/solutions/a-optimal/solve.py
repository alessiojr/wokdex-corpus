import sys

def solve():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
        
        for _ in range(n):
            m = int(sys.stdin.readline().strip())
            catalog = {}
            for _ in range(m):
                # Using rsplit to handle possible spaces in names if allowed 
                # (though spec says name then price)
                parts = sys.stdin.readline().strip().split()
                if len(parts) >= 2:
                    price = float(parts[-1])
                    name = " ".join(parts[:-1])
                    catalog[name] = price
            
            p = int(sys.stdin.readline().strip())
            total = 0.0
            for _ in range(p):
                parts = sys.stdin.readline().strip().split()
                if len(parts) >= 2:
                    qty = int(parts[-1])
                    name = " ".join(parts[:-1])
                    if name in catalog:
                        total += catalog[name] * qty
            
            print(f"R$ {total:.2f}")
    except EOFError:
        pass
    except ValueError:
        pass

if __name__ == "__main__":
    solve()
