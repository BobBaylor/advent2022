#!/usr/bin/env python3

""" data input file looks like:
mmbclcsDHCflDDlCrzzrDWjPJvjPvqJPjfpqZQdfWd
NNFLnFRNhgNQtMLSFSgwSwGJPZWLPvjpjjJGZJPvWPvJ
BnwFNgVVhwNwVQrmzbrrCHVTmDsm
CTsVssjPTWPbzhfbfqqpbqJq
RRttdQlRdnNpdmwBnBDhFrGrqDGBqJJfJD
...

each letter denotes an item-type
Q1: each line is sack. Each sack has 2 halves.
    Each sack has one item-type in both halves.
    The letter indicates a "score" for the item.
    Find the dup-ed item in each sack and add up the scores over all the sacks.
Q2: each group of 3 lines is an elf group.
    each sack in a group shares a single common item: its ID.
    Add up all the IDs.
"""
from time import perf_counter

time_start = perf_counter()

def get_bags(row):
    # check that two sides of bag are equal count
    row = row.strip()
    half_len = len(row)//2
    strs = [row[:half_len], row[half_len:]]
    assert len(strs[0]) == len(strs[1])
    assert half_len > 0
    bag_sets = [set(strs[0]), set(strs[1])]
    return bag_sets

def prior(s, idx):
    # return the score of a letter in s
    # idx for debugging
    if len(s) != 1:
        print(f'bad len at line {idx+1}: <{s}>')
    if s.islower():
        p = 1 + ord(s) - ord('a')
    else:
        p = 27 + ord(s) - ord('A') 
    return p


def show(g):
    # simple print of a group
    print()
    print(g[0])
    print(g[1])
    print(g[2])

##########################################################################
# input the data file
with open('day3data.txt') as in_file:
    in_lines = in_file.readlines()
print(f'%s\nline count {len(in_lines)}'%('*'*40))

bags = [get_bags(row) for row in in_lines]
print(f'bags len {len(bags)}')

dups = [x[0] & x[1] for x in bags]
print(f'dups len {len(dups)}')

priors = [prior(list(x)[0], idx) for idx, x in enumerate(dups)]
print(f'priority len {len(priors)}')
print(f'sum of priorities {sum(priors)}')

print('-'*30)  # second question ----------

xx = [x.strip() for x in in_lines]
groups = [[xx[i], xx[i+1], xx[i+2]] for i in range(0,len(xx),3)]
groups = list(groups)
print(f'groups len {len(groups)}')
for g in groups[:3]:
    show(g)

commons = [set(x[0]) & set(x[1]) & set(x[2]) for x in groups]
print(f'commons[:10] {commons[:10]}')

badges = [prior(list(g)[0], idx) for idx, g in enumerate(commons)]
print(f'badges[:10] {badges[:10]}')
print(f'sum of badges {sum(badges)}')

time_end = perf_counter()
print(f'done in {(time_end-time_start)*1e3:.3f} milli-seconds')

"""
****************************************
line count 300
bags len 300
dups len 300
priority len 300
sum of priorities 8088
------------------------------
groups len 100

mmbclcsDHCflDDlCrzzrDWjPJvjPvqJPjfpqZQdfWd
NNFLnFRNhgNQtMLSFSgwSwGJPZWLPvjpjjJGZJPvWPvJ
BnwFNgVVhwNwVQrmzbrrCHVTmDsm

CTsVssjPTWPbzhfbfqqpbqJq
RRttdQlRdnNpdmwBnBDhFrGrqDGBqJJfJD
HttgcggdNwQtgcpTsvjVPTcssjsv

bWrpnrpPcFNbfPtwVPddVVDw
jLgqqJgjZLhHjRqLHLjqHgftpmJVtTmwQmtGddwwDVJm
HhzgshZLpHLjqhLLZRZpLRbbrlBNsrrNsFWcCvvFCcNN
commons[:10] [{'Q'}, {'p'}, {'p'}, {'c'}, {'M'}, {'f'}, {'s'}, {'V'}, {'N'}, {'N'}]
badges[:10] [43, 16, 16, 3, 39, 6, 19, 48, 40, 40]
sum of badges 2522
done in 2.482 milli-seconds
"""
