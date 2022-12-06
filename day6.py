#!/usr/bin/env python3


from time import perf_counter

time_start = perf_counter()

# test data is a string followed by the expected locations of the header and message start

test_data = """mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 7 19
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5 23
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6 23
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10 29
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11 26"""


##########################################################################


def find_headers(s_rcvd, h_len):
    h_lst = []
    for idx in range(len(s_rcvd)-h_len):
        t = s_rcvd[idx:idx+h_len]   # slice off each sequence of header len characters
        if len(set(t)) == h_len:    # if a set made with the slice is as long as the slice
            h_lst += [[idx+h_len, t]]  # then the slice is made up of unique characters
    return h_lst


# ----------------------------------------------------------
print(f'%s'%('*'*40))

for idx, s_test in enumerate(test_data.split('\n')):
    s_lst = s_test.split(':')
    if len(s_lst) == 2:
        h_lst = find_headers(s_lst[0], 4)
        expected = int(s_lst[-1].split()[-2])
        print(f'test {idx} found header at {h_lst[0][0]}, expected {expected}')


# input the data file
with open('day6data.txt') as in_file:
    in_str = in_file.read()
h_lst = find_headers(in_str, 4)
print(f'real data found header at {h_lst[0][0]}')

print(f'%s'%('='*40))

for idx, s_test in enumerate(test_data.split('\n')):
    s_lst = s_test.split(':')
    if len(s_lst) == 2:
        h_lst = find_headers(s_lst[0], 14)
        expected = int(s_lst[-1].split()[-1])
        print(f'test {idx} found message start at {h_lst[0][0]}, expected {expected}')


# input the data file
with open('day6data.txt') as in_file:
    in_str = in_file.read()
h_lst = find_headers(in_str, 14)
print(f'real data found message start at {h_lst[0][0]}')


time_end = perf_counter()
print(f'done in {(time_end-time_start)*1e3:.3f} milli-seconds')
"""
****************************************
test 0 found header at 7, expected 7
test 1 found header at 5, expected 5
test 2 found header at 6, expected 6
test 3 found header at 10, expected 10
test 4 found header at 11, expected 11
real data found header at 1356
========================================
test 0 found message start at 19, expected 19
test 1 found message start at 23, expected 23
test 2 found message start at 23, expected 23
test 3 found message start at 29, expected 29
test 4 found message start at 26, expected 26
real data found message start at 2564
done in 17.482 milli-seconds
"""
