#!/bin/python
# -*- coding: utf-8 -*-

###############################################################################
###                                                                         ###
###  Description: First read the description of the DFA.                    ###
###     The description is in a file named by the first command line        ###
###     argument (see below for information about the format of this file). ###
###     Next read a series of zero or more strings from another text file   ###
###     named by the second command line argument. These are inputs to the  ###
###     DFA. Each string will take up an entire line of text, ending with a ###
###     newline character (which is not included in the string). For each   ###
###     string, write to standard output either “accept” or “reject”        ###
###     according to the behavior of the DFA on the string. End each output ###
###     word with a newline.                                                ###
###                                                                         ###
###############################################################################

__author__  = "Tyler Hall"
__copyright__ = "Copyright 2017"

###################
#     IMPORTS     #
###################

import sys

###################
# GLOBAL VARIABLE #
###################



###################
#     FUNCTIONS   #
###################

def main(argv1, argv2):
    DFA_file = open(argv1,"r")
    str_file = open(argv2,"r")

    DFA_data = DFA_file.read()
    str_data = str_file.read().split('\n')

####### READING DFA FILE SETTING UP TRANSITION MAP #######
    DFA_lines = DFA_data.split('\n')
    line_one = DFA_lines[0]
    line_two = DFA_lines[1]
    line_three = DFA_lines[2]
    lines_four = DFA_lines[3:]

    # Number of States (from line_one)
    number_of_states = line_one.split(' ')[3]


    # Accepting states (from line_two)
    accepting_states = list(line_two.split(' ')[2:])

    # Alphabet (from line_three)
    alphabet = line_three[10:]
    alphabet_table = { }
    count = 0
    for x in alphabet:
        alphabet_table.update({x:count})
        count += 1
    # Transitions (from lines_four)
    DFA_table = { }
    for x in xrange(int(number_of_states)):
        list_trans = lines_four[x]
        list_trans = list(list_trans.split(' '))
        DFA_table.update({x: list_trans})
####### READING STRING FILE #######
    for line in str_data[:len(str_data) - 1 ]:
        state = 0
        reject = False
        if line == '':
            state = 0
        else:
            for x in line:
                if(alphabet_table.has_key(x)):
                    x_value = alphabet_table.get(x)

                    current_state_trans = DFA_table.get(int(state))

                    state = current_state_trans[int(x_value)]
                else:
                    reject = True
                    break
        if( str(state) not in accepting_states or reject == True ):
            print("reject")
        else:
            print("accept")


###################
#       MAIN      #
###################
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        main(sys.argv[1], sys.argv[2])
    else:
        print "Please pass two argument"
