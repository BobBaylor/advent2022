#!/usr/bin/env python3

""" data input file looks like:
11334
6264
9318

1209
4404
3988
5816
3890
4990
2796
4199
5439
4249
2938
1120
2612

1755
12840
6995
1547
13621
3701
...

that's just the first three elves

Question 1: how many calories (sum of an elf) does the fattest elf have?

Question 2: what's the sum of ccalories of the 3 fattest elves?

"""
from time import perf_counter
time_start = perf_counter()

def elf_str(elf):
    """ elf_str(): contsruct a string representing one elf
    """
    str_lst = [f'elf {elf[1]+1} with {elf[0]} calories']
    str_lst += [f' ending on line {elf[2]}']
    str_lst += [f'            had {elf[3]}']
    str_lst += ['']
    return '\n'.join(str_lst)

# input the data file
with open('day1data.txt') as in_file:
    in_lines = in_file.readlines()

print(f'%s\nfound {len(in_lines)} lines'%('*'*40))

elves = []  # each entry will be a list of:
            #       sum, elf_id, line number, list of calories

cal = []     # elf calorie list
elf_id = 0   # elf counter
# I keep the calorie list as a debugging aid

# first question asked for the fattest elf so we capture that with _most vars
# second question asked for sum of top 3 elves so _most vars are superfluous and we must resort to sorting
cal_most = -1
elf_most = -1

# loop through the lines, contructing elves and tracking the fattest one found, so far
# handles some types of bad input:
#   empty lines separate elves but more than one empty line should not save an empty elf
#   lines that don't have an int on them should be flagged but ignored
for idx, line in enumerate(in_lines):
    line = line.strip()
    # a non-empty line has a calorie number to save to cal[]
    if line:
        try:
            cal += [int(line)]
        except ValueError:
            print(f'INPUT ERROR: non-int found on line {idx+1}')
    # an empty line marks the end of an elf so save it to elves[]
    else:
        if cal:     # ignore multiple empty lines
            elves += [[sum(cal), elf_id, idx+1, cal]]
            if elves[-1][0] > cal_most:
                cal_most = elves[-1][0]
                elf_most = elf_id
            elf_id = elf_id + 1
            cal = []

print(f'found {len(elves)} elves. elf_most = {elf_most}')

# print(f'\nfirst elve is {elf_str(elves[0])}')
print(f'fattest elve is elf number {elf_str(elves[elf_most])}')

elf_sort = sorted(elves,key= lambda x: x[0])

if False:
    str1 = "\n".join(f'{elf_str(e)}' for e in elf_sort[:3])
    str2 = "\n".join(f'{elf_str(e)}' for e in elf_sort[-3:])
    print(f'*********** skinniest elves: ********\n{str1}')
    print(f'*********** fattest elves: ********\n{str2}')

three_sum = sum([e[0] for e in elf_sort[-3:]])
print(f'sum of the top 3 elves is {three_sum}')

time_end = perf_counter()
print(f'done in {(time_end-time_start)*1e3:.3f} milli-seconds')

"""
****************************************
found 2265 lines
found 263 elves. elf_most = 34
fattest elve is elf number elf 35 with 66186 calories
 ending on line 325
            had [3949, 4571, 5785, 5968, 2506, 4511, 5234, 6501, 5448, 4961, 2762, 3742, 6426, 3822]

sum of the top 3 elves is 196804
done in 1.611 milli-seconds

"""
