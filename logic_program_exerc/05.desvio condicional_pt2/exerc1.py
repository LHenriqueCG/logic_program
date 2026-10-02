# Escreva um programa em Python que receba três valores numéricos reais (a,
# b e c) representando os comprimentos dos lados de um triângulo.

# ◆ O programa deve primeiro verificar a condição de existência geométrica:
# a soma de dois lados quaisquer deve ser estritamente maior que o
# terceiro lado.

# ◆ Caso a condição seja atendida, classifique o triângulo em Equilátero,
# Isósceles ou Escaleno.

# ◆ Se as medidas não formarem um triângulo, exiba uma mensagem de
# erro.
lado1 = float(input(f'Escolha uma medida para o primeiro lado do triângulo: '))
lado2 = float(input(f'Escolha uma medida para o segundo lado do triângulo: '))
lado3 = float(input(f'Escolha uma medida para o terceiro lado do triângulo: '))

if lado1 + lado2 < lado3 or \
   lado3 + lado2 < lado1 or \
   lado1 + lado3 < lado2:
   print('As medidas não são válidas para formação de um triângulo')

elif lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print('Os três lados do triângulo são iguais. É um triângulo EQUILÁTERO')

elif lado1 == lado2 and lado3 != lado1 and lado3 != lado2 or\
lado1 == lado3 and lado2 != lado1 and lado2 != lado3 or\
lado3 == lado2 and lado1 != lado2 and lado1 != lado3:
    print('Dois lados do triângulo são iguais e um diferente. É um triângulo ISÓSCELES')

elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print('Os três lados do triângulo são diferentes. É um triângulo ESCALENO')

