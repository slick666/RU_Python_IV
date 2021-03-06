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

 d. Use the platform module to determine what OS you are using, then execute a
    command unique to that OS i.e. "yum search gcc" if Red Hat or Cent OS, or apt-get
    if Debian or Ubuntu.

 e. Use subprocess Popen to run "du -h" and output stdout to a pipe. Read the pipe
    and print the output.

 f. Create a new function commander() which takes any number of commands to execute
    (as strings) on the arg list, then runs them sequentially printing stdout.

"""
import subprocess
print("step a.")
subprocess.call(["ls", "-l"])
print('')

print("step b.")
subprocess.call(["ls", "-l"], stdout=subprocess.PIPE)
print('')

print("step c.")
try:
    subprocess.call(["bogus", "command"])
except OSError as e:
    print(e)
print('')

print("step e.")
proc = subprocess.Popen(["du", "-h"], stdout=subprocess.PIPE)
proc.wait()
print("Output from command:\n{}".format(proc.stdout.read()))
print('')

print("step f.")


def commander(commands):
    for cmd in commands:
        output = subprocess.check_output(cmd, shell=True)
        print "Output from {} :\n{}".format(cmd, output)
commands = ["ls -al",
            "df -h",
            "mount",
            'fortune',
            "who",
            "whoami"]
commander(commands)
