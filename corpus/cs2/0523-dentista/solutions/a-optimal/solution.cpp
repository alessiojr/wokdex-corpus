#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Consulta {
    int inicio, fim;
};

bool compararConsultas(const Consulta &a, const Consulta &b) {
    if (a.fim != b.fim) return a.fim < b.fim;
    return a.inicio < b.inicio;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    if (!(cin >> N)) return 0;
    
    vector<Consulta> consultas(N);
    for (int i = 0; i < N; ++i) {
        cin >> consultas[i].inicio >> consultas[i].fim;
    }
    
    sort(consultas.begin(), consultas.end(), compararConsultas);
    
    int atendidas = 0;
    int ultimoFim = 0;
    
    for (int i = 0; i < N; ++i) {
        if (consultas[i].inicio >= ultimoFim) {
            atendidas++;
            ultimoFim = consultas[i].fim;
        }
    }
    
    cout << atendidas << endl;
    
    return 0;
}
