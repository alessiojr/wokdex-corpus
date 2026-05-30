import sys

def solve():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
        
        for _ in range(n):
            m = int(sys.stdin.readline().strip())
            catalog = []
            for _ in range(m):
                parts = sys.stdin.readline().strip().split()
                if len(parts) >= 2:
                    price = float(parts[-1])
                    name = " ".join(parts[:-1])
                    catalog.append((name, price))
            
            p = int(sys.stdin.readline().strip())
            total = 0.0
            for _ in range(p):
                parts = sys.stdin.readline().strip().split()
                if len(parts) >= 2:
                    qty = int(parts[-1])
                    name = " ".join(parts[:-1])
                    
                    # Sub-optimal: Linear search in catalog
                    item_price = 0.0
                    for cat_name, cat_price in catalog:
                        if cat_name == name:
                            item_price = cat_price
                            break
                    
                    total += item_price * qty
            
            print(f"R$ {total:.2f}")
    except EOFError:
        pass
    except ValueError:
        pass

if __name__ == "__main__":
    solve()
