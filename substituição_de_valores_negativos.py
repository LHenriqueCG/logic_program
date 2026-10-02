# Programa onde o usuário digitará dez números inteiros para preencher um vetor.
# Em seguida, o programa substitui todos os números negativos por zero.
lista=[]
for i in range (0,10):
    numero=int(input("Digite um número: "))
    lista.append(numero)

for numero in lista:
    if numero < 0:
        indice = lista.index(numero)
        lista.pop(indice)
        lista.insert(indice, 0)

print(lista)