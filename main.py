import random


def main():
    DICE_COUNT = 1
    PLAYER_COUNT = 2
    show_welcome()
    dices = throw_dice(DICE_COUNT)
    total_rounds = 0
    for dice in dices:
        total_rounds += dice
    print(f'Wir spielen {total_rounds} Runden')
    player_totals = [0, 0]
    round = 1
    while (round <= total_rounds):
        print('+----------+')
        print(f'| Runde {round}  |')
        print('+----------+')
        player = 0
        while (player < PLAYER_COUNT):
            print(f'\nSpieler {player + 1} du bist dran')
            points = player_round()
            if points == -1:
                print('  Oh nein! Du hast alle Punkte verloren')
            else:
                player_totals[player] += points
                print(f'  Du hast nun Total {player_totals[player]} Punkte')
            player += 1
        round += 1
    show_winner(player_totals)

def player_round():
    round_points = 0
    while True:
        dices = throw_dice(2)
        print(f'  Du hast {dices[0]} und {dices[1]} gewürfelt')
        if dices[0] == 1 and dices[1] == 1:
            return -1
        elif dices[0] == 1 or dices[1] == 1:
            print('  Leider ist deine Runde vorbei')
            return 0
        else:
            round_points += dices[0] + dices[1]
            print(f'  Dein Total für diese Runde ist {round_points}', end=' ')
            again = input('Willst du nochmal würfeln? (Y/n)? ')
            if again.lower() == 'n':
                return round_points


def throw_dice(number):
    """
    Throws a number of six sided dice and returns a tupel with the points
    :param number: how many dice to roll
    :return: tupel
    """
    i = 0
    dice = list()
    while i < number:
        dice.append(random.randint(1, 6))
        i += 1

    return dice

def show_winner(totals):
    """
    Shows the winner of the game
    :param totals: list of totals
    :return:
    """
    winner = 0
    highest = -1
    index = 0
    for total in totals:
        print (f'Spieler {index+1} hat {total} Punkte erreicht')
        if total > highest:
            highest = total
            winner = index
        index += 1

    print (f'Der Sieger ist Spieler {winner+1}')

def show_welcome():
    """
    shows the welcome message
    :return:
    """
    print('Willkommen zu Groan! Ein taktisches Würfelspiel für 2 Spieler')
    choice = input('Willst du die Regeln lesen (y/N)? ')
    if choice.lower() == 'y':
        print('************************************************')
        print('Regeln blabla')
        print('************************************************')


if __name__ == '__main__':
    main()
