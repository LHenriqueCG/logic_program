# Construa um programa onde o usuário digitará cinco números para preencher um vetor. O
# programa deve criar um segundo vetor que contenha os mesmos elementos do primeiro,
# porém na ordem inversa, e exibir o novo vetor na tela.
numeros = []
for i in range (0,5):
    numero = int(input("Digite o número: "))
    numeros.append(numero)

numeros_inversos = numeros.copy()
numeros_inversos.sort(reverse=True)
print(numeros_inversos)