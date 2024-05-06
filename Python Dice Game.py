import random
import time
import sys
import colorama
from colorama import Fore, Back, Style

def typewriter_whole(text, delay):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(delay)

a = "Initialising world..."
b = "\n.\n.\n.\n.\n.\n.\n.\n"
c = "Initialisation complete!\n"
d = "Transporting..."

typewriter_whole(a, 0.1)
typewriter_whole(b, 0.3)
typewriter_whole(c, 0.1)
typewriter_whole(d, 0.1)
time.sleep(1)

text_whole = Fore.CYAN + """\n\nThe tavern bustles with a diverse array of individuals from across the realm: swashbuckling pirates share tales of high-sea adventures, while wizards clad in shimmering robes engage in arcane discussions, their hands crackling with magic. Knights clad in gleaming armor swap stories of valor, while shadowy figures lurk in dim corners, hinting at clandestine dealings. Amidst it all, serving wenches weave through the crowd with trays of ale, laughter and revelry filling the air. You navigate through this lively scene until you reach an isolated corner table. Seated there is a rugged pirate, his eyes gleaming with anticipation as he awaits a challenger for a game of dice. With a nod, you join him, the promise of gold coins wagered adding an extra thrill to the already electric atmosphere of the tavern. In this bustling hub of activity, the vibrant tapestry of life unfolds, where adventurers, mystics, champions, rogues, and more converge in pursuit of excitement and respite.""" + Style.RESET_ALL

typewriter_whole(text_whole, 0.01)

pirate_intro_1 = Fore.RED + "\n\n\"Another scallywag has decided to challenge me, eh?\"\n\"So be it, I will see better use for your gold\"\n\"Please, allow me to hear your name\"" + Style.RESET_ALL

typewriter_whole(pirate_intro_1, 0.05)

name = input("\n\n>>> ")

pirate_intro_2 = Fore.RED + "\n\"" + name + "..." + " " + "A fine name for a fine warrior.\"" + Style.RESET_ALL

pirate_intro_3 = Fore.RED + "\n\"Now," + " " + name + "," + " " + "shall we get started?\"\n\n" + Style.RESET_ALL

typewriter_whole(pirate_intro_2, 0.05)

typewriter_whole(pirate_intro_3, 0.05)

# input: print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# output: ● ┌ ─ ┐ │ └ ┘

# Dice frame:
# 
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: (Fore.GREEN + "┌─────────┐", 
                     "│         │", 
                     "│    ●    │", 
                     "│         │", 
        Fore.GREEN + "└─────────┘" + Style.RESET_ALL),
    2: (Fore.GREEN + "┌─────────┐", 
                     "│ ●       │", 
                     "│         │", 
                     "│       ● │", 
        Fore.GREEN + "└─────────┘" + Style.RESET_ALL),
    3: (Fore.GREEN + "┌─────────┐", 
                     "│ ●       │", 
                     "│    ●    │", 
                     "│       ● │", 
        Fore.GREEN + "└─────────┘" + Style.RESET_ALL),
    4: (Fore.GREEN + "┌─────────┐", 
                     "│ ●     ● │", 
                     "│         │", 
                     "│ ●     ● │", 
        Fore.GREEN + "└─────────┘" + Style.RESET_ALL),
    5: (Fore.GREEN + "┌─────────┐", 
                     "│ ●     ● │", 
                     "│    ●    │", 
                     "│ ●     ● │", 
        Fore.GREEN + "└─────────┘" + Style.RESET_ALL),
    6: (Fore.GREEN + "┌─────────┐", 
                     "│ ●     ● │", 
                     "│ ●     ● │", 
                     "│ ●     ● │", 
        Fore.GREEN + "└─────────┘" + Style.RESET_ALL)
}

player_score = 0
pirate_score = 0

pirate_win = [Fore.RED + "\"Seems like this win is mine\"" + Style.RESET_ALL,
              Fore.RED + "\"Heh! Another win for me!\"" + Style.RESET_ALL,
              Fore.RED + "\"I'll be taking yer' gold!\"" + Style.RESET_ALL,
              Fore.RED + "\"A win for me\"" + Style.RESET_ALL]
pirate_lose = [Fore.RED + "\"Drats! This win is yours...\"" + Style.RESET_ALL,
               Fore.RED + "\"AAARRRRR!!! I lose!\"" + Style.RESET_ALL,
               Fore.RED + "\"Ah, you win this time\"" + Style.RESET_ALL,
               Fore.RED + "\"Heh, beginner's luck\"" + Style.RESET_ALL]

dice_choose = "Choose the amount of dice you would like to play with:"
typewriter_whole(dice_choose, 0.05)

num_of_dice = int(input("\n\n>>> "))

coin_start = Fore.YELLOW + "\nYou currently have 50 coins" + Style.RESET_ALL
typewriter_whole(coin_start, 0.05)

# num_of_dice = int(input("Choose the amount of dice you would like to play with:\n\n>>> "))
# time.sleep(1)

roll_again = "yes"

coins = 50

while roll_again == "yes" or roll_again == "Y" or roll_again == "Yes" or roll_again == "YES" or roll_again == "y":

    dice = []
    dice_2 = []
    total = 0
    total_2 = 0
    # coins = 50

    coin_bet = "\n\nChoose the amount of coins you would like to bet:"
    typewriter_whole(coin_bet, 0.05)

    bet = int(input("\n\n>>> "))
    # test = bet

    for die in range(num_of_dice):
      dice.append(random.randint(1, 6))

    for die in range(num_of_dice):
      dice_2.append(random.randint(1, 6))

    rolling = "\nRolling...\n\n"

    typewriter_whole(rolling, 0.05)
    time.sleep(1)

    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()
        time.sleep(0.25)

    for die in dice:
        total += die

    time.sleep(1)
    typewriter_whole(Fore.GREEN + "Total:" + " " + str(total) + Style.RESET_ALL, 0.1)

    pirate_play_1 = Fore.RED + "\n\n\"So you rolled a " + str(total) + ", eh?\"" + Style.RESET_ALL

    typewriter_whole(pirate_play_1, 0.05)

    pirate_play_2 = Fore.RED + "\n\"My turn!\"\n" + Style.RESET_ALL

    typewriter_whole(pirate_play_2, 0.05)

    typewriter_whole(rolling, 0.05)
    time.sleep(1)

    for line in range(5):
        for die in dice_2:
            print(dice_art.get(die)[line], end="")
        print()
        time.sleep(0.25)

    for die in dice_2:
        total_2 += die

    typewriter_whole(Fore.GREEN + "Total:" + " " + str(total_2) + Style.RESET_ALL, 0.1)

# Player win:
    if total > total_2:
        player_score += 1
        coins += (bet * 2)
        # coins += test
        typewriter_whole("\n\n" + random.choice(pirate_lose), 0.05)
        typewriter_whole(Fore.YELLOW + "\n\n" + "+" + " " + str(bet * 2) + " " + "coins!" + Style.RESET_ALL, 0.05)
        # "+ x gold"
        # "Gold: x"


# Pirate Win:
    elif total_2 > total:
        pirate_score += 1
        coins -= bet
        # coins -= test
        typewriter_whole("\n\n" + random.choice(pirate_win), 0.05)
        typewriter_whole(Fore.YELLOW + "\n\n" + "-" + " " + str(bet) + " " + "coins..." + Style.RESET_ALL, 0.05)


    else:
        typewriter_whole("\nDraw", 0.1)

    typewriter_whole("\n\nPlayer score:" + " " + str(player_score), 0.05)
    time.sleep(0.25)
    typewriter_whole("\nPirate score:" + " " + str(pirate_score), 0.05)

##############
    coin_count = Fore.YELLOW + "\n\nCoins: " + str(coins) + Style.RESET_ALL
    typewriter_whole(coin_count, 0.05)
##############

    if coins <= 0:
        typewriter_whole("\n\nYou have no more coins left...", 0.05)
        time.sleep(0.5)
        typewriter_whole("\n\nYou lost!", 0.05)
        time.sleep(0.5)
        typewriter_whole("\n\nEnding game...", 0.1)
        sys.exit()

    play_again = Fore.RED + "\n\n\"Let's play again?\" (Y/N)" +Style.RESET_ALL
    typewriter_whole(play_again, 0.05)
    
    roll_again = input("\n\n>>> ")
    # roll_again = input("\nPlay again? (Y/N)\n\n>>> ")


# Todo: Add replayability feature (done)
#       Fix "Choose the amount of dice you would like to play with:" typewriter effect (done)
#       Add currency system (99% done)
#       Add betting feature (99% done)
#       Pirate ASCII (this is hard to do lol)
#       Dice rolling animation (semi // idk how to improve it)
#       Coloured text (doing now // i'm having trouble // i think i fixed it // i fixed it)
#       Clean up code
#       Improve code efficiency

# if bet < 0 or > coins:
#    print("invalid")

#test 1
#test 2