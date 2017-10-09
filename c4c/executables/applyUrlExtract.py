import re

hand = open('finalResultsPostReadyFormat1-1k.txt')

for line in hand:
	line = line.rstrip()
	stuff = re.findall('(https://.*\/)apply\'', line)
	print(stuff)