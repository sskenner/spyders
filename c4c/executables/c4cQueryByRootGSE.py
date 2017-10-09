# Python program to query custom search engine for listings and send them to an API

# Name - c4cQueryPrintCheckPost.py
# Date and version No: ??????

import json, codecs, requests, pickle, datetime
import urllib.request, urllib.parse, urllib.error
import re
import subprocess
from googleapiclient.discovery import build 
from itertools import repeat
from unidecode import unidecode
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import Request, urlopen


AVAILABLE_TOKEN_SETS = {
    'ess': {
        'api_key': 'AIzaSyB_QXKEohLw7XvtgecsshkzkqUOJ8FzSCc',
        'cse_id': '009043117829057268965:tgiqlni9v2w'
    },
    'ssk': {
        'api_key': 'AIzaSyAn_YOSbC43zmv2cexCddaIYfJfMb9d08s',
        'cse_id': '003565523015477317201:lwtcnf2u57i'
    }
}

NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN = 'ess'

API_KEY_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['api_key']
CSE_ID_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['cse_id']

CODEFORCASH_BASE_URL = 'https://i.codefor.cash'
CODEFORCASH_API_KEY = '5b26197b391c5dab05c5606d43fba9c6'

MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY = 10

# clients = ['twitch', 'creditkarma']
# clients = ['creditkarma']
clients = ['twitch']

BAD_WORDS_LIST = ["personal trainer", "executive assistant", "low cost","ultimate software", "app tester", "1-2 hours a day","secretary", "front desk", "office manager", "use referr", "commission", "motivated individuals" , "sales specialist","no experience required", "amazing opportunity", "court researcher","technical support", "tech support", "mystery shopper","customer service", "field engineer", "administrative", "book keeping", "extra money", "extra cash", "extra income", "data entry", "have a car", "debit card", "earn extra income", "step by step training", "dollars a week", "supplemental income", "sales rep","closed lead", "do you want to make", "facebook page", "facebook fan page", "theater installation", "game tester", "% stake","printing and mailing", "laserjet", "credit score","real estate investment", "research study","in person", "focus group", "survey", "you must live", "local", "must be local", "tutor", "instructor", "partner ", "equity", "cofounder", "co founder", "co-founder", "unpaid", "volunteer", "get paid", "get pay", "weekly", "webcam", "money making", "fast money", "workfromhome", "fast cash", "scam", "make money", "selling cell phones", "wireless sales", "it's legit", "telemarketer", "fb account", "Cell Phone Repair", "earn money by just", "only applicants residing in", "from his location", "virtual assistant", "by working less", "earn extra money", "experienced seller", "looking for a job", "earn over", "motorclub",  "office assistant", "event planner", "____________________________________________________________", "Filter by:"]

def do_google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    print('<<<< CSE Query Loop >>>>')
    print(res['queries']['request'][0]['startIndex'], 'CSE Start Index')
    print(res['queries']['request'][0]['totalResults'], 'CSE Query Results')

    if res['queries']['request'][0]['totalResults'] == '0':
        # # # prints when reach the gse page where totalResults == '0'
        print('@@@@ NO CSE QUERY RESULTS @@@@')
        # print(res)
        return res['items']
    else:
        return res['items']
    
# set gse query parameters to iterate through results
def get_job_listings_from_google(cse_search_term, number_of_listings_to_get):
    return_value = []
    for search_result_number_from_which_api_query_results_start in range(1, number_of_listings_to_get + 1, MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY):
        try:
            return_value.extend(do_google_search(
                # online version of keywords > https://i.codefor.cash/job_alerts/generate_subscriber_keywords
                search_term=cse_search_term,
                api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN,
                num=MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY, start=search_result_number_from_which_api_query_results_start))
        except:
            print(len(return_value), 'Listings + Empty Index')
            return return_value[:number_of_listings_to_get]
    return return_value[:number_of_listings_to_get]

# def save_gse_call_results(listings):
#     with open('saved_gse_results.txt','a+') as f:
#         f.write(json.dump(listings), sort_keys = True,
#                 indent = 4)
def save_gse_call_results(listings):
    print('@@@@', len(listings), 'Listings Saved @@@@')
    with open('saved_gse_results.txt','a+') as f:
        f.write(json.dumps(listings))
    # with open('saved_gse_results.txt','a+') as f:
    #     f.write(json.dumps(get_job_listings_from_google("'software engineer' remote site:jobs.lever.co/" + client, 10), sort_keys = True,
    #             indent = 4))

