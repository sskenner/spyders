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
        "cacheId": "xdpmKwkYWgAJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/gigya/4d49a34f-9099-489d-a31b-503ee85c7361",
        "htmlFormattedUrl": "https://jobs.lever.co/gigya/4d49a34f-9099-489d-a31b-503ee85c7361",
        "htmlSnippet": "Gigya&#39;s R&amp;D center in Azrieli towers in Tel-Aviv is looking for a senior <b>C#</b> <br>\ndeveloper with strong software engineering skills, to develop high-quality, <br>\nadvanced&nbsp;...",
        "htmlTitle": "Gigya - Senior <b>C#</b> Infrastructure/server developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/gigya/4d49a34f-9099-489d-a31b-503ee85c7361",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1483032404076.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRLsnFc0PMcFFI43P6jdsIQvSM0sUMq_MtuIf76o8aytrt35QzTPnDNptqi",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "Gigya\u2019s R&D center in Azrieli towers in Tel-Aviv is looking for a senior C# developer with strong software engineering skills, to develop high-quality, advanced infrastructures and micro-services for use by other R&D teams in the company.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1483032404076.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Gigya - Senior C# Infrastructure/server developer",
                    "og:url": "https://jobs.lever.co/gigya/4d49a34f-9099-489d-a31b-503ee85c7361",
                    "twitter:description": "Gigya\u2019s R&D center in Azrieli towers in Tel-Aviv is looking for a senior C# developer with strong software engineering skills, to develop high-quality, advanced infrastructures and micro-services for use by other R&D teams in the company.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1481204313579.png",
                    "twitter:title": "Gigya - Senior C# Infrastructure/server developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Gigya's R&D center in Azrieli towers in Tel-Aviv is looking for a senior C# \ndeveloper with strong software engineering skills, to develop high-quality, \nadvanced\u00a0...",
        "title": "Gigya - Senior C# Infrastructure/server developer"
    },
    {
        "cacheId": "5ijOrjw3kg4J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/gigya/efd4f720-56c9-478c-bb30-3f6601340c66",
        "htmlFormattedUrl": "https://jobs.lever.co/gigya/efd4f720-56c9-478c-bb30-3f6601340c66",
        "htmlSnippet": "Your primary challenge will be to lead a team of experienced programmers <br>\ndeveloping our SaaS based user management system. The team develops <br>\nGigya&#39;s&nbsp;...",
        "htmlTitle": "Gigya - <b>C#</b> Server Side Team Leader",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/gigya/efd4f720-56c9-478c-bb30-3f6601340c66",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1483032404076.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRLsnFc0PMcFFI43P6jdsIQvSM0sUMq_MtuIf76o8aytrt35QzTPnDNptqi",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "Gigya is looking for an experienced, talented team leader ready to take on the challenge of developing our core services. About The Position: Your primary challenge will be to lead a team of experienced programmers developing our SaaS based user management system. The team develops Gigya\u2019s core systems that run at massive scale. You will take an active part on the designing and planning systems with other great team leaders, the head of R&D and our VP architect.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1483032404076.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Gigya - C# Server Side Team Leader",
                    "og:url": "https://jobs.lever.co/gigya/efd4f720-56c9-478c-bb30-3f6601340c66",
                    "twitter:description": "Gigya is looking for an experienced, talented team leader ready to take on the challenge of developing our core services. About The Position: Your primary challenge will be to lead a team of experienced programmers developing our SaaS based user management system. The team develops Gigya\u2019s core systems that run at massive scale. You will take an active part on the designing and planning systems with other great team leaders, the head of R&D and our VP architect.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1481204313579.png",
                    "twitter:title": "Gigya - C# Server Side Team Leader",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Your primary challenge will be to lead a team of experienced programmers \ndeveloping our SaaS based user management system. The team develops \nGigya's\u00a0...",
        "title": "Gigya - C# Server Side Team Leader"
    },
    {
        "cacheId": "KHQNFtMj29wJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../cacae7e7-f303-4af4-ab11-c6dfea2c3498",
        "htmlFormattedUrl": "https://jobs.lever.co/.../cacae7e7-f303-4af4-ab11-c6dfea2c3498",
        "htmlSnippet": "This <b>C#</b> Developer will support the Factsheet platform by working on product <br>\nfeatures and enhancements raised by the Factsheet team. Key duties include&nbsp;...",
        "htmlTitle": "Kurtosys - <b>C#</b> Developer - Factsheet Reporting",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/kurtosys/cacae7e7-f303-4af4-ab11-c6dfea2c3498",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/3cfa711a-651a-409a-a7d4-5ad27c30a140-1502985410952.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "163",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRW0uyyg-xHU5g0NOw_rEfOxsbOZ0CK3NTxu-zNQ9McRq5qsg0KSkqu_-YP",
                    "width": "310"
                }
            ],
            "metatags": [
                {
                    "og:description": "INTRODUCTION This C# Developer will support the Factsheet platform by working on product features and enhancements raised by the Factsheet team. Key duties include taking requirements from users and customers and incorporating these into standard product features, responding to issues by investigating problems and providing hotfixes, and providing assistance on configuration questions and best practices. The C# Developer will work closely with Engineering and Factsheet Production teams locally, as well as other global Kurtosys offices.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/3cfa711a-651a-409a-a7d4-5ad27c30a140-1502985410952.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Kurtosys - C# Developer - Factsheet Reporting",
                    "og:url": "https://jobs.lever.co/kurtosys/cacae7e7-f303-4af4-ab11-c6dfea2c3498",
                    "twitter:description": "INTRODUCTION This C# Developer will support the Factsheet platform by working on product features and enhancements raised by the Factsheet team. Key duties include taking requirements from users and customers and incorporating these into standard product features, responding to issues by investigating problems and providing hotfixes, and providing assistance on configuration questions and best practices. The C# Developer will work closely with Engineering and Factsheet Production teams locally, as well as other global Kurtosys offices.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/3cfa711a-651a-409a-a7d4-5ad27c30a140-1502985405500.png",
                    "twitter:title": "Kurtosys - C# Developer - Factsheet Reporting",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "This C# Developer will support the Factsheet platform by working on product \nfeatures and enhancements raised by the Factsheet team. Key duties include\u00a0...",
        "title": "Kurtosys - C# Developer - Factsheet Reporting"
    }
]

