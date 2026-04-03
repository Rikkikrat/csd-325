"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game

Modified by: Rikki Kratochvil
Assignment: Module 3 Cho-Han Update
Purpose: Update prompts, house fee, and bonus rule.
"""

import random
import sys

JAPANESE_NUMBERS = {
    1: 'ICHI',
    2: 'NI',
    3: 'SAN',
    4: 'SHI',
    5: 'GO',
    6: 'ROKU'
}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total is an even (cho) or odd (han) number.

Bonus Notice:
If the total of the dice is 2 or 7, you receive a 10 mon bonus.
''')

purse = 5000

while True:  # Main game loop.
    # Ask the player to place a bet.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')

    while True:
        # Changed input prompt to initials.
        pot = input('rk: ')

        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player choose CHO or HAN.
    while True:
        # Changed input prompt to initials.
        bet = input('rk: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results.
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Calculate the total of the dice.
    totalRoll = dice1 + dice2

    # Added bonus rule for a total of 2 or 7.
    if totalRoll == 2 or totalRoll == 7:
        print('The total roll was', totalRoll, '- you got a 10 mon bonus!')
        purse = purse + 10

    # Determine whether the total is even or odd.
    rollIsEven = (totalRoll % 2 == 0)
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = (bet == correctBet)

    # Display results and update purse.
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot

        # Changed house fee from 10% to 12%.
        houseFee = int(pot * 0.12)
        print('The house collects a', houseFee, 'mon fee.')
        purse = purse - houseFee
    else:
        purse = purse - pot
        print('You lost!')

    # Check whether the player has any money left.
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        break