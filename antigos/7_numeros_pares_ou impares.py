pares=0
impares=0

for pegar in range (0,7):
    pegar=int(input('Escreva um número: '))
    if pegar % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Os números pares são {pares} e os impares são {impares}')