# #local manual per listing test
def get_job_listings_from_google():
    data_get_job_listings_from_google = results_from_GSE_query
    return data_get_job_listings_from_google

#Post GSE query
# def get_job_listings_from_google(number_of_listings_to_get = 100):
#     return_value = []
#     for search_result_number_from_which_api_query_results_start in range(1, number_of_listings_to_get + 1, MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY):
#         return_value.extend(do_google_search(
#             # https://i.codefor.cash/job_alerts/generate_subscriber_keywords
#             search_term='site:jobs.lever.co go engineer',
#             api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN,
#             num=MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY,
#             # start=1))
#             start=search_result_number_from_which_api_query_results_start))
#     return return_value[:number_of_listings_to_get]

# def save_prePost_listings(listings):
#     with open('prePostListings.txt','a+') as f:
#         f.write(json.dumps(send_job_listings_to_codeforcash(get_job_listings_from_google()), sort_keys = True,
#                 indent = 4))

# def save_gse_call_results(listings):
#     with open('finalResults.txt','a+') as f:
#         f.write(json.dumps(get_job_listings_from_google(), sort_keys = True,
#                 indent = 4))

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
            print(web_data)

            # search for/iterate over bad words here then if true continue without running "for data_key in data_to_send_in_request_body:" for loop
            
            

            # # save file with Lynx descriptions
            # with open('preCheckDescriptions.txt','a+') as f:
            #     f.write(json.dumps(web_data))

            data_to_send_in_request_body["description"] = web_data

            for data_key in data_to_send_in_request_body:
                # data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key].encode('UTF8').decode('utf-8')
                data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key]

            # # print prePostListings before post to c4c
            # with open('prePostListings.txt','a+') as f:
            #     f.write(json.dumps(data_to_send_in_request_body))

            #test print json formatted complete listing
            # print(data_to_send_in_request_body)
    
        # # send formatted json to code4cash api
        # response_per_post = requests.post(
        #     url=CODEFORCASH_BASE_URL+'/api/metum/create',
        #     data=data_to_send_in_request_body)
        # # save code4cash response
        # with open('responseFromCodeforcash','ab+') as f:
        #     pickle.dump(response_per_post, f)

if __name__ == '__main__':
    send_job_listings_to_codeforcash(get_job_listings_from_google())
    # save_gse_call_results(send_job_listings_to_codeforcash(get_job_listings_from_google()))

    # save_gse_call_results(send_job_listings_to_codeforcash(remove_non_ascii(get_job_listings_from_google())))

    # send_job_listings_to_codeforcash(return_value)
    # save_gse_call_results(return_value)

    # save_result_of_sending_job_listings_to_codeforcash(send_job_listings_to_codeforcash(return_value))

    # save_gse_call_results(get_job_listings_from_google())

    # save_result_of_sending_job_listings_to_codeforcash(
    #     get_job_listings_from_google())
        
