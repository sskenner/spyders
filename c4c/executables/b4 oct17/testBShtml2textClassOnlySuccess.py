from bs4 import BeautifulSoup, SoupStrainer
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
import html2text
import re

# req = Request('https://jobs.lever.co/eventbrite/a631deac-26d8-491d-9238-400a206e40f4', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('https://jobs.lever.co/roam/ca9b536d-592b-4755-b03a-14df06274743', headers={'User-Agent': 'Mozilla/5.0'})
req = Request('https://jobs.lever.co/baylabs/660b02d8-6701-4499-9768-fbe1fceca9aa', headers={'User-Agent': 'Mozilla/5.0'})

r = urllib.request.urlopen(req).read()

only_tag_class = SoupStrainer("div", {"class" : "section-wrapper page-full-width"}) 
## can add newline after each section?

# only_tag_class = SoupStrainer("div", {"class" : "section section page-centered"})


soup = BeautifulSoup(r, "html.parser", parse_only=only_tag_class)
# soup = BeautifulSoup(r, "html.parser", parse_only=only_tag_class).prettify()

# htmlText = soup.find_all("br")
# selects = soup.find_all('br')
# div_name = selects.div
# div_name.decompose()
# soup.decompose("br")
# unwanted = html_no_br.find("br")
# unwanted = html_all_br.br.extract()

# print(html_no_br)

htmlDecode = soup.encode('utf-8').decode('utf-8', 'ignore')
# print(type(htmlText))

# html2text.BODY_WIDTH = 0
# print(type(htmlText))

htmlText = html2text.html2text(htmlDecode)

# htmlTextJoined = re.sub(' +', '', htmlText)
# htmlTextJoined = ' '.join(htmlText.split())
# htmlTextJoined =re.sub(r'\n{2,10}', '',htmlText)
htmlTextJoined =re.sub(r'\n+', '\n',htmlText)

# print(htmlText)
print(htmlTextJoined)