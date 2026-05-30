# Ajude! - Tutorial Passo a Passo

## 1. Entendendo o Desafio
Você tem uma missão crítica: o software da competição pifou e você precisa criar um gerador de *score* para salvar o dia!

A regra de pontuação na maratona é simples e segue dois pontos diretos:
1. Um time ganha **1 ponto** para cada problema resolvido corretamente ("correct").
2. O **Tempo Total** é a soma dos minutos exatos em que cada problema foi resolvido, mas com uma penalidade extra: adiciona-se **20 minutos** obrigatoriamente para cada tentativa falha ("incorrect") anterior daquele problema — mas **apenas** se o problema for eventualmente resolvido. Problemas que o time tentou mas nunca acertou não afetam o tempo!

## 2. Estruturação dos Dados
Como o input contém no máximo as submissões de 26 problemas (letras de 'A' a 'Z'), o tamanho da estrutura de dados não é um limitador. Podemos usar um Array simples ou um Dicionário / Hash Map para gerenciar o "rascunho" de erros.

Precisamos de 3 estruturas lógicas principais para cada caso de teste:
- `questoes_resolvidas = 0` (acumulador do placar)
- `tempo_total = 0` (acumulador do tempo global)
- Um Array/Map `penalidades_acumuladas` indexando as letras ou códigos ASCII do problema (ex: `penalidades['A'] = 0`, `penalidades['B'] = 0`, ...).

## 3. Passo a Passo da Lógica

Para lermos e processarmos as `N` linhas, basta o seguinte raciocínio:

### Passo 3.1: Leitura Indeterminada
Use um bloco `while` global lendo `N`, com a condição de quebra automática `if N == 0`. Lembre-se, importantíssimo, de preencher as variáveis do Passo 2 com ZEROS a cada novo ciclo de `N`!

### Passo 3.2: Avaliação da Submissão
Crie um Loop de 1 até `N` e em cada etapa leia os três atributos: `ID_Problema`, `Tempo_Minutos` e `Veredito`.

- **Se o `Veredito` = "incorrect"**:
  Isso significa que o time errou, mas não devemos somar os +20 minutos no tempo global ainda. Apenas registramos no nosso "rascunho".  
  Faça: `penalidades_acumuladas[ID_Problema] += 20`

- **Se o `Veredito` = "correct"**:
  Bingo! O time resolveu o desafio. Aqui é onde toda a bagagem é cobrada.
  Faça:
  1. `questoes_resolvidas += 1`
  2. `tempo_total += Tempo_Minutos` (o momento atual em que submeteram o acerto)
  3. `tempo_total += penalidades_acumuladas[ID_Problema]` (todas aquelas tentativas fracassadas que tínhamos guardado no rascunho caem no saldo do time agora!)

*(Nota de Otimização: A questão garante cronologia correta e apenas um "correct" máximo. Você não precisa usar flags para proteger múltiplas sentenças de correct do mesmo problema).*

### Passo 3.3: Impressão
Após acabar as lidas do bloco `N` atual, apenas imprima `questoes_resolvidas` e `tempo_total` separados por um espaço em branco, com a devida quebra de linha `\n`.


## Exemplo Isolado
Se a entrada for:
`C 10 incorrect` -> `penalidades['C'] = 20`
`C 15 incorrect` -> `penalidades['C'] = 40`
`A 18 correct` -> (Resolveu A no minuto 18!) `questoes = 1`. `tempo_total = 18` (A não tinha penalidade anterior).
`C 25 correct` -> (Resolveu C!). `questoes = 2`. `tempo_total += 25` (minuto do acerto) + `40` (que estavam guardados na `penalidades['C']`) = `83`.

O output desse bloco seria simplesmente: `2 83`.


### Exemplo de Entrada e Saída

```
0 0
3 431
```
