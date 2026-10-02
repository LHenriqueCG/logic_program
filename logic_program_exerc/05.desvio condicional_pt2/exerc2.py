# Crie um script que avalie a concessão de empréstimo com base em três
# variáveis: renda_mensal (float), score (inteiro de 0 a 1000) e possui_restricao
# (booleano).
# ◆ Aprovado: score maior ou igual a 700, renda_mensal a partir de 4000.00
# e sem restrições cadastrais.
# ◆ Análise Manual: Se não for aprovado diretamente, mas a renda_mensal
# for de pelo menos 2500.00, sem restrições, e (score maior ou igual a 500
# ou renda_mensal superior a 6000.00).
# ◆ Recusado: Qualquer outro caso.
renda_mensal = float(input('Informe sua renda mensal: ' ))
score = float(input('Informe seu score: ' ))
possui_restricao = bool(input('Se você não possui algum tipo de restrição não digite nada e dê enter mas se você tiver, digite algo a seguir: '.strip()))

if score >= 700 and renda_mensal >= 4000 and possui_restricao == False:
    print('Aprovado')

elif renda_mensal >= 2500 and possui_restricao == False and score >= 500 or renda_mensal > 6000:
    print('Análise Manual')

else:
    print('Recusado')