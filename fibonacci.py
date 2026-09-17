anterior = 0
atual = 1
proximo = (anterior + atual)
print(anterior)
print(atual)
print(proximo)
while (proximo <= 2000 ):
    anterior = atual
    atual = proximo
    proximo = anterior + atual
    print(proximo)