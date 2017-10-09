# import re
import json

handle = open('leverClientAggrList.txt')

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
        # print(counts)
        # with open('leverClientListCount.txt','a+') as f:
        #     f.write(json.dumps(counts))
print(sorted([(v,k) for k,v in counts.items()]))

# bigcount = None
# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print(bigword, bigcount)

# han = open('leverClientListURIList.txt')
# han = open('leverClientListGQueryByDate.1.txt')
# han = open('leverClientListURIListTest.txt')
# han = open('leverClientListGQueryByDate.txt')

# for line in han:
#     line = line.rstrip()
#     client = re.findall('(^.+)/', line)
#     with open('leverClientList.2.txt','a+') as f:
#             f.write(line)
    # print(client)

    # if re.search('https://jobs', line) :
    #     with open('leverClientListURIList.txt','a+') as f:
    #         f.write(line)
        # print(line)
