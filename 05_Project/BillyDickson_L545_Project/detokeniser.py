##########################################
#               3.Detokeniser            #
#                                        #
#  Simple detokeniser that recombines    #
#  cleaned up text at spaces. Preserves  #
#  original \n for better readability.   #
#                                        #
##########################################

import sys

line = sys.stdin.readline()
output = []
while line != '':
      if line == '\n':
            line = sys.stdin.readline()
      output.append(line)
      line = sys.stdin.readline()
print(' '.join(output))
