# passo 1: criar variavel 
# passo 1.5: atribuir valor a variavel
numero = int(input("Digite um numero: "))

# passo 2: verificar se o resto da divisão da variavel por "2" é 0
resultado = numero % 2

# passo 2.1: se for -> "É Par"
if resultado == 0:
  print (f"{numero} é par")

else:
  print(f"{numero} é impar")  

# passo 3: se não for -> "É Impar"

print(f"A metade de {numero} é: {numero / 2}")
print (f"O resto da divisão de {numero} por 2 é: {resultado}")