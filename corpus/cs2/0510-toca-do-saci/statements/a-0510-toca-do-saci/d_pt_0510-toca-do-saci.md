# Toca do Saci — Tutorial

A forma mais limpa de construir este código é criar uma matriz 2D levemente maior (adicionando "bordas de zero") que o tamanho lido. Na nossa solução usamos `vector<vector<int>>` de dimensão $(N+2) \times (M+2)$, sendo que as linhas e colunas `0` e `N+1`/`M+1` ficam zeradas naturalmente. Assim, o algoritmo de movimento jamais sofrerá *Segfault* (falha de segmentação ao acessar índices fora dos limites), pois baterá no valor $0$ da barreira inativa.

## Passo a Passo na Simulação de Caminho

### 1. Declaração com Bordas de Proteção
```cpp
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

vector<vector<int>> grid(n + 2, vector<int>(m + 2, 0));
int x = -1, y = -1;

for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++) {
        cin >> grid[i][j];
        if (grid[i][j] == 3) { x = i; y = j; } // Guarda a posição da saída
    }
```

### 2. Caminhar em Loop até a Emília
Iniciamos as coordenadas $x$ e $y$ onde está o número `3` (saída). O contador começa em 1, pois estamos pisando nessa célula.
Enquanto `grid[x][y]` não for `2` (a Emília), continuamos andando.

```cpp
int passos = 1;

while (grid[x][y] != 2) {
    // Destrói o caminho para trás (pão de migalhas destrutivo)
    grid[x][y] = 0; 
    
    // Tenta as 4 direções
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        
        // Se a próxima sala for válida (1, 2 ou 3), ande!
        if (grid[nx][ny] > 0) {
            passos++;
            x = nx;
            y = ny;
            break; // Já achou o próximo bloco do corredor
        }
    }
}

cout << passos << endl;
```

### 3. Por que funciona quando a Emília está no meio?
No exemplo 3 da OBI, a Emília (valor `2`) está no *meio* do corredor, não no final. Mesmo assim o algoritmo funciona perfeitamente! Isso porque começamos da saída (`3`) e destruímos cada célula ao sair dela. Como o enunciado garante que o caminho é único e sem ramificações, o algoritmo segue a única direção possível até encontrar o `2`, contabilizando todas as salas no caminho — que é exatamente o que Emília faria voltando.

A complexidade de tempo é $O(\text{tamanho do caminho})$, muito mais rápida que uma BFS completa!

