matriz = []
novaMatriz = []
novaMatriz2 = []
lista_palavras_separadas = []
listaIncorrect = []
soma = 0
quantidade = 0
incorrect = 0
x = 0

while True:
    linha = input()
    if linha == '0':
        break
    matriz.append(linha)

for i in matriz:
    novaMatriz.append([i])
    
for i in novaMatriz:
    elemento = i[0]
    palavras = elemento.split()
    lista_palavras_separadas.append(palavras)

for i in lista_palavras_separadas:
    lista = i
    if len(i) == 3:
        x = x + 1
        if lista[2] == "incorrect":
            listaIncorrect.append(lista[0])
        if lista[2] == "correct":
            if lista[0] in listaIncorrect:
                incorrect = incorrect + listaIncorrect.count(lista[0])
            soma = int(lista[1]) + soma
            quantidade = quantidade + 1
    elif (len(i) == 1) and (x >= 1):
        print("%d %d" % (quantidade, (soma + (incorrect * 20))))
        quantidade = 0
        soma = 0
        incorrect = 0
        x = x + 1
        listaIncorrect.clear()
        
if (len(lista_palavras_separadas)) == (x + 1):
    print("%d %d" % (quantidade, (soma + (incorrect * 20))))