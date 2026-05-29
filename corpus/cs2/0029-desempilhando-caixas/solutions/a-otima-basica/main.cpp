#include <iostream>
#include <vector>
#include <algorithm> // Para std::lower_bound

int main() {
    // Otimização para operações de I/O em C++
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int N;
    std::cin >> N; // Lê o número de caixas

    std::vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> A[i]; // Lê os valores (pesos/tamanhos) das caixas
    }

    // dp[i] armazenará o menor valor final de uma subsequência crescente de comprimento i+1.
    // O vetor 'dp' será mantido em ordem estritamente crescente.
    std::vector<int> dp;

    for (int x : A) {
        // Encontra a posição onde 'x' deve ser inserido para manter 'dp' ordenado.
        // 'lower_bound' retorna um iterador para o primeiro elemento que não é menor que 'x' (i.e., >= x).
        auto it = std::lower_bound(dp.begin(), dp.end(), x);

        if (it == dp.end()) {
            // Se 'x' é maior que todos os elementos em 'dp',
            // ele estende a subsequência crescente mais longa encontrada.
            dp.push_back(x);
        } else {
            // Se 'x' é menor ou igual a 'dp[it]', ele pode substituir 'dp[it]'.
            // Isso significa que encontramos uma subsequência crescente de mesmo comprimento,
            // mas que termina com um valor menor (ou igual), o que é melhor
            // para permitir futuras extensões com outros números.
            *it = x;
        }
    }

    // O tamanho final do vetor 'dp' é o comprimento da Sequência Crescente Mais Longa (LIS).
    std::cout << dp.size() << std::endl;

    return 0;
}
