#!/bin/python
# -*- coding: utf-8 -*-

class DFA:

    def __init__(self, states, alphabet, delta, accepts):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.start_state = 0
        self.delta = delta
        self.accepts = set(accepts)
        self.current_state = start_state

    ## print DFA
    def dfa_print(self):
        print "Number of states: %s" % len(self.states)
        print "Accepting states:", self.accepts
        print "Alphabet:", self.alphabet
        for c in self.alphabet:
            results = map(lambda x: self.delta(x, c), sorted(self.states))
            print c, "\t", "\t".join(map(str, results))

    
