#!/bin/python
# -*- coding: utf-8 -*-

###############################################################################
###                                                                         ###
###  Description: Read the description of a DFA from a text file, and write ###
###  (to standard output) the description of a minimal equivalent DFA       ###
###                                                                         ###
###############################################################################

__author__  = "Tyler Hall"
__copyright__ = "Copyright 2017"

###################
#     IMPORTS     #
###################

import sys
from pprint import pprint

###################
# GLOBAL VARIABLE #
###################

number_of_states,accepting_states,alphabet_table, DFA_table = 0,[],[],[]

###################
#     FUNCTIONS   #
###################
def DFA_print():
    print("Number of states: " + str(number_of_states))
    print("Accepting states: " + "\\".join([str(x) for x in accepting_states]))
    print("Alphabet: " + alphabet)
    for value in sorted(DFA_table.itervalues()):
        print(" ".join([str(x) for x in value]))
        
#Initalizes the DFA
def init_DFA_setup(data_file):
    DFA_file = open(data_file,"r")

    DFA_data = DFA_file.read()

####### READING DFA FILE SETTING UP TRANSITION MAP #######
    DFA_lines = DFA_data.split('\n')
    line_one = DFA_lines[0]
    line_two = DFA_lines[1]
    line_three = DFA_lines[2]
    lines_four = DFA_lines[3:]

    # Number of States (from line_one)
    number_of_states = int(line_one.split(' ')[3])


    # Accepting states (from line_two)
    accepting_states = list(int(i) for i in line_two.split(' ')[2:])

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
        list_trans = list(int(i) for i in list_trans.split(' '))
        DFA_table.update({x: list_trans})
    return number_of_states, accepting_states, alphabet_table, DFA_table

#Returns true or false if the state is an accepting one
def isAccepting(state):
    if state not in accepting_states:
        return False
    else:
        return True

def break_key(name):
    a,b = name.split(':')
    return a,b

def main(argv1):

####### READING DFA FILE SETTING UP TRANSITION MAP #######
    global number_of_states,accepting_states,alphabet_table, DFA_table
    table_dict = {}
    new_states = {}
    removed_states = []

    #If a change is made in table_dict it goes back through all the cells in table
    change = True

    number_of_states,accepting_states, alphabet_table, DFA_table = init_DFA_setup(argv1)
###################### MINIMIZING DFA ######################
    #initalize table (Dictionary)
    for x in DFA_table.iterkeys():
        for i in range(x+1, number_of_states):
            key_name = str(x)+ ":" + str(i)
            if(isAccepting(x) == isAccepting(i)):
                table_dict.update({key_name: False})
            else:
                table_dict.update({key_name: True})
    # Creates Table to final form
    while change == True:
        change = False
        for table_key in sorted(table_dict.iterkeys()):
            #print(table_key + " " + str(table_dict.get(key_name)))
            if(table_dict.get(table_key) == False):
                a,b = break_key(table_key)
                a_trans = DFA_table.get(int(a))
                b_trans = DFA_table.get(int(b))
                for alpha_char in sorted(alphabet_table.iterkeys()):
                        value = alphabet_table.get(alpha_char)
                        a_char_state = a_trans[int(value)]
                        b_char_state = b_trans[int(value)]
                        if (a_char_state != b_char_state):
                            if(a_char_state > b_char_state):
                                char_state = str(b_char_state) + ":" + str(a_char_state)
                            else:
                                char_state = str(a_char_state) + ":" + str(b_char_state)
                            if(table_dict.get(char_state) == True):
                                table_dict.update({table_key: True})
                                change = True
                                break


    for table_key, table_value in sorted(table_dict.items()):
        pass
    #pprint(removed_states)


###################
#       MAIN      #
###################
if __name__ == "__main__":
    if(len(sys.argv) != 1):
        main(sys.argv[1])
    else:
        print "Please pass one argument"
