notaP = float (input ("Digite a nota de Português:"))
notaM = float (input ("Digite a nota de Matemática:"))
media = notaP + notaM

if media >= 6:
    print (f"Média do aluno é: {media} - Aluno aprovado!")
else:
    print(f"Média do aluno é: {media} - Aluno Reprovado!")