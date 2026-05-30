# Ajude! - Dicas e Estratégia

## Objetivo
O problema "Ajude!" simula o sistema de pontuação clássico de uma maratona de programação. Sua tarefa é calcular quantos problemas foram resolvidos pela equipe e calcular o tempo total de penalidade resultante das tentativas dessa equipe.

## Abordagem Recomendada

A forma mais eficiente de resolver este problema é através de uma varredura linear estrita **O(N)** utilizando um mapa ou um simples vetor de inteiros (Array de 26 posições) para rastrear o estado provisório de cada problema ('A' até 'Z').

1. **Rastreamento de Erros**: Como a penalidade de +20 minutos por erro só deve ser aplicada se a equipe **realmente resolver** o problema depois, não podemos somar os 20 minutos imediatamente no tempo global. Devemos acumular esses 20 minutos num contador separado para a letra específica (ex: `penalidades['A']`).
2. **Confirmação de Acerto**: Quando encontrarmos a string `"correct"` para uma letra, incrementamos o número de problemas resolvidos e adicionamos ao tempo global: o tempo daquela submissão + o total de penalidades acumuladas em `penalidades['Letra']`.
3. **Casos de Teste Múltiplos**: Lembre-se de zerar todos os contadores e o array/mapa de penalidades no início de cada novo caso de teste (que é lido repedidamente até `N = 0`).

### Complexidade
- **Tempo:** **O(N)** por caso de teste, pois iteramos sobre a entrada apenas uma vez.
- **Espaço (Memória):** **O(1)**, já que o máximo de chaves possíveis no vetor auxiliar será sempre o tamanho do alfabeto inglês (26 posições).

### Exemplo

```
0 0
3 431
```
