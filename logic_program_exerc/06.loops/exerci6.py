# Construa um programa que só aceite notas escolares entre zero e dez
# (treinamento para controle de erros).

nota = float(input('Digite a nota do aluno: '))

while nota < 0 or nota > 10:
    print ("A nota deve estar entre 0 e 10")
    nota = float(input('Digite a nota do aluno: '))