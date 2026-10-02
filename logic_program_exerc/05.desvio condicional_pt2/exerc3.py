# Um sistema de controle de maquinário pesado deve autorizar a operação
# com base em: cargo (string: "operador" ou "supervisor"), hora_atual (inteiro
# de 0 a 23) e chave_emergencia (booleano). O acesso deve ser concedido se:
# ◆ A chave_emergencia estiver ativa (True), independentemente de
# qualquer outra variável; OU
# ◆ O usuário for "supervisor"; OU
# ◆ O usuário for "operador" E a hora_atual estiver entre 8 e 17 (inclusive).
# ◆ Caso contrário, o sistema deve exibir "Acesso Bloqueado".

cargo = (input('Digite seu cargo: '))
hora_atual = int(input('Digite a hora atual (Entre 0 e 23): '))
chave_emergencia = bool(input('Se a chave de emergencia não tiver ativa só de "Enter" nessa opção mas se tiver ativa escreva algo a seguir: '))

if chave_emergencia == True or\
   cargo == "supervisor" or\
   cargo == "operador" and 8 <= hora_atual <= 17:
     print('Acesso concedido')

else:
    print('Acesso Bloqueado')