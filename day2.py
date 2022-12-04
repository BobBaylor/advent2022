#!/usr/bin/env python3

""" data input file looks like:
C X
C X
C X
A Z
C X
C X
A Y
B X
B Y
B Z
C Y
C X
C X
...

for a total of 2466 lines

Question 1: what's my score if I follow the strategy guide

Question 2:
    The Elf finishes helping with the tent and sneaks back over to you.
    "Anyway, the second column says how the round needs to end:
        X means you need to lose,
        Y means you need to end the round in a draw, and
        Z means you need to win. Good luck!"

    The total score is still calculated in the same way,
    but now you need to figure out what shape to choose so the round ends as indicated.
    The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
    Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

    Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
"""
from time import perf_counter

time_start = perf_counter()

def play(in_line, idx):
    """
    A for Rock, B for Paper, and C for Scissors.
    The second column, is your play:
        A for Rock, B for Paper, and C for Scissors.
    The score for a single round is the score for the shape you selected
        (1 for Rock, 2 for Paper, and 3 for Scissors) plus
        the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    """
    line = in_line.strip().upper()
    shape_score = {'A': 1, 'B': 2, 'C': 3}
    outcome_score = {
        'A': {'A': 3, 'B': 0, 'C': 6},
        'B': {'A': 6, 'B': 3, 'C': 0},
        'C': {'A': 0, 'B': 6, 'C': 3},
        }
    try:
        elf = line[0]
        me = line[2]
    except IndexError:
        print(f'ERROR bad line <{in_line}> at location {idx + 1}')
    try:
        score = shape_score[me] + outcome_score[me][elf]
    except KeyError:
        print(f'ERROR bad line <{in_line}> at location {idx + 1}')

    return score



def score_wrong(in_line, idx):
    """
    A for Rock, B for Paper, and C for Scissors.
    The second column, you reason, must be what you should play in response:
        X for Rock, Y for Paper, and Z for Scissors.

    The score for a single round is the score for the shape you selected
        (1 for Rock, 2 for Paper, and 3 for Scissors) plus
        the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    # shape_score = {'X': 1, 'Y': 2, 'Z': 3}
    outcome_score = {
        'X': {'A': 3, 'B': 0, 'C': 6},
        'Y': {'A': 6, 'B': 3, 'C': 0},
        'Z': {'A': 0, 'B': 6, 'C': 3},
        }
    """
    line = in_line.strip().upper()
    shape_score = {'X': 1, 'Y': 2, 'Z': 3}
    outcome_score = {
        'X': {'A': 3, 'B': 0, 'C': 6},
        'Y': {'A': 6, 'B': 3, 'C': 0},
        'Z': {'A': 0, 'B': 6, 'C': 3},
        }
    try:
        elf = line[0]
        me = line[2]
    except IndexError:
        print(f'ERROR bad line <{in_line}> at location {idx + 1}')
    try:
        score = shape_score[me] + outcome_score[me][elf]
    except KeyError:
        print(f'ERROR bad line <{in_line}> at location {idx + 1}')
    return score


def cheat(in_line, idx):
    """
    A for Rock, B for Paper, and C for Scissors.
    The second column, you reason, must be what you should play in response:
        X for LOSE, Y for DRAW, and Z for WIN.

    The score for a single round is the score for the shape you selected
        (1 for Rock, 2 for Paper, and 3 for Scissors) plus
        the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    """
    line = in_line.strip().upper()
    cheat_play = {
        'A': {'X': 'C', 'Y': 'A', 'Z': 'B'},
        'B': {'X': 'A', 'Y': 'B', 'Z': 'C'},
        'C': {'X': 'B', 'Y': 'C', 'Z': 'A'},
        }
    try:
        elf = line[0]
        command = line[2]
    except IndexError:
        print(f'ERROR bad line <{in_line}> at location {idx + 1}')
    try:
        my_play = cheat_play[elf][command]
    except KeyError:
        print(f'ERROR bad line <{in_line}> at location {idx + 1}')
    return ' '.join([elf, my_play])

##########################################################################
# input the data file
with open('day2data.txt') as in_file:
    in_lines = in_file.readlines()

print(f'%s\nfound {len(in_lines)} lines'%('*'*40))
# second question: transform the list to a play list and play it

wrong_lines = [score_wrong(x, idx) for idx, x in enumerate(in_lines)]
print(f'found {len(wrong_lines)} (wrong) games')

cheat_lines = [cheat(x, idx) for idx, x in enumerate(in_lines)]

scores = [play(x, idx) for idx, x in enumerate(cheat_lines)]

print(f'found {len(scores)} games')

total_wrong = sum(wrong_lines)
print(f'sum of wrong scores is {total_wrong}')
total_score = sum(scores)
print(f'sum of scores is {total_score}')

time_end = perf_counter()
print(f'done in {(time_end-time_start)*1e3:.3f} milli-seconds')
"""
****************************************
found 2500 lines
found 2500 (wrong) games
found 2500 games
sum of wrong scores is 14069
sum of scores is 12411
done in 6.863 milli-seconds
"""

