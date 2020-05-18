import random

options = ["Piedra", "Papel", "tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()

    if player == ai:
        return 'Empate!'

    elif player == 'piedra':
        if ai == 'papel':
            return 'Perdiste!'
        else:
            return 'Ganaste!'

    elif player == 'papel':
        if ai == 'tijeras':
            return 'Perdiste!'
        else:
            return 'Ganaste!'

    elif player == 'tijeras':
        if ai == 'piedra':
            return 'Perdiste!'
        else:
            return 'Ganaste!'

# Entry Point
def Game():
    global options

    player = random.choice(options)
    ai = random.choice(options)

    winner = quienGana(player, ai)

    print(winner)

