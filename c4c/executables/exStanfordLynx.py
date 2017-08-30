from bs4 import BeautifulSoup, SoupStrainer
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
import html2text
import subprocess

req = Request('https://jobs.lever.co/gonimbly/ae0efc21-9754-4418-b5b3-0a1c66ffb281', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts', headers={'User-Agent': 'Mozilla/5.0'})
r = urllib.request.urlopen(req).read()

# only_body_tag = SoupStrainer("body")
only_attr = SoupStrainer("div", {"class" : "section section page-centered"})


soup = BeautifulSoup(r, "html.parser", parse_only=only_attr).prettify()

# soup = BeautifulSoup(r, "html.parser")

htmlText = soup.encode('utf-8').decode('utf-8', 'ignore')

# print(html2text.html2text(htmlText))

# print(soup)

f = open('Lynx.htm','w')
f.write(htmlText)
f.close()

# lynx -cfg <(echo COLLAPSE_BR_TAGS:FALSE) -dump Lynx.htm > output.txt

# def kill_lynx(pid):
#     os.kill(pid, signal.SIGKILL)
#     os.waitpid(-1, os.WNOHANG)
#     print("lynx killed")
 
def get_url(url):
    web_data = ""
 
    cmd = "lynx -dump -nolist -notitle \"{0}\"".format(url)
    lynx = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    # t = threading.Timer(300.0, kill_lynx, args=[lynx.pid])
    # t.start()
 
    web_data = lynx.stdout.read()
    # t.cancel()
 
    web_data = web_data.decode("utf-8", 'replace')
    return web_data

if __name__ == "__main__":    
    print(get_url("./Lynx.htm"))
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