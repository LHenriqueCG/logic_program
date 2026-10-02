# Construa um programa onde o usuário digitará duas notas escolares e o
# programa irá calcular a média e, caso seja menor que 6, exibirá na tela:
# “Aluno Reprovado”. Caso seja maior ou igual a 6 exibirá na tela: “Aluno
# Aprovado”.
nota1 = float(input(f'Digite a primeira nota: '))
nota2 = float(input(f'Digite a segunda nota: '))
media = float(nota1+nota2) / 2

if media < 6 :
    print('Aluno Reprovado')
else:
    print('Aluno Aprovado')