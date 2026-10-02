import random

jogadas = ['pedra' , 'papel' , 'tesoura']
jogador = str(input("Jogador : Escolha pedra , papel ou tesoura e digite a seguir ->"))
pc = random.choice(jogadas)
print(pc)

if jogador == "pedra" and pc == "pedra" or jogador == "papel" and pc == "papel" or jogador == "tesoura" and pc == "tesoura" :
    print (f"Os dois jogadores escolheram {jogador}: EMPATE")

elif jogador == "pedra" and pc == "papel":
    print ("A máquina venceu. Papel embrulha a pedra")

elif jogador == "pedra" and pc == "tesoura":
    print ("Você venceu. Pedra quebra a tesoura")

elif jogador == "papel" and pc == "tesoura":
    print ("A máquina venceu. tesoura corta o papel")

elif jogador == "papel" and pc == "pedra":
    print ("Você venceu. Papel embrulha a pedra")

elif jogador == "tesoura" and pc == "papel":
    print ("Você venceu. Tesoura corta o papel")

elif jogador == "tesoura" and pc == "pedra":
    print ("A máquina venceu. Pedra quebra a pedra")

else:
    print ("Jogada inválida!")