import re

han = open('leverClientListURIList.txt')
# han = open('leverClientListGQueryByDate.1.txt')
# han = open('leverClientListURIListTest.txt')
# han = open('leverClientListGQueryByDate.txt')

for line in han:
    line = line.rstrip()
    client = re.findall('(^.+)/', line)
    with open('leverClientList.2.txt','a+') as f:
            f.write(line)
    # print(client)

    # if re.search('https://jobs', line) :
    #     with open('leverClientListURIList.txt','a+') as f:
    #         f.write(line)
        # print(line)