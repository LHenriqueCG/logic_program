renda_mensal = float(input("Informe sua renda mensal -> "))
score = int(input("Informe seu Score -> "))
restricao = int(input("Possui alguma retrição financeira em seu nome? se sim digite 1 se não digite 0 ? ->"))

if (score >= 700 and renda_mensal >= 4000 and restricao == 0):
    print ("Sua solicitação de empréstimo foi aceita.")

elif (renda_mensal >= 2500 and restricao == 0 and score >= 500 or renda_mensal > 6000):
    print("Sua solicitação está em análise , aguarde o contato.")

else:
    print("Sua solicitação não foi aprovada, tente outra vez futuramente.")
