# print('sup world!')

## REGULAR EXPRESSIONS-PART 1
#############################
# # find()
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.find('From:') >= 0:
#         print(line)
#
# # re.search()
# import re
#
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From:', line) :
#         print(line)

# # Using re.search() Like startswith()
#
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.find('From:') >= 0:
#         print(line)
#
# import re
#
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From:', line) :
#         print(line)

# from io import open
# import re
#
# hand = open("mbox-short.txt", "r")
# for line in hand:
#     line = line.rstrip()
#     if re.search('^X.*:', line):
#         print(line)

# ^X.*:
# ^X-\S+:

## REGULAR EXPRESSIONS-PART 2
#############################
# import re
# x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[AEIOU]+',x)
# print(y)
# y = re.findall('[0-9]+', x)
# print(y)

## Greedy matching
# import re
# x = 'From: Using the : character'
# y = re.findall('^F.+:',x)
# print(y)
## Non-Greedy
# import re
# x = 'From: Using the : character'
# y = re.findall('^F.+?:',x)
# print(y)
## Fine Tuning String Extraction
# import re
# x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# y = re.findall('\S+@\S+',x)
# print(y)

# import re
# x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# y = re.findall('\S+@\S+',x)
# print(y)
# y = re.findall('^From (\S+@\S+)',x)
# print(y)

##Find and string slicing
# data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# atPosition = data.find('@')
# print(atPosition)
# spacePosition = data.find(' ',atPosition)
# print(spacePosition)
# host = data[atPosition+1 : spacePosition]
# print(host)

##The double split pattern
# data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# words = data.split()
# email = words[1]
# pieces = email.split('@')
# print(pieces[1])

##The double split pattern - RegEx
# import re
# line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# y = re.findall('@([^ ]*)',line)
# print(y)
## .. Cooler Version
# import re
# line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# y = re.findall('^From .*@([^ ]*)',line)
# print(y)

##Spam Confidence
# import re
# hand = open('mbox-short.txt')
# numberList = list()
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
#     if len(stuff) != 1: continue
#     number = float(stuff[0])
#     numberList.append(number)
# print('Maximum:', max(numberList))

##Escape Character
# import re
# x = 'We just blah blah $10.00 for cookies'
# y = re.findall('\$[0-9.]+',x)
# print(y)

## BOOK ##
##########
# Regular expressions
#
# Character matching in regular expressions
