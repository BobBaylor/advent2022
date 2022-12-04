#!/usr/bin/env python3

""" data input file looks like:
14-28,13-28
72-81,82-91
4-4,6-95
47-49,48-59
26-36,37-76
2-99,98-99
26-36,19-35

...

each line has two pairs. Each pair denotes a range of numbers.
Q1: How many pairs have one range enclosing the other range?
Q2: How many pairs have one range that overlaps the other range?
"""
from time import perf_counter

time_start = perf_counter()

def get_pair(row, idx):
    # return a pair of runs
    row = row.strip()
    both = row.split(',')
    pairs = []
    for x in both:
        y = x.split('-')
        pairs += [[int(y[0]), int(y[1])]]
    return pairs

def is_enclosed(p, idx):
    # return true if one enclosesthe other
    # idx for debugging
    if (min(p[0]) <= min(p[1])) and (max(p[0]) >= max(p[1])):
        return True
    if (min(p[1]) <= min(p[0])) and (max(p[1]) >= max(p[0])):
        return True
    return False

def is_overlap(p, idx):
    # return true if one overlaps the other
    # idx for debugging
    if (min(p[0]) <= max(p[1])) and (max(p[0]) >= min(p[1])):
        return True
#    if (min(p[1]) <= max(p[0])) and (max(p[1]) >= min(p[0])):
#        return True
    return False


def show(g):
    # simple print of a pair
    # print()
    print(g)


##########################################################################
# input the data file
with open('day4data.txt') as in_file:
    in_lines = in_file.readlines()
print(f'%s\nline count {len(in_lines)}'%('*'*40))

pairs = [get_pair(row, idx) for idx, row in enumerate(in_lines)]
print(f'pair count is {len(pairs)}')

for p in pairs[:5]:
    show(p)
encl = [[p, idx] for idx, p in enumerate(pairs) if is_enclosed(p, idx)]
print(f'enclosed count is {len(encl)}')

encl_not = [[p, idx] for idx, p in enumerate(pairs) if not is_enclosed(p, idx)]
print(f'not count is {len(encl_not)}')

print('enclosed')
for p in encl[:3]:
    show(p)
print('not enclosed')
for p in encl_not[:3]:
    show(p)
print('='*30)
lap = [[p, idx] for idx, p in enumerate(pairs) if is_overlap(p, idx)]
print(f'overlap count is {len(lap)}')

lap_not = [[p, idx] for idx, p in enumerate(pairs) if not is_overlap(p, idx)]
print(f'not count is {len(lap_not)}')
print('overlapped')
for p in lap[:3]:
    show(p)
print('not overlapped')
for p in lap_not[:3]:
    show(p)

time_end = perf_counter()
print(f'done in {(time_end-time_start)*1e3:.3f} milli-seconds')

"""
****************************************
line count 1000
pair count is 1000
[[14, 28], [13, 28]]
[[72, 81], [82, 91]]
[[4, 4], [6, 95]]
[[47, 49], [48, 59]]
[[26, 36], [37, 76]]
enclosed count is 305
not count is 695
enclosed
[[[14, 28], [13, 28]], 0]
[[[2, 99], [98, 99]], 5]
[[[18, 18], [18, 55]], 17]
not enclosed
[[[72, 81], [82, 91]], 1]
[[[4, 4], [6, 95]], 2]
[[[47, 49], [48, 59]], 3]
==============================
overlap count is 811
not count is 189
overlapped
[[[14, 28], [13, 28]], 0]
[[[47, 49], [48, 59]], 3]
[[[2, 99], [98, 99]], 5]
not overlapped
[[[72, 81], [82, 91]], 1]
[[[4, 4], [6, 95]], 2]
[[[26, 36], [37, 76]], 4]
done in 10.432 milli-seconds
"""
