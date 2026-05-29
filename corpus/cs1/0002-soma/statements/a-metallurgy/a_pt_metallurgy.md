# O Grande Forno de Alta Precisão

Bem-vindo à refinaria central! Aqui operamos o Forno Blast-X9000, capaz de atingir temperaturas de **1538°C** para o ferro e **1085°C** para o cobre.

Para a produção da "Super Liga Z", o processo é extremamente delicado. A temperatura ambiente deve estar em exatos **23°C**, e a umidade relativa do ar não pode passar de **45%**. O forno leva cerca de **40 minutos** para pré-aquecer.

O Engenheiro Chefe precisa de um relatório sobre a carga total de materiais brutos. O processo envolve jogar dois tipos de minério no forno. Apesar de todas as variáveis complexas de temperatura, pressão (**101.3 kPa**) e tempo de resfriamento (**12 horas**), a lei de conservação de massa de Lavoisier ainda impera absoluta: nada se perde, tudo se transforma.

Sua tarefa, em meio a todos esses controles de painel e leituras de sensores complexos, é na verdade bem simples (mas não conte para o chefe que é só isso!): precisamos apenas saber qual será o peso final da mistura no início do processo.

## Entrada
O sistema do forno fornecerá dois valores inteiros $X$ e $Y$, representando, respectivamente, a quantidade (em kg) do **Minério A** e do **Minério B**. (Ignore os sensores de temperatura e pressão, eles são lidos por outro subsistema).

*Domínio: $-10^4 \leq X, Y \leq 10^4$*

## Saída
Imprima um único número inteiro representando a massa total que estará dentro do forno.

## Exemplos

| Entrada | Saída |
| :--- | :--- |
| 2<br>7 | 9 |

| Entrada | Saída |
| :--- | :--- |
| 10<br>5 | 15 |
