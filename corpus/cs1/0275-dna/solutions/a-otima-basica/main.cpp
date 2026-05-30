#include <iostream>
#include <string>
#include <vector>

int main() {
    // Otimização para entrada/saída em C++
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::string dna1, dna2;
    
    // Leitura das duas sequências de DNA
    std::cin >> dna1 >> dna2;

    int mutations = 0;
    
    // As sequências de DNA têm sempre o mesmo comprimento.
    // Itera por cada posição para comparar os nucleotídeos.
    for (size_t i = 0; i < dna1.length(); ++i) {
        // Se os caracteres na posição 'i' forem diferentes, incrementa o contador.
        if (dna1[i] != dna2[i]) {
            mutations++;
        }
    }

    // Imprime o número total de mutações (diferenças)
    std::cout << mutations << std::endl;

    return 0;
}
