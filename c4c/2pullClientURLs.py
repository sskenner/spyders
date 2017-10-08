import re

han = open('leverClientListURIListTest.txt')
# han = open('leverClientListGQueryByDate.txt')

for line in han:
    line = line.rstrip()
    client = re.findall('(^.+)/', line)
    print(client)

    # if re.search('https://jobs', line) :
    #     print(line)