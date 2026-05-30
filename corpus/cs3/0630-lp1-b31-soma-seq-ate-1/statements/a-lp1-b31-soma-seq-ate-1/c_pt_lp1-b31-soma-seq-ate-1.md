# Soma de Valores

Lembre-se do padrão da "Sentinela" num laço `while`. A Sentinela é o gatilho de saída (o valor que dispara a nossa parada).
Crie um bloco `while(true)` e dentro dele efetue a leitura da sua variável (por exemplo, `cin >> X`). Se `X == -1`, então você imediatamente dá um `break;` para escapar do bloco e não incluir o `-1` na soma! Caso contrário, apenas some `X` no seu acumulador global.
Após o loop, basta imprimir `cout << "A soma dos valores eh: " << soma`.
