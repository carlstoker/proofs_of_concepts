#!/usr/bin/env python3
"""Rock, Paper, Scissors, Spock, Lizard"""
import random


class RockPaperScissors:
    hands = []
    players = {}

    def __init__(self, **kwargs):
        if 'hands' in kwargs:
            self.hands = kwargs['hands']
        else:
            self.hands = [
                {'name': 'Rock', 'beats': {'Scissors': 'crushes', 'Lizard': 'crushes'}},
                {'name': 'Paper', 'beats': {'Rock': 'covers', 'Spock': 'disproves'}},
                {'name': 'Scissors', 'beats': {'Paper': 'cuts', 'Lizard': 'decapitates'}},
                {'name': 'Spock', 'beats': {'Scissors': 'smashes', 'Rock': 'vaporizes'}},
                {'name': 'Lizard', 'beats': {'Spock': 'poisons', 'Paper': 'eats'}}
            ]
        if 'players' in kwargs:
            self.players = kwargs['players']
        else:
            self.players = {
                0: {'name': 'Player 1', 'move': 0},
                1: {'name': 'Computer', 'move': 0}
            }

    def evaluate_result(self):
        mod = ((self.players[0]['move'] - self.players[1]['move']) + len(self.hands)) % len(self.hands)

        if mod == 0:        # Tie
            return 0
        elif mod % 2 > 0:   # Player 1 wins
            return 1
        else:               # Player 2 wins
            return 2

    def print_result(self):
        result = self.evaluate_result()

        moves = self.move_names()
        if result == 0:
            print('Tie. Both players chose {}.'.format(moves[self.players[0]['move']]))
        else:
            winner = result - 1
            loser = (winner - 1) % 2
            winning_move = moves[self.players[winner]['move']]
            losing_move = moves[self.players[loser]['move']]
            winning_action = self.hands[self.players[winner]['move']]['beats'][losing_move]

            print('{} wins! {} {} {}.'.format(
                self.players[winner]['name'],
                winning_move,
                winning_action,
                losing_move
            ))

    def move_names(self):
        return [x['name'] for x in self.hands]

    def move_prompt(self, player_num):
        player_move = None
        moves = self.move_names()

        while player_move not in moves:
            player_move = input('{}? '.format(', '.join(moves)))

        self.players[player_num]['move'] = moves.index(player_move)
        return None

    def move_random(self, player_num):
        self.players[player_num]['move'] = random.randint(0, len(self.hands) - 1)

    def move_set(self, player_num, move_num):
        self.players[player_num]['move'] = move_num


def main():
    rps = RockPaperScissors()
    rps.move_prompt(0)
    rps.move_random(1)
    rps.print_result()
    return None


def test_cases():
    rps = RockPaperScissors()

    for p1 in range(0, len(rps.hands)):
        rps.move_set(0, p1)
        for p2 in range(0, len(rps.hands)):
            rps.move_set(1, p2)
            rps.print_result()


if __name__ == '__main__':
    main()
