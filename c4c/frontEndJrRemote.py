import json, codecs
from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyB_QXKEohLw7XvtgecsshkzkqUOJ8FzSCc"
my_cse_id = "009043117829057268965:tgiqlni9v2w"
count = 1

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

while count < 30:
	results = google_search(
	    'junior+remote site:jobs.lever.co', my_api_key, my_cse_id, num=1, start=count)

	# for result in results:
	#     pprint.pprint(result)
	# count += 10
	for result in results:
		with open('results.txt', 'ab+') as f:
			json.dump(results, codecs.getwriter('utf-8')(f), sort_keys = True, indent = 4, ensure_ascii=False)
		if results == " ": break
		count += 1

f1 = open('results.txt', 'r')
f2 = open('resultsFinal.txt', 'w+')
for line in f1:
	f2.write(line.replace('][', ','))
f1.close()
f2.close()

