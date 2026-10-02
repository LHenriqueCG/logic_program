# Desenvolva um programa para registrar as vendas de uma loja ao longo
# do dia.

# O programa deve processar múltiplos clientes até que o
# operador digite 0 no total de compras para encerrar o expediente.

# Regras de Negócio:
# ■ Para cada cliente, utilize um loop while que leia o valor de cada
# produto comprado, somando-os até que seja digitado -1 (fim da
# compra daquele cliente).

# ■ Se o valor total da compra for superior a R$ 200, aplique 10%
# de desconto; se for superior a R$ 100, aplique 5%; caso
# contrário, sem desconto (utilize if/elif/else).

# ■ Pergunte a quantidade de parcelas (de 1 a 6). Utilize um loop
# for para exibir o cronograma de pagamento, mostrando o valor
# exato de cada parcela mensal.

# ■ Ao final do expediente (quando for digitado 0 para novo cliente),
# exiba o faturamento total acumulado do dia e a quantidade de
# clientes atendidos.

# ○ Restrição: Utilize apenas variáveis numéricas acumuladoras (float e
# int). Não utilize listas.

cliente = 0
faturamento = 0
total = 0
parcelas = int(input('Você pode parcelar em até 6x, será em quantas vezes?: '))

while True:
    compra = float(input('valor do item: R$'))
    if compra == 0:
        break
    if compra == -1:
        if valor_total > 0:
            clientes += 1
