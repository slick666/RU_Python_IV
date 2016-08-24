#!/usr/bin/env python
# *-* coding:utf-8 *-*

"""

:mod:`lab_subprocess` -- subprocess module
============================================

LAB subprocess Learning Objective: Familiarization with subprocess

::

 a. Use the subprocess call function to run "ls -l" and print the output.

 b. Do the same as a), but suppress stdout.

 c. Do the same as a), but run the command "/bogus/command". What happens?



 e. Use subprocess Popen to run "du -h" and output stdout to a pipe. Read the pipe
    and print the output.

 f. Create a new function commander() which takes any number of commands to execute
    (as strings) on the arg list, then runs them sequentially printing stdout.

"""

from os import devnull
from subprocess import check_output, Popen, PIPE


def commander(*args):
    return check_output(args=args)


def main():

    COMMAND = ['ls', '-l']
    BOGUS_COMMAND = ['bogus']

    # Part a
    print("PART A")
    print(check_output(COMMAND))
    print

    # Part b
    print("PART B")
    with open(devnull, 'wb') as DEVNULL:
        process_b = Popen(COMMAND, stdout=DEVNULL)
        process_b.wait()
        print(process_b.stderr)
    print

    # Part c
    print("PART C")
    try:
        print(check_output(BOGUS_COMMAND))
    except OSError as err:
        print(err)
    print

    # Part e
    print("PART E")
    process_c = Popen(['du', '-h'], stdout=PIPE)
    process_b.wait()
    print(process_c.stdout.readlines())
    print

    # Part f
    print("PART F")
    commander(['ls', '-l'])
    print

if __name__ == '__main__':
    main()