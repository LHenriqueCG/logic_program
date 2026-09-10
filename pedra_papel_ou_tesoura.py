jogada1 = str(input("Jogador 1 : Escolha pedra , papel ou tesoura e digite a seguir ->"))
jogada2 = str(input("Jogador 2 : Escolha pedra , papel ou tesoura e digite a seguir ->"))

if jogada1 == "pedra" and jogada2 == "pedra" or jogada1 == "papel" and jogada2 == "papel" or jogada1 == "tesoura" and jogada2 == "tesoura" :
    print (f"Os dois jogadores escolheram {jogada1}: EMPATE")

elif jogada1 == "pedra" and jogada2 == "papel":
    print (f"Jogador 2 venceu. Papel embrulha a pedra")

elif jogada1 == "pedra" and jogada2 == "tesoura":
    print (f"Jogador 1 venceu. Pedra quebra a tesoura")

elif jogada1 == "papel" and jogada2 == "tesoura":
    print (f"Jogador 2 venceu. tesoura corta o papel")

elif jogada1 == "papel" and jogada2 == "pedra":
    print (f"Jogador 1 venceu. Papel embrulha a pedra")

elif jogada1 == "tesoura" and jogada2 == "papel":
    print (f"Jogador 1 venceu. Tesoura corta o papel")

elif jogada1 == "tesoura" and jogada2 == "pedra":
    print (f"Jogador 2 venceu. Pedra quebra a pedra")

else:
    print (" Jogada inválida!")