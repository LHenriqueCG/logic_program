# Construa um programa onde o usuário digitará seis notas (números reais).
# O programa deve calcular a média dessas notas e, em seguida, exibir
# quantas e quais notas ficaram estritamente acima da média calculada.

notas = []
soma = 0
for i in range (0,6):
    nota = int(input("Digite a nota: "))
    notas.append(nota)
    soma += nota

media = soma/len(notas)
notas_am = [] # notas acima da média.
for nota in notas:
    if nota > media:
        notas_am.append(nota)

print(f'A média é {media}, a quantidade de notas acima da média são {len(notas_am)}, e as notas são {notas_am}.')    
