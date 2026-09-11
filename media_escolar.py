notaP = float (input ("Digite a nota de Português:"))
notaM = float (input ("Digite a nota de Matemática:"))


media = (notaP + notaM) / 2

if media >= 6:
    print (f"Média do aluno é: {media:.1f} - Aluno aprovado!")
else:
    print(f"Média do aluno é: {media:.1f} - Aluno Reprovado!")