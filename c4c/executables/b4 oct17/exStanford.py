from bs4 import BeautifulSoup, SoupStrainer
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
import html2text

req = Request('https://jobs.lever.co/roam/ca9b536d-592b-4755-b03a-14df06274743', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts', headers={'User-Agent': 'Mozilla/5.0'})
r = urllib.request.urlopen(req).read()

# only_body_tag = SoupStrainer("body")
only_attr = SoupStrainer("div", {"class" : "section section page-centered"})


soup = BeautifulSoup(r, "html.parser", parse_only=only_attr).prettify()

# soup = BeautifulSoup(r, "html.parser")

htmlText = soup.encode('utf-8').decode('utf-8', 'ignore')

print(html2text.html2text(htmlText))

# print(r)


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