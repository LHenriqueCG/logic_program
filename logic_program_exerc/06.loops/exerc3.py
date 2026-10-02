# Construa um programa onde o usuário digitará um número e o programa
# completará o número digitado até 0, apenas com números pares.

numero = int(input("Digite um número para ir até 0, apenas com números pares: "))


for i in range(numero,-1,-1):
    if numero % 2 == 0:
        print (numero)
    numero -= 1 