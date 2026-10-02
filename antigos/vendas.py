soma_total = 0
total_clientes = 0
valor_total = 0

while True:
    valor_produto = float(input('Insira o valor do produto! ->'))

    if valor_produto == 0:
        break

    if valor_produto == -1:

        if valor_total > 0:
            total_clientes += 1

            if valor_total > 200:
                valor_final = valor_total * 0.9
                print(f'O valor total inicial é de R${valor_total} e com o desconto de 10% fica R${valor_final}')

            elif valor_total > 100:
                valor_final = valor_total * 0.95
                print(f'O valor total inicial é de R${valor_total} e com o desconto de 5% fica R${valor_final}')

            else:
                valor_final = valor_total
                print(f'(Valor não é válido para desconto) O valor total é de R${valor_final}')
            parcelas = int(input('Digite a quantidade de parcelas que deseja, em até 6 vezes: '))

            while parcelas < 1 or parcelas > 6:
                print(f'Você digitou {parcelas}, mas deve estar entre 1 e 6')
                parcelas = int(input('Digite a quantidade de parcelas que deseja, em até 6 vezes: '))
            valor_parcela = valor_final / parcelas

            for mes in range(1, parcelas + 1):
                print(f'No mês {mes} a parcela será R$ {valor_parcela:.2f}')
            soma_total += valor_final
            valor_total = 0
        print('PRÓXIMO CLIENTE')
        
    else:
        valor_total += valor_produto
print('EXPEDIENTE ENCERRADO')
print(f'Seu faturamento hoje foi de R${soma_total:.2f} e o número de clientes atendidos foi de {total_clientes}')