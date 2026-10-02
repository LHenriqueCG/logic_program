# Construa um programa onde o usuário digitará um valor e o programa
# mostrará, na tela, a tabuada de multiplicação deste número.
numero = int(input('Digite um número para ver sua tabuada de multiplicação: '))

for i in range(10):
    print((i+1)*numero)