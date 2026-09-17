nota = float(input('Digite a nota entre 0 e 10: '))

while (nota < 0 or nota > 10):
    print(f'Você digitou {nota} , mas',
          'ela deve estar entre 0 e 10.' )
    nota = float(input('Digite a nota entre 0 e 10: '))
