import random


def main():
    show_welcome()
    total_rounds = throw_dice(2)
    print(f'Wir spielen {total_rounds} Runden')
    round = 1
    # while (round < total_rounds ):
    #     # play one round
    #     player = 1
    #     while (player < 2):
    #         # one player plays his round
    #         pass
    #     round+=1


def throw_dice(number):
    i = 0
    dice = list()
    while i < number:
        dice.append(random.randint(1,6))
        i+=1

    return dice

def show_welcome():
    """
    shows the welcome message
    :return:
    """
    print('Willkommen zu Groan! Ein taktisches Würfelspiel für 2 Spieler')
    choice = input('Willst du die Regeln lesen (y/N)? ')
    if choice.lower() == 'y':
        print ('Regeln blabla')




if __name__ == '__main__':
    main()