def send_job_listings_to_codeforcash(listings):
    save_gse_call_results(listings)
    count = 0
    # iterate through gse results to grab values for c4c API
    for listing in range(len(listings)):
        any_bad_words = False
        data_to_send_in_request_body = {
            "key": CODEFORCASH_API_KEY,
            "title": listings[listing]["title"],
            "website": listings[listing]["link"],
            "description": "",
            "utc_datetime": datetime.datetime.utcnow().isoformat(),
            "lat": "",
            "lng": "",
            "country": "",
            "employment_type": "",
            "remote_ok": "",
            "time_commitment": ""
        }
        # encode/decode dictionary from and to json
        data_send_job_lisitings_to_codeforcash = json.dumps(data_to_send_in_request_body)
        data_of_each_listing = json.loads(data_send_job_lisitings_to_codeforcash)

        # use beautiful soup to follow url and grab descriptions
        try:
            html = urllib.request.urlopen(data_of_each_listing["website"]).read()
        # keep going if url is 404
        except urllib.error.HTTPError as e:
            print(e)
            continue
        else:
            # soupstrain description
            description_tag_class = SoupStrainer("div", {"class" : "section-wrapper page-full-width"})
            description_soup = BeautifulSoup(html, "html.parser", parse_only=description_tag_class)
            description_html_decoded = description_soup.encode('utf-8').decode('utf-8', 'ignore')
           
            f = open('Lynx.htm','w')
            f.write(description_html_decoded)
            f.close()

            # pass description through lynx to format
            description_web_data = ''
            cmd = 'lynx -dump -width 1024 -nolist -notitle \"{0}\"'.format('./Lynx.htm')
            lynx = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            description_web_data = lynx.stdout.read()
            description_web_data = description_web_data.decode('utf-8', 'replace')

            # soupstrain location
            location_tag_class = SoupStrainer("div", {"class" : "sort-by-time posting-category medium-category-label"})
            location_soup_html = BeautifulSoup(html, "html.parser", parse_only=location_tag_class)
            location = location_soup_html.text

            # print listing title
            print(data_of_each_listing["title"])
            print('>>>>', data_of_each_listing["website"])
            # set remote or not
            # print(location)
            if 'Remote' in location or 'remote' in location or 'Remote' in data_of_each_listing["title"] or 'remote' in data_of_each_listing["title"]:
                data_to_send_in_request_body["remote_ok"] = 'remote_ok'
                # print('remote')
            else:
                # print('no remote')
                data_to_send_in_request_body["remote_ok"] = 'remote_not_ok'
            
            # check for bad words in description
            for bad_word in BAD_WORDS_LIST:
                if bad_word in description_web_data:
                    any_bad_words = True
                    print('** bad word:', bad_word)
                else:
                    data_to_send_in_request_body["description"] = description_web_data
                    data_to_send_in_request_body["country"] = location

                    for data_key in data_to_send_in_request_body:
                        data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key]
                    
            # save listings without bad words
            if any_bad_words == False:
                clean_data_to_post = data_to_send_in_request_body
                count += 1
                # test: print formatted descriptions
                # print(description_web_data)
            else:
                continue
                    
            # # test print json formatted complete listing
            # print(data_to_send_in_request_body)
    
        # # send formatted json to code4cash api
        # response_per_post = requests.post(
        #     url=CODEFORCASH_BASE_URL+'/api/metum/create',
        #     data=clean_data_to_post)
        # # save code4cash response
        # with open('responseFromCodeforcash','ab+') as f:
        #     pickle.dump(response_per_post, f)

        # # save prePostListings before post to c4c
        with open('saved_post_data.txt','a+') as f:
            f.write(json.dumps(clean_data_to_post))

    # print(clean_data_to_post)
    print('****', count, 'Clean Listings Posted ****')

if __name__ == '__main__':
    for client in clients:
        print('**** ROOT:', client, '****')
        send_job_listings_to_codeforcash(get_job_listings_from_google("'software engineer' site:jobs.lever.co/" + client, 150))
        # get_job_listings_from_google("'software engineer' site:jobs.lever.co/" + client, 40)        
        # save_gse_call_results(send_job_listings_to_codeforcash(get_job_listings_from_google("'software engineer' remote site:jobs.lever.co/" + client, 10)))

