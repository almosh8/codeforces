import datetime as dt
import sys
import os
from random import randrange

if os.getenv('LOCAL') == '1':
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')


def scan_str():
    if os.getenv('LOCAL') == '1':
        return input_file.readline()
    else:
        print('\n')
        x = input()
        return x


def scan_strs_list():
    str = scan_str()
    strs = str.split()

    str = strs[0]

    return strs

def scan_chars_list():
    str = scan_str()
    return list(str)

def scan():
    strs = scan_strs_list()
    str = strs[0]
    #print(strs[0])
    return int(str)

def scan_list():
    strs = scan_strs_list()
    return [int(x) for x in strs]


def output_one(x):
    if os.getenv('LOCAL') == '1':
        output_file.write(str(x) + '\n')
    else:
        print(x)


def output(x):
    if isinstance(x, list):
        for i in x:
            output(i)
    else:
        output_one(x)

PRESENT = 'present'
CORRECT = 'correct'
ABSENT = 'absent'

s = list(scan_str())
q = list(scan_str())
present = {}

for c in s:
    present[c] = 1

for i, c in enumerate(q):
    if s[i] == c:
        output(CORRECT)
    elif c in present:
        output(PRESENT)
    else:
        output(ABSENT)