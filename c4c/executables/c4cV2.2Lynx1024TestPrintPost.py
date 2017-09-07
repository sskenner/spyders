import json, codecs, requests, pickle, datetime
import urllib.request, urllib.parse, urllib.error
import re
import subprocess
from googleapiclient.discovery import build 
from itertools import repeat
from unidecode import unidecode
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import Request, urlopen


# AVAILABLE_TOKEN_SETS = {
#     'ess': {
#         'api_key': 'AIzaSyB_QXKEohLw7XvtgecsshkzkqUOJ8FzSCc',
#         'cse_id': '009043117829057268965:tgiqlni9v2w'
#     },
#     'ssk': {
#         'api_key': 'AIzaSyAn_YOSbC43zmv2cexCddaIYfJfMb9d08s',
#         'cse_id': '003565523015477317201:lwtcnf2u57i'
#     }
# }

# NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN = 'ess'

# API_KEY_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['api_key']
# CSE_ID_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['cse_id']

CODEFORCASH_BASE_URL = 'https://i.codefor.cash'
CODEFORCASH_API_KEY = '5b26197b391c5dab05c5606d43fba9c6'

# MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY = 10

# def do_google_search(search_term, api_key, cse_id, **kwargs):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
#     return res['items']

results_from_GSE_query = [
    {
        "cacheId": "da9woURNlJgJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/alation/fd8dae88-5abd-4740-99e9-4ab871aea60f",
        "htmlFormattedUrl": "https://jobs.lever.co/alation/fd8dae88-5abd-4740-99e9-4ab871aea60f",
        "htmlSnippet": "... and mentor <b>junior</b> engineers; (if you are <b>junior</b>) be hungry to learn and take on <br>\n... Java, or <b>Javascript</b>; a desire to participate in a fast-paced and intense startup&nbsp;...",
        "htmlTitle": "Alation - Software Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/alation/fd8dae88-5abd-4740-99e9-4ab871aea60f",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5d0299db-6a81-4f27-821d-4df595bec1a1-1485300847600.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "93",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTVZp2blUBHF6mEVF6bNNV4OUz6zrBU1CH2PoT3ChZIB5ItxHPc9AJ0RA",
                    "width": "542"
                }
            ],
            "metatags": [
                {
                    "og:description": "Alation was founded in 2012 when a PhD engineer from Google, a designer from Apple, and an executive from Oracle teamed up to help people to connect with the data they need. Today, our team consists of creators and communicators with varied backgrounds. From Stanford and Cal, big companies and one-man startups, the United States and abroad, we all came together to work toward a shared vision of a world where informed decision-making is the norm -- we are incredibly driven to make data more accessible in every industry. We\u2019re based in sunny Redwood City, CA and funded by top investors like Andreessen Horowitz, Data Collective, and Costanoa Venture Capital. Our customers include some of the world\u2019s largest organizations, with thousands of employees and petabytes of data.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5d0299db-6a81-4f27-821d-4df595bec1a1-1485300847600.png",
                    "og:image:height": "200",
                    "og:title": "Alation - Software Engineer",
                    "og:url": "https://jobs.lever.co/alation/fd8dae88-5abd-4740-99e9-4ab871aea60f",
                    "twitter:description": "Alation was founded in 2012 when a PhD engineer from Google, a designer from Apple, and an executive from Oracle teamed up to help people to connect with the data they need. Today, our team consists of creators and communicators with varied backgrounds. From Stanford and Cal, big companies and one-man startups, the United States and abroad, we all came together to work toward a shared vision of a world where informed decision-making is the norm -- we are incredibly driven to make data more accessible in every industry. We\u2019re based in sunny Redwood City, CA and funded by top investors like Andreessen Horowitz, Data Collective, and Costanoa Venture Capital. Our customers include some of the world\u2019s largest organizations, with thousands of employees and petabytes of data.",
                    "twitter:title": "Alation - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... and mentor junior engineers; (if you are junior) be hungry to learn and take on \n... Java, or Javascript; a desire to participate in a fast-paced and intense startup\u00a0...",
        "title": "Alation - Software Engineer"
    }
]

#local manual per listing test
def get_job_listings_from_google():
    data_get_job_listings_from_google = results_from_GSE_query
    return data_get_job_listings_from_google

# def get_job_listings_from_google(number_of_listings_to_get = 10):
#     return_value = []
#     for search_result_number_from_which_api_query_results_start in range(1, number_of_listings_to_get + 1, MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY):
#         return_value.extend(do_google_search(
#             # https://i.codefor.cash/job_alerts/generate_subscriber_keywords
#             search_term='sqlite site:jobs.lever.co',
#             api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN,
#             num=MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY,
#             # start=1))
#             start=search_result_number_from_which_api_query_results_start))
#     return return_value[:number_of_listings_to_get]

def save_gse_call_results(listings):
    with open('finalResults.txt','a+') as f:
        f.write(json.dumps(get_job_listings_from_google(), sort_keys = True,
                indent = 4))

def send_job_listings_to_codeforcash(listings):
    for listing in range(len(listings)):
        data_to_send_in_request_body = {
            "key": CODEFORCASH_API_KEY,
            "title": listings[listing]["title"],
            "website": listings[listing]["link"],
            # "description": listings[listing]["snippet"],
            "description": "",
            "utc_datetime": datetime.datetime.utcnow().isoformat(),
            "lat": "",
            "lng": "",
            "country": "",
            "employment_type": "",
            "remote_ok": "",
            "time_commitment": ""
        }
        data_send_job_lisitings_to_codeforcash = json.dumps(data_to_send_in_request_body)
        data_of_each_listing = json.loads(data_send_job_lisitings_to_codeforcash)

        try:
            html = urllib.request.urlopen(data_of_each_listing["website"]).read()
        except urllib.error.HTTPError as e:
            print(e)
        else:
            only_tag_class = SoupStrainer("div", {"class" : "section-wrapper page-full-width"})
            soup = BeautifulSoup(html, "html.parser", parse_only=only_tag_class)
            htmlDecode = soup.encode('utf-8').decode('utf-8', 'ignore')
            
            f = open('Lynx.htm','w')
            f.write(htmlDecode)
            f.close()

            #refactor as functions
            web_data = ''
            cmd = 'lynx -dump -width 1024 -nolist -notitle \"{0}\"'.format('./Lynx.htm')
            lynx = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            web_data = lynx.stdout.read()
            web_data = web_data.decode('utf-8', 'replace')
            
            #test print lynx formatted description 
            # print(web_data)

            data_to_send_in_request_body["description"] = web_data

            for data_key in data_to_send_in_request_body:
                # data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key].encode('UTF8').decode('utf-8')
                data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key]

            #test print json formatted complete listing
            print(data_to_send_in_request_body)
    
        response_per_post = requests.post(
            url=CODEFORCASH_BASE_URL+'/api/metum/create',
            data=data_to_send_in_request_body)
        
        with open('responseFromCodeforcash','ab+') as f:
            pickle.dump(response_per_post, f)

if __name__ == '__main__':
    save_gse_call_results(send_job_listings_to_codeforcash(get_job_listings_from_google()))

    # save_gse_call_results(send_job_listings_to_codeforcash(remove_non_ascii(get_job_listings_from_google())))

    # send_job_listings_to_codeforcash(return_value)
    # save_gse_call_results(return_value)

    # save_result_of_sending_job_listings_to_codeforcash(send_job_listings_to_codeforcash(return_value))

    # save_gse_call_results(get_job_listings_from_google())

    # save_result_of_sending_job_listings_to_codeforcash(
    #     get_job_listings_from_google())
        
