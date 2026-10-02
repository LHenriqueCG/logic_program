# Construa um programa onde o usuário digitará dez números inteiros. O programa deve
# identificar qual é o maior e qual é o menor número digitado, exibindo também a posição
# (índice) em que cada um deles se encontra no vetor.

numeros = []
for i in range (0,10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

maior_numero = max(numeros)
menor_numero = min(numeros)

print (f'O maior número é {maior_numero} e a posição dele é {numeros.index(maior_numero)}.\nE o menor é {menor_numero} e a posição dele é {numeros.index(menor_numero)}')