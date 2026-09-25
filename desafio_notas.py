#Crie um array/lista com as notas de 5 alunos (você escolhe os valores).
notas = [8.5, 5.0, 9.5, 6.0, 4.5]

#Use um for para percorrer o array e mostrar cada nota na tela.
for nota in notas:
    print(nota)

    #Dentro do mesmo for, use um if para classificar cada nota: "Aprovado" (nota ≥ 6) ou "Reprovado" (nota < 6).
    if nota >= 6:
        print("Aprovado\n")
    else:
        print("Reprovado\n")

#Depois do for, calcule a média das notas.
media = sum(notas) / len(notas)
print(f"A média das nota é: {media}\n")

#Use um while para pedir ao usuário que digite notas novas até ele digitar -1 (ou outro valor "sentinela" pra parar), e vá guardando essas notas num novo array.
notas_input = []
nota_input = 0
while nota_input != -1:

    nota_input = float(input("(Para encerrar o envio de notas digite -1)\nInsira uma nota nova: "))
    if nota_input != -1:
        notas_input.append(nota_input)

#No final, mostre quantos alunos foram aprovados e quantos foram reprovados.
todas_notas = notas + notas_input
print(f"Essas são todas as notas: {todas_notas}")
aprovados = []
reprovados = []
for nota in todas_notas:
    if nota >= 6:
        aprovados.append(nota)
    else:
        reprovados.append(nota)

print(f"Os Aprovados são as notas: {aprovados}\nOs reprovados são as notas: {reprovados}")
print(f"Aprovados: {len(aprovados)}\nReprovados: {len(reprovados)}")
