#!/usr/bin/env python3
from random import choice

#Dict defining hands
hands = {
    'Rock': {'Scissors': 'crushes', 'Lizard': 'crushes'},
    'Paper': {'Rock': 'covers', 'Spock': 'disproves'},
    'Scissors': {'Paper': 'cuts', 'Lizard': 'decapitates'},
    'Lizard': {'Spock': 'poisons', 'Paper': 'eats'},
    'Spock': {'Scissors': 'smashes', 'Rock': 'vaporizes'}
}

#Player input for hand selection
player = None
while player is None:
    player = input('{}? '.format(', '.join(hands.keys())))
    if player not in hands.keys():
        player = None

#Pseudorandomize hand selection for CPU
computer = choice(list(hands.keys()))

#Result calculation and output
if player == computer:
    print('You tied!')
elif computer in hands[player]:
    print('You win! {} {} {}.'.format(player, hands[player][computer], computer))
else:
    print('You lose! {} {} {}.'.format(computer, hands[computer][player], player))
