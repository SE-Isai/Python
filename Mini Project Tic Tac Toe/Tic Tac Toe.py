#Preguntar nombres
#while loop para jugar otra vez
#imprimir el mapa y elegiremos el jugador "x" y "0"
#contador de juegos
#variable booleana para detectar el ganador

from random import choice
player_1 = input(" Jugador 1, introduce tu nombre")
player_2 = input(" Jugador 2, introduce tu nombre")
play = True
while play:
    game = list(range(0, 9))
    win = False
    occupied_cases = 0
    player_turn = choice([player_1, player_2])
    if player_turn == player_1:
        print("El jugador 1 juega X\n El jugador 2 juega O ")
    else:
        print("El jugador 2 juega X\n El jugador 1 juega O ")
    while not win and occupied_cases <= 8:
        print("\n" + str(game[0]), game[1], game[2])
        print(game[3], game[4], game[5])
        print(game[6], game[7], game[8], "\n")
        move = int(input("Jugador X, haz un movimiento"))
        while move not in range (0,9) or game[move] not in range (0,9):
            move = int(input("Entrada invalida, haz un nuevo movimiento"))
        game[move] = "X"
        print("\n" + str(game[0]), game[1], game[2])
        print(game[3], game[4], game[5])
        print(game[6], game[7], game[8], "\n")
        occupied_cases += 1
        win = game[0] == game[1] == game[2] or game[3] == game[4] == game[5] or game[6] == game[7] == game[8] or game[6] == game[3] == game[0] or game[7] == game[4] == game[1] or game[8] == game[5] == game[2] or game[0] == game[4] == game[8] or game[6] == game[4] == game[2]
        if win:
            print("\n\tEl jugador X gana\t")
            play_again = input(("¿Jugar otra vez? Y/N")).lower()
            while play_again != "y" and play_again != "n":
                play_again = input("Introduzca los datos correctos\n¿Jugar otra vez? Y/N").lower()
            if play_again == "y":
                play = True
                print("Juego nuevo")
            else:
                play = False
                print("Juego terminado")

        elif occupied_cases > 8:
            print("Empate")
            play_again = input(("¿Jugar otra vez? Y/N")).lower()
            while play_again != "y" and play_again != "n":
                play_again = input("Introduzca los datos correctos\n¿Jugar otra vez? Y/N").lower()
            if play_again == "y":
                play = True
                print("Juego nuevo")
            else:
                play = False
                print("Juego terminado")
        else:
            move = int(input("Jugador O, haz un movimiento"))
            while move not in range(0, 9) or game[move] not in range(0, 9):
                move = int(input("Entrada invalida, haz un nuevo movimiento"))
            game[move] = "O"
            print("\n" + str(game[0]), game[1], game[2])
            print(game[3], game[4], game[5])
            print(game[6], game[7], game[8], "\n")
            occupied_cases += 1
            win = game[0] == game[1] == game[2] or game[3] == game[4] == game[5] or game[6] == game[7] == game[8] or game[6] == game[3] == game[0] or game[7] == game[4] == game[1] or game[8] == game[5] == game[2] or game[0] == game[4] == game[8] or game[6] == game[4] == game[2]
            if win:
                print("\n\tEl jugador O gana\t")
                play_again = input(("¿Jugar otra vez? Y/N")).lower()
                while play_again != "y" and play_again != "n":
                    play_again = input("Introduzca los datos correctos\n¿Jugar otra vez? Y/N").lower()
                if play_again == "y":
                    play = True
                    print("Juego nuevo")
                else:
                    play = False
                    print("Juego terminado")

            elif occupied_cases > 8:
                print("Empate")
                play_again = input(("¿Jugar otra vez? Y/N")).lower()
                while play_again != "y" and play_again != "n":
                    play_again = input("Introduzca los datos correctos\n¿Jugar otra vez? Y/N").lower()
                if play_again == "y":
                    play = True
                    print("Juego nuevo")
                else:
                    play = False
                    print("Juego terminado")
