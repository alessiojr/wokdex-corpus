import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    line_idx = 0
    num_cases = int(input_data[line_idx])
    line_idx += 1
    
    for _ in range(num_cases):
        num_products = int(input_data[line_idx])
        line_idx += 1
        
        prices = {}
        for _ in range(num_products):
            parts = input_data[line_idx].split()
            prices[parts[0]] = float(parts[1])
            line_idx += 1
            
        num_items = int(input_data[line_idx])
        line_idx += 1
        
        total = 0.0
        # FLAWED LOGIC: Store items in a dictionary, overwriting quantities
        # instead of accumulating (e.g., if 'apple 2' and 'apple 3' appear, 
        # it will only count 'apple 3').
        shopping_list = {}
        for _ in range(num_items):
            parts = input_data[line_idx].split()
            name = parts[0]
            qty = int(parts[1])
            shopping_list[name] = qty # Overwrite!
            line_idx += 1
            
        # Total calculation from the flawed list
        for name, qty in shopping_list.items():
            if name in prices:
                total += prices[name] * qty
                
        print(f"R$ {total:.2f}")

if __name__ == "__main__":
    solve()
