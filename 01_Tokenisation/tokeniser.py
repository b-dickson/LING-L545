import sys, re
#tokenises text and prints out with line number
def tokenise(line):
	for i in '?!.,;:()':
		line = line.replace(i, ' ' + i + ' ')

#Used the following line as noted in the slides to clean up extra spaces so they wouldn't be counted.
#One could accomplish the above replace() task with re as well, however I wanted to try it with replace()
#as noted in the practical
	line = re.sub(r'  +', ' ', line[:-1])

#long way around for replacing space with newline but easier to work with
#splits at space, then rejoins with newline
	output = []
	for c in line.split(' '):
		output.append(c)
	return '\n '.join(output)

line = sys.stdin.readline()

#my solution to counting, this so i wouldnt have to deal with a counter inside the function
counter = 1
document = ''
while line != '':
	document += tokenise(line.strip('\n'))
	line = sys.stdin.readline()

for i in document.split('\n'):
	print(str(counter),' ',i)
	counter += 1

