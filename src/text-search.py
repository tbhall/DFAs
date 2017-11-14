#!/bin/python
# -*- coding: utf-8 -*-

###############################################################################
###                                                                         ###
###  Description: Read a string w from a text file, and write to standard   ###
###  output the description of a DFA that accepts a string x iff w is a     ###
###  substring of x.                                                        ###
###                                                                         ###
###############################################################################

__author__  = "Tyler Hall"
__copyright__ = "Copyright 2017"

###################
#     IMPORTS     #
###################

import sys
from itertools import repeat
from pprint import pprint

###################
# GLOBAL VARIABLE #
###################
number_of_states = 0
accepting_states = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_table = {}
DFA_table = {}
'''
Number of states: 4
Accepting states: 3
Alphabet: 01
1 0
0 2
3 1
3 0
'''

###################
#     FUNCTIONS   #
###################

def DFA_print():
    print("Number of states: " + str(number_of_states))
    print("Accepting states: " + "\\".join([str(x) for x in accepting_states]))
    print("Alphabet: " + alphabet)
    for value in DFA_table.itervalues():
        print(" ".join([str(x) for x in value]))

def main(argv):
    global number_of_states
    global accepting_states
    global alphabet
    global alphabet_table
    global DFA_table
    reference = {}
    STR_file = open(argv,"r")

    text = STR_file.read().split('\n')[0]

    number_of_states = len(text) + 1
    accepting_states.append(len(text))
    count = 0
    for x in alphabet:
        alphabet_table.update({x:count})
        count += 1
    list_trans = [0 for i in alphabet_table]
    list_trans_last = [7 for i in alphabet_table]

    for x in xrange(int(number_of_states)):
        if(x == (int(number_of_states)-1)):
            state = number_of_states - 1
            DFA_table.update({x: list(repeat(state, 26))})
        else:
            DFA_table.update({x: list(repeat(0, 26))})

    for i in range(0,len(text),1):
        reference.update({text[:i]: i})

    for key, value in sorted(DFA_table.items()[:-1]):
        c = text[key]
        reference.update({text[:key]: key})
        alphabet_value = alphabet_table.get(c)
        value[alphabet_value] = key+1
        for i in range(1,key,1):
            for char in text:
                past_phase = text[i:key]+char
                if(past_phase in reference):
                    state = reference.get(past_phase)
                    char_value = alphabet_table.get(char)
                    if(value[char_value] == 0):
                        value[char_value] = state
        for char in text:
            if(char in reference):
                state = reference.get(char)
                char_value = alphabet_table.get(char)
                if(value[char_value] == 0):
                    value[char_value] = state

    DFA_print()


###################
#       MAIN      #
###################
if __name__ == "__main__":
    if(len(sys.argv) != 1):
        main(sys.argv[1])
    else:
        print "Please pass one argument"
