lista=[]
for i in range (0,8):
    numero=int(input("Digite um número: "))
    lista.append(numero)

numero_adicional = int(input("Digite um número adicional para verificarmos se está na lista: "))
if numero_adicional in lista:
        print(f'o número está na posição {lista.index(numero_adicional)}')
