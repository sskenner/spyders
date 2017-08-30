from bs4 import BeautifulSoup, SoupStrainer
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
import subprocess

### test various boards
req = Request('https://jobs.lever.co/visier/43bb5cbc-1a7d-4096-94db-07c235890e39', headers={'User-Agent': 'Mozilla/5.0'})

# req = Request('https://jobs.lever.co/pillpack/5ed959c8-5777-4298-ab6a-8e64be331c7a', headers={'User-Agent': 'Mozilla/5.0'})
## error: encode ## Traceback (most recent call last):
#   File "lynxTestHhc.py", line 23, in <module>
#     f.write(htmlText)
#   File "C:\Users\kenners\AppData\Local\Programs\Python\Python36-32\lib\encodings\cp1252.py", line 19, in encode
#     return codecs.charmap_encode(input,self.errors,encoding_table)[0]
# UnicodeEncodeError: 'charmap' codec can't encode character '\u2028' in position 1966: character maps to <undefined>
#####################################################################
# req = Request('https://jobs.lever.co/brightlink/851b9097-8189-4314-a390-13663b6edefd', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('https://jobs.lever.co/gonimbly/ae0efc21-9754-4418-b5b3-0a1c66ffb281', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('https://jobs.lever.co/koddi/a166e767-7530-4f1f-bff1-b89427bd1548', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('https://jobs.lever.co/clerky/59623abf-f7d6-425a-bacb-53ddeaf5035e', headers={'User-Agent': 'Mozilla/5.0'})
###
r = urllib.request.urlopen(req).read()

only_attr = SoupStrainer('div', {'class' : 'section section page-centered'})

soup = BeautifulSoup(r, 'html.parser', parse_only=only_attr).prettify()

htmlText = soup.encode('utf-8').decode('utf-8', 'ignore')

f = open('Lynx.htm','w')
f.write(htmlText)
f.close()

def format_div(htm):
    web_data = ''
    cmd = 'lynx -dump -nolist -notitle \"{0}\"'.format(htm)
    lynx = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    web_data = lynx.stdout.read()
    web_data = web_data.decode('utf-8', 'replace')
    
    return web_data

if __name__ == '__main__':    
    print(format_div('./Lynx.htm'))
    # print(get_url("file:///C:/Windows/minz/scrapin/c4c/Lynx.htm"))
	# print(get_url("file:///Users/nimda/code/spyders/c4c/Lynx.htm"))
	# lynx -cfg <(echo COLLAPSE_BR_TAGS:FALSE) -dump Lynx.htm > output.txt
    # print(get_urlData('file:///Users/nimda/code/spyders/c4c/Lynx.htm'))

# print(type(soup))
# print(soup.prettify()[0:2000])
# print(soup.get_text())
# print(text)
# print(soup.prettify())
# letters = soup.find_all("div", {"class" : "content-details"})
# letters = soup.find_all("div", {"class" : "ec_statements"})


# textInfo = soup.p.get_text().replace('\n','br')
# descWnewline = "\n".join(textInfo)
# textInfo = soup.p.get_text()

# print(descWnewline)
# print(type(textInfo))

# print(letters)
# print(html2text.html2text('''<div class="content-details ">
# <a class="b-inner" href="/about/advocacy/legislative-alerts/letter-congress-opposing-repeal-osha-rule-requiring-employers">
# <div class="b-text">
# <h5 class="content-type">Legislative Alert</h5>
# <h2 class="content-title"><span>Letter to Congress Opposing Repeal of OSHA Rule Requiring Employers to Keep Records on Serious Work-Related Injuries and Illnesses</span>
# </h2>
# <time datetime="2017-03-16T06:32:00-0400">March 16, 2017</time>
# </div>
# </a>
# <div></div>
# </div>
# '''))

# lobbying = {}
# for element in letters:
# 	lobbying[element.a.get_text()] = {}
# # print(lobbying)
# # print(letters[0].a["href"])

# prefix = "www.aflcio.org"
# for element in letters:
# 	lobbying[element.a.get_text()]["link"] = prefix + element.a["href"]
# # print(lobbying)	
# # print(letters[0].find("time"))

# for element in letters:
# 	print(element)
# 	date = element.find_all(id="h5")
# 	lobbying[element.a.get_text()]["date"] = element.time["datetime"]
# # print(date)
# # print(lobbying)


# http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html