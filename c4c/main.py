# import pprint
import json, codecs
from googleapiclient.discovery import build
import requests

def main():
	# service = build("customsearch", "v1", developerKey="AIzaSyB_QXKEohLw7XvtgecsshkzkqUOJ8FzSCc")

	data = requests.get('https://www.googleapis.com/customsearch/v1?q=jobs.lever.co+javascript&cx=009043117829057268965:tgiqlni9v2w&key=AIzaSyB_QXKEohLw7XvtgecsshkzkqUOJ8FzSCc')
	# data = service.cse().list(
	# 	q='jobs.lever.co+javascript',
	# 	cx='009043117829057268965:tgiqlni9v2w',
	# 	start=0
	# 	).execute()
	# pprint.pprint(res)
	with open('data.txt', 'wb') as f:
		json.dump(data, codecs.getwriter('utf-8')(f), sort_keys = True, indent = 4, ensure_ascii=False)
		json.dump(data, sort_keys = True, indent = 4, ensure_ascii=False)

if __name__ == '__main__':
	main()