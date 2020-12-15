##########################################
#                2.Deleter               #
#                                        #
#  Delets all tokens up to the word      #
#  'ingredients'.                        #
#                                        #
##########################################

import sys
line = sys.stdin.readline()
while line != '':
	for i in line.split():
		if i.lower() == 'ingredients':
			while line != '':
				print(line)
				line = sys.stdin.readline()
	line = sys.stdin.readline()
