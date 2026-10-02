# Construa um programa que o usuário digitará um número e a aplicação
# completará o número digitado até completar cem.

numero = int(input('Digite um número para a aplicação completar o número digitado até cem: '))

while numero <= 100:
    print(numero)
    numero += 1

for i in range(numero,101):
    print(i)