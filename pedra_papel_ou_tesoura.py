import random

jogadas = ['pedra' , 'papel' , 'tesoura']
jogador = str(input("Jogador : Escolha pedra , papel ou tesoura e digite a seguir ->"))
pc = random.choice(jogadas)
print(pc)

if jogador == "pedra" and pc == "pedra" or jogador == "papel" and pc == "papel" or jogador == "tesoura" and pc == "tesoura" :
    print (f"Os dois jogadores escolheram {jogador}: EMPATE")

elif jogador == "pedra" and pc == "papel":
    print ("Jogador 2 venceu. Papel embrulha a pedra")

elif jogador == "pedra" and pc == "tesoura":
    print ("Jogador 1 venceu. Pedra quebra a tesoura")

elif jogador == "papel" and pc == "tesoura":
    print ("Jogador 2 venceu. tesoura corta o papel")

elif jogador == "papel" and pc == "pedra":
    print ("Jogador 1 venceu. Papel embrulha a pedra")

elif jogador == "tesoura" and pc == "papel":
    print ("Jogador 1 venceu. Tesoura corta o papel")

elif jogador == "tesoura" and pc == "pedra":
    print ("Jogador 2 venceu. Pedra quebra a pedra")

else:
    print ("Jogada inválida!")