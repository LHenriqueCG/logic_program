# Variáveis acumuladoras
# Guarda a soma do valor final de todas as compras do dia
soma_total = 0
# Conta quantos clientes foram atendidos no dia
total_clientes = 0
# Acumula os valores dos produtos de UM cliente enquanto ele compra
valor_total = 0

# Loop principal: processa um cliente após o outro
# O programa fica nesse loop até o operador digitar 0 (fim do expediente)
while True:

    # Lê o valor de cada produto que o cliente está comprando
    valor_produto = float(input('Insira o valor do produto! ->'))

    # Encerramento do expediente
    # Se o operador digitar 0, o dia acabou: sai do loop
    if valor_produto == 0:
        break

    # Fim da compra de UM cliente (digitou -1)
    if valor_produto == -1:

        # Só processa se o cliente realmente comprou alguma coisa
        if valor_total > 0:

            # Conta mais um cliente atendido
            total_clientes += 1

            # Regra de desconto (if / elif / else)

            # Compra acima de R$ 200 → desconto de 10%
            if valor_total > 200:
                valor_final = valor_total * 0.9
                print(f'O valor total inicial é de R${valor_total} e com o desconto de 10% fica R${valor_final}')

            # Compra acima de R$ 100 → desconto de 5%
            elif valor_total > 100:
                valor_final = valor_total * 0.95
                print(f'O valor total inicial é de R${valor_total} e com o desconto de 5% fica R${valor_final}')

            # Compra até R$ 100 → sem desconto
            else:
                valor_final = valor_total
                print(f'(Valor não é válido para desconto) O valor total é de R${valor_final}')

            # Parcelamento: acontece para qualquer valor de compra
            # Pergunta em quantas parcelas o cliente quer pagar (1 a 6)
            parcelas = int(input('Digite a quantidade de parcelas que deseja, em até 6 vezes: '))

            # Valida a entrada: só aceita valores entre 1 e 6
            while parcelas < 1 or parcelas > 6:
                print(f'Você digitou {parcelas}, mas deve estar entre 1 e 6')
                parcelas = int(input('Digite a quantidade de parcelas que deseja, em até 6 vezes: '))

            # Calcula o valor de cada parcela
            valor_parcela = valor_final / parcelas

            # Loop for: exibe o cronograma de pagamento mês a mês
            for mes in range(1, parcelas + 1):
                print(f'No mês {mes} a parcela será R$ {valor_parcela:.2f}')

            # Soma o valor final desse cliente ao faturamento total do dia
            soma_total += valor_final

            # Zera o total para o próximo cliente começar do zero
            valor_total = 0

        print('PRÓXIMO CLIENTE')

    # Adição de produto à compra do cliente atual
    # Se não foi -1 nem 0, é um produto: acumula no total do cliente
    else:
        valor_total += valor_produto

# Resumo do expediente (exibido apenas quando o operador digita 0)
print('EXPEDIENTE ENCERRADO')
print(f'Seu faturamento hoje foi de R${soma_total:.2f} e o número de clientes atendidos foi de {total_clientes}')