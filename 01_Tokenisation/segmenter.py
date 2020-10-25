import sys
#simple approach that replaces every full stop followed by space with full stop and newline
line = sys.stdin.readline()
while line != '':
	for i in line.split(' '):
#if line is split at space, and last char is full stop, then next char must have been space
		if i[-1] == '.':
			sys.stdout.write(i + '\n')
		else:
			sys.stdout.write(i + ' ')
	line = sys.stdin.readline()
