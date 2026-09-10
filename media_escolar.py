notaP = float (input ("Digite a nota de Português:"))
notaM = float (input ("Digite a nota de Matemática:"))
notaC = float (input ("Digite a nota de Ciências:"))
notaH = float (input ("Digite a nota de História:"))
notaG = float (input ("Digite a nota de Geografia:"))

media = (notaP + notaM + notaC + notaH + notaG) / 5

if media >= 6:
    print (f"Média do aluno é: {media:.1f} - Aluno aprovado!")
else:
    print(f"Média do aluno é: {media:.1f} - Aluno Reprovado!")