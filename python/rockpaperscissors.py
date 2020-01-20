#!/usr/bin/env python3
"""Rock, Paper, Scissors"""
from random import choice

# Dict defining winning hands
hands = {
    'Rock': {'Scissors': 'crushes', 'Lizard': 'crushes'},
    'Paper': {'Rock': 'covers', 'Spock': 'disproves'},
    'Scissors': {'Paper': 'cuts', 'Lizard': 'decapitates'},
    'Lizard': {'Spock': 'poisons', 'Paper': 'eats'},
    'Spock': {'Scissors': 'smashes', 'Rock': 'vaporizes'}
}

# Player input for hand selection
while True:
    player = input('{}? '.format(', '.join(hands.keys())))
    if player in hands.keys():
        break

# Pseudorandomize hand selection for CPU
computer = choice(list(hands.keys()))

# Result calculation and output
if player == computer:
    print('You tied!')
elif computer in hands[player]:
    print('You win! {} {} {}.'.format(player, hands[player][computer], computer))
else:
    print('You lose! {} {} {}.'.format(computer, hands[computer][player], player))
