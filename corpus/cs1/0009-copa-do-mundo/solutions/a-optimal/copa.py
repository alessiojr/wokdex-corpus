import sys

def main():
    # Read all input at once and split by whitespace for robustness
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    while idx < len(data):
        try:
            T = int(data[idx])
            N = int(data[idx+1])
        except (ValueError, IndexError):
            break
            
        idx += 2
        
        if T == 0 and N == 0:
            break
            
        total_points = 0
        for _ in range(T):
            # Each team has a name and points
            # nome = data[idx] # Skip name
            try:
                pontos = int(data[idx+1])
                total_points += pontos
            except (ValueError, IndexError):
                pass
            idx += 2
            
        # Formula: Each draw reduces the total points from 3*N by 1
        # Sum of points = 3*(N - draws) + 2*draws = 3*N - 3*draws + 2*draws = 3*N - draws
        # Therefore: draws = 3*N - Sum of points
        empates = 3 * N - total_points
        print(empates)

if __name__ == "__main__":
    main()