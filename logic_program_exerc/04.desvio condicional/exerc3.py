# Construa um jogo de pedra, papel e tesoura.
pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'
jogador1 = (input(f"Jogador 1 - Escolha um entre pedra, papel ou tesoura e escreve sua jogada a seguir: "))
jogador2 = (input(f"Jogador 2 - Escolha um entre pedra, papel ou tesoura e escreve sua jogada a seguir: "))

if jogador1 == jogador2:
    print(f"Os dois jogadores jogaram {jogador1}! EMPATE")

elif jogador1 == 'pedra' and jogador2 == 'papel' or \
    jogador1 == 'papel' and jogador2 == 'tesoura' or \
    jogador1 == 'tesoura' and jogador2 == 'pedra':
     print(f'Jogador 2 venceu! {jogador2} ganha de {jogador1}.')

elif jogador2 == 'pedra' and jogador1 == 'papel' or \
    jogador2 == 'papel' and jogador1 == 'tesoura' or \
    jogador2 == 'tesoura' and jogador1 == 'pedra':
    print(f'Jogador 1 venceu! {jogador1} ganha de {jogador2}.')

else:
    jogador1 or jogador2 != 'pedra' or 'papel' or 'tesoura'
    print("Sua jogada não é uma jogada válida. Recomece o jogo e escolha entre pedra , papel ou tesoura")