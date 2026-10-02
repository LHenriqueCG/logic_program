cargo = str(input("Qual seu cargo? -> "))
hora_atual = int(input("Que horas são? -> "))
chave_emergencia = int(input("A chave de emergência está ativa? se sim digite 1 se não digite 0 -> "))

if (chave_emergencia == 1) or (cargo == "supervisor") or (cargo == "operador" and 8 <= hora_atual <= 17):
    print ("Acesso Liberado")
else:
    print ("Acesso Bloqueado")