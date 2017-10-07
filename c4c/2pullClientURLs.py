import re

han = open('leverClientListGQueryByDate.txt')

for line in han:
    line = line.rstrip()
    if re.search('https://jobs', line) :
        print(line)