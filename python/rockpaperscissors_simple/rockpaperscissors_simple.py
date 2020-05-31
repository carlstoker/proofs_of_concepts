#!/usr/bin/env python3
import random
hands = ['rock', 'paper', 'scissors']

p1 = None
while p1 not in hands:
    p1 = input('{}? '.format(', '.join(hands))).lower()
p1 = hands.index(p1)

p2 = random.randint(0, len(hands) - 1)

result = ((p1 - p2) + len(hands)) % len(hands)
if result == 0:
    print('Tie!')
elif result == 1:
    print('You win! {} beats {}.'.format(hands[p1], hands[p2]))
else:
    print('You lose! {} beats {}.'.format(hands[p2], hands[p1]))