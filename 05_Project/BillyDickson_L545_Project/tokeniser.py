##########################################
#               1.Tokeniser              #
#                                        #
#  Simple tokeniser that splits words    #
#  at spaces. Doesn't join with \n as    #
#  this messes with detokenisation.      #
#                                        #
##########################################

import sys
import re

def tokenise(line):

        line = re.sub(r'([^0-9]),', r'\g<1> ,', line)
        line = re.sub(r',([^0-9])', r', \g<1>', line)
        line = re.sub(r'([\(\)"?:!;])', r' \g<1> ', line)

        output = []
        for c in line.split(' '):
                output.append(c)
        return ' '.join(output)

line = sys.stdin.readline()

while line != '':
        print(tokenise(line))
        line = sys.stdin.readline()
