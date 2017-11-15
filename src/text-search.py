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
    #global alphabet_table
    global DFA_table
    reference = {}
    STR_file = open(argv,"r")

    text = STR_file.read().split('\n')[0]

    number_of_states = len(text) + 1
    accepting_states.append(len(text))
    count = 0

    for x in xrange(int(number_of_states)):
        trans_value = list(repeat(0, 26))
        if(x == (int(number_of_states)-1)):
            state = number_of_states - 1
            DFA_table.update({x: list(repeat(state, 26))})
        else:
            c = text[x]
            reference.update({text[:x]: x})
            alphabet_value = alphabet.index(c)
            trans_value[alphabet_value] = x+1
            DFA_table.update({x: trans_value})
            for i in xrange(1,x,1):
                if(text[i:x] in reference):
                    for char in alphabet:
                        if(trans_value[alphabet.index(char)] == 0):
                            past_phase = text[i:x]+char
                            if(past_phase in reference):
                                state = reference.get(past_phase)
                                char_value = alphabet.index(char)
                                if(trans_value[char_value] == 0):
                                    trans_value[char_value] = state

            char_value = alphabet.index(text[0])
            if(trans_value[char_value] == 0):
                trans_value[char_value] = 1

    DFA_print()


###################
#       MAIN      #
###################
if __name__ == "__main__":
    if(len(sys.argv) != 1):
        main(sys.argv[1])
    else:
        print "Please pass one argument"
