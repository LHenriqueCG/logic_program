numero = int(input("Digite um número para ir até 0 -> "))

for i in range(numero, -1, -1):
    if i % 2 == 0:
        print (i)