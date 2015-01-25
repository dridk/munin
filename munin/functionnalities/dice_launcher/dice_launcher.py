# -*- coding: utf-8 -*-
#########################
#       DICE            #
#########################


#########################
# IMPORTS               #
#########################
from random import randint
import re




#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CLASS                 #
#########################
class DiceLauncher():
    """
    Simple Functionnality application.
    Wait for something like:
        3d8 1d9 2d20
    each set of dices are launched, and results are returned:
        3d8: {2, 1, 7} 10
        1d9: {3} 3
        2d20: {12, 17} 29
        total: 42
    """
    REGEX = re.compile(r"\s*((?:\s*\d+[dD]\d+)+)")


# CONSTRUCTOR #################################################################
    def __init__(self):
        self._regex = self.REGEX


# PUBLIC METHODS ##############################################################
    def do_command(self, bot, matched_groups, sudo=False, author=None):
        """Execute command for bot (unused), according to regex matchs (used) and sudo mode (unused)"""
        results = ''
        total   = 0

        for dice_set in matched_groups[0].split(' '):
            n, s = dice_set.lower().split('d')
            if '0' in (n, s): continue
            numbers  = [randint(1, int(s)) for _ in range(int(n))]
            total   += sum(numbers)
            results += '{' + ', '.join((str(_) for _ in numbers)) + '} \ttotal: ' + str(sum(numbers)) + '\n'

        return results + 'total: ' + str(total)



# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
    def want_speak(self):
        """Return True iff self have something to say"""
        return False


# ACCESSORS ###################################################################
    @property
    def regex(self):
        return self._regex

    @property
    def help(self):
        return """DICELAUNCHER: launch dices. Try something like '3d5 3d20', you will understand."""


# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################


