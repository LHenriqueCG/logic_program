# Construa um programa onde o usuário digitará três números e o programa
# exibirá, na tela, o maior entre eles.

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))

numeros = []
numeros.append(numero1)
numeros.append(numero2)
numeros.append(numero3)

maior = max(numeros)
print(f'O maior entre eles é {maior}')