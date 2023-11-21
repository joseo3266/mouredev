'''*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 *'''
points = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2","P1","P2","P1","P1"]
#points = ["P1", "P1", "P1", "P1","P1"]
#points = ["P2", "P2", "P2", "P2","P2"]

i1 = 0
i2 = 0
i = 0 
winner = False

player1 = ['love',15, 30, 40, 'winner']
player2 = ['love',15, 30, 40, 'winner']

for point in points:
    if winner == True:
        break
    if player1[i1] == 40 and player2[i2] == 40:

        print(f"Deuce")
        while True:

            if points[i] == 'P1':
                print("Ventaja Player 1")
                i += 1
                if points[i] == 'P1':
                    print("Victoria Jugador 1!")
                    winner = True
                    break
                elif points[i] == 'P2':
                    i += 1
                    print("Deuce")
                    continue

            elif points[i] == 'P2':
                print("Ventaja player 2")
                i += 1
                if points[i] == 'P2':
                    print("Victoria Player 2")
                    winner = True
                    break
                elif points[i] == 'P1':
                    i += 1
                    print('deuce')
                    continue
            
    elif point == 'P2':
        i2 +=1
        if player2[i2] == 'winner':
            print(f"{player1[i1]} - {player2[i2]}")
            break
        else:
            print(f"{player1[i1]} - {player2[i2]}")


    elif point == 'P1':
        i1 += 1
        if player1[i1] == 'winner':
            print(f"{player1[i1]} - {player2[i2]}")
            break
        else:
            print(f"{player1[i1]} - {player2[i2]}")
    i += 1