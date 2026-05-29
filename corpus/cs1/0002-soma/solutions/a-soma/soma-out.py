# Alternativa 1: Usando map() para converter diretamente

# Alternativa 2: Usando list comprehension
# valor1, valor2 = [int(x) for x in input().split()]

# Alternativa 3: Usando unpacking com split()
# valor1, valor2 = input().split()
# valor1, valor2 = int(valor1), int(valor2)
# print("resultado:", valor1 + valor2)
# print("==Resultado==\n");

# print("==Digite um número==\n");
material_1 = int(input())
material_2 = int(input())
soma = material_1 + material_2
# print("==Digite um número==\n");
print(soma)