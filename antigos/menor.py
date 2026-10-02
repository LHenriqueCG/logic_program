# como achar o menor valor entre dois números

# Passo 1 -> Ter 2 números
numero1 =  int(input("Digite um número: "))
numero2 =  int(input("Digite outro número: "))


#Passo2 -> Testar condicional
if numero1>numero2:
    print(f"O segundo número: {numero2} é menor que o primeiro número: {numero1}!")

elif numero1==numero2:
    print(f"O primeiro número: {numero1} é igual ao segundo número: {numero2}!")

else:
    print(f"O primeiro número: {numero1} é menor que o segundo número: {numero2}!")