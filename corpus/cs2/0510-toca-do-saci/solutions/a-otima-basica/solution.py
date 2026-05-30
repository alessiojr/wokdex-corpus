import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Create grid with padding of 0s
    grid = [[0] * (m + 2) for _ in range(n + 2)]
    
    idx = 2
    x, y = -1, -1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            val = int(input_data[idx])
            idx += 1
            grid[i][j] = val
            if val == 3:
                x, y = i, j
                
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    passos = 1
    while grid[x][y] != 2:
        grid[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if grid[nx][ny] > 0:
                passos += 1
                x, y = nx, ny
                break
                
    print(passos)

if __name__ == '__main__':
    main()
