# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()

# import urllib.request
#
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#
# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

##
# import urllib.request, urllib.parse, urllib.error
# import re
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# links = re.findall(b'href="(http://.*?)"', html)
# for link in links:
#     print(link.decode())

# Code: http://www.py4e.com/code3/urlregex.py
##

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))
##
##
# # To run this, you can install BeautifulSoup
# # https://pypi.python.org/pypi/beautifulsoup4
#
# # Or download the file
# # http://www.py4e.com/code3/bs4.zip
# # and unzip it in the same directory as this file
#
#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#
# # html.parser is the HTML parser included in the standard Python 3 library.
# # information on other HTML parsers is here:
# # http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
# soup = BeautifulSoup(html, "html.parser")
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     # Look at the parts of a tag
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)
#
# # Code: http://www.py4e.com/code3/urllink2.py
