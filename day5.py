#!/usr/bin/env python3

""" data input file looks like:
                [B]     [L]     [S]
        [Q] [J] [C]     [W]     [F]
    [F] [T] [B] [D]     [P]     [P]
    [S] [J] [Z] [T]     [B] [C] [H]
    [L] [H] [H] [Z] [G] [Z] [G] [R]
[R] [H] [D] [R] [F] [C] [V] [Q] [T]
[C] [J] [M] [G] [P] [H] [N] [J] [D]
[H] [B] [R] [S] [R] [T] [S] [R] [L]
 1   2   3   4   5   6   7   8   9

move 8 from 7 to 1
move 9 from 1 to 9
move 4 from 5 to 4
move 4 from 6 to 1
move 3 from 8 to 5
move 6 from 5 to 9

...

first section of data represents stacks of items
second set of lines are movements from stack to stack.
    Items are moved, one at a time so the fist move
move 8 from 7 to 1
will result in stack1 having [L] on top and [S] in the 4th position from the bottom


Q1: What crates will be on top. Starting tops are RFQJBGLCS
Q2: again but move crates together (not flipping order) instead of as single crates
"""
from time import perf_counter

time_start = perf_counter()

def get_stacks(row, idx, stacks):
    # initialize stacks, a line at a time
    # return False when we hit a blank line, else True
    if '[' in row:  # we're still building
        r = row.ljust(36, ' ')
        for idx, c in enumerate(r[1::4]):
            if c == ' ':
                continue    # no crate
            stacks[idx] += [c]
        return True
    if row.strip():
        return True                     # line of stack numbers - ignore

    return False                        # and we're done with init


def move_stacks(row, idx, stacks, b_singles):
    # move crates, a line at a time
    if not 'move' in row:
        print(f'missing move at line {idx+1}')
    else:
        # move 8 from 7 to 1
        toks = row.split()
        if len(toks) < 6:
            print(f'short input at line {idx+1}')
        if 'from' not in toks[2]:
            print(f'missing from at line {idx+1}')
        if 'to' not in toks[4]:
            print(f'missing to at line {idx+1}')
        s_count = int(toks[1])
        s_from = int(toks[3])
        s_to = int(toks[5])
        if s_count > len(stacks[s_from]):
            print(f'not enough crates at line {idx+1}: {row}, stacks[s_from]')
        m = stacks[s_from][-s_count:]             # pick up the crates
        stacks[s_from] = stacks[s_from][:-s_count] # remove from from stack
        if b_singles:
            stacks[s_to] += m[::-1]     # deposit on to to stack
        else:
            stacks[s_to] += m[::]     # deposit on to to stack


def show(stks, idx):
    # simple print of a stack
    # print()
    s = '%2d '%idx
    s = s + ''.join([v for v in stks[idx]])
    return s

def show_all(stks):
    s = '\n'.join([show(stks, i) for i in range(1,len(stks))])
    return s


##########################################################################
# input the data file
def main(b_singles):
    with open('day5data.txt') as in_file:
        in_lines = in_file.readlines()
    # print(f'%s\nline count {len(in_lines)}'%('*'*40))

    stacks = [[] for i in range(9)]    # numbers are off by one...
    b_init = True
    for idx, row in enumerate(in_lines):
        if b_init:
            b_init = get_stacks(row, idx, stacks)
            if not b_init:
                # blank line - insert one stack so I can use zero-based index instead of '1'
                stacks = [['?']] + stacks
                # also, we've added to the stacks from the tops down so flip them now
                stacks = [s[::-1] for s in stacks]  # flip all the stacks right side up
                if b_singles:
                    all_s = show_all(stacks)
                    print(f'start conditions:\n{all_s}')
        else:
            move_stacks(row, idx, stacks, b_singles)

    all_s = show_all(stacks)
    print(f'\nend conditions for %s moves:\n{all_s}'%('single' if b_singles else 'multi'))
    ans_pad = [x[-1] if x else ' ' for x in stacks[1:]]
    ans = ''.join(ans_pad)
    print(f'%s answer: {ans}'%('single' if b_singles else 'multi'))


main(True)     # move crates one at a time
print(f'%s'%('='*40))
main(False)    # move crates all at once (no flipping order)


time_end = perf_counter()
print(f'done in {(time_end-time_start)*1e3:.3f} milli-seconds')

"""
start conditions:
 1 HCR
 2 BJHLSF
 3 RMDHJTQ
 4 SGRHZBJ
 5 RPFZTDCB
 6 THCG
 7 SNVZBPWL
 8 RJQGC
 9 LDTRHPFS

end conditions for single moves:
 1 MVQFHGTCHFS
 2 RJBZPCH
 3 JRDZDQ
 4 W
 5 JGS
 6 R
 7 TB
 8 BPFRBHHSCHCNZPGLLRSJTRTD
 9 L
single answer: SHQWSRBDL
========================================

end conditions for multi moves:
 1 SDMHRTJTBQC
 2 BPTNCZD
 3 SRHRWT
 4 Q
 5 FZZ
 6 H
 7 GB
 8 GGBLHCJCPJDLHRLSVFHJPFRR
 9 S
multi answer: CDTQZHBRS
done in 6.523 milli-seconds"""
