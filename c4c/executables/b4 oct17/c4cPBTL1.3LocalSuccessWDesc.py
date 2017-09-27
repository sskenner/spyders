import json, codecs, requests, pickle, datetime
import urllib.request, urllib.parse, urllib.error
from googleapiclient.discovery import build 
from itertools import repeat
from unidecode import unidecode
from bs4 import BeautifulSoup

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
        "cacheId": "11RdFUJdzOwJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/roam/ca9b536d-592b-4755-b03a-14df06274743",
        "htmlFormattedUrl": "https://jobs.lever.co/roam/ca9b536d-592b-4755-b03a-14df06274743",
        "htmlSnippet": "... Extensive experience working with and setting up different big data stores like <br>\nElasticsearch, MongoDB, RDBMS, HDFS, Cassandra, <b>Neo4j</b>; Experience with&nbsp;...",
        "htmlTitle": "Roam - ML Platform Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/roam/ca9b536d-592b-4755-b03a-14df06274743",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/6cad6bfb-f63b-425e-86f6-16dd7281377c-1475234623144.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "123",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUtAZ0Rch-nyJ0U9NXfsjssNQUkXZ0y27BKREhavAHXBVWiAmhV-5ZhA",
                    "width": "409"
                }
            ],
            "metatags": [
                {
                    "og:description": "At Roam, our mission is to dramatically improve the health of the world\u2019s population by bringing comprehensive knowledge to patients, providers, professionals, and companies. Roam is developing a machine learning and data platform that powers rich analysis of patient journeys and factors affecting treatment decisions. Analysis built on this platform enables life sciences organizations and health care providers to better leverage large, disparate data sources to identify and improve patterns of care. The Roam platform is powered by machine learning and a proprietary data asset we call the Health Knowledge Graph. The Health Knowledge Graph converts billions of disparate, often unstructured, data elements into a coherent picture of healthcare. The relationships and information captured in the Graph are continuously enriched using machine learning and natural language processing to extract more information, and by making connections to new data sources. The result is an unprecedented,",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/6cad6bfb-f63b-425e-86f6-16dd7281377c-1475234623144.png",
                    "og:image:height": "200",
                    "og:title": "Roam - ML Platform Engineer",
                    "og:url": "https://jobs.lever.co/roam/ca9b536d-592b-4755-b03a-14df06274743",
                    "twitter:description": "At Roam, our mission is to dramatically improve the health of the world\u2019s population by bringing comprehensive knowledge to patients, providers, professionals, and companies. Roam is developing a machine learning and data platform that powers rich analysis of patient journeys and factors affecting treatment decisions. Analysis built on this platform enables life sciences organizations and health care providers to better leverage large, disparate data sources to identify and improve patterns of care. The Roam platform is powered by machine learning and a proprietary data asset we call the Health Knowledge Graph. The Health Knowledge Graph converts billions of disparate, often unstructured, data elements into a coherent picture of healthcare. The relationships and information captured in the Graph are continuously enriched using machine learning and natural language processing to extract more information, and by making connections to new data sources. The result is an unprecedented,",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/6cad6bfb-f63b-425e-86f6-16dd7281377c-1475234634202.png",
                    "twitter:title": "Roam - ML Platform Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... Extensive experience working with and setting up different big data stores like \nElasticsearch, MongoDB, RDBMS, HDFS, Cassandra, Neo4j; Experience with\u00a0...",
        "title": "Roam - ML Platform Engineer"
    }
]

def get_job_listings_from_google():
    data_get_job_listings_from_google = results_from_GSE_query
    return data_get_job_listings_from_google

def save_api_call_results(listings):
    with open('finalResults.txt','a+') as f:
        f.write(json.dumps(get_job_listings_from_google(), sort_keys = True,
                indent = 4))
#
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
            # data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key].replace(chr(128), '')
        
        data_send_job_lisitings_to_codeforcash = json.dumps(data_to_send_in_request_body)

        data_of_each_listing = json.loads(data_send_job_lisitings_to_codeforcash)
        
        #>>> break if no site available
        try:
            html = urllib.request.urlopen(data_of_each_listing["website"]).read()
        except urllib.error.HTTPError as e:
            print(e)
        else:
            soup = BeautifulSoup(urllib.request.urlopen(data_of_each_listing["website"]).read(), 'html.parser')
        
            # title_tag = soup.title.contents[0]
            description_array = []
            for row in soup.find_all("div", attrs={"class" : "section section page-centered"}):
                description_array.append(row.text)
            description = "\n\n".join(description_array)
            # for row in (soup.find_all('li'):
            #     description_array.append(row.text)
            # description = "\n".join(description_array)

            data_to_send_in_request_body["description"] =description

            for data_key in data_to_send_in_request_body:
                data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key].encode('UTF8')
            # print(data_to_send_in_request_body)
        
            response_per_post = requests.post(
                url=CODEFORCASH_BASE_URL+'/api/metum/create',
                data=data_to_send_in_request_body)
            
            with open('responseFromCodeforcash','ab+') as f:
                pickle.dump(response_per_post, f)

# def remove_non_ascii(listings):
#     # for list in listings:
#     #     list.encode('UTF8')
#     unidecode(unicode(listings, encoding = "utf-8"))

# def save_result_of_sending_job_listings_to_codeforcash(listings):
#     with open('responseFromCodeforcash','ab+') as f:
#         pickle.dump(send_job_listings_to_codeforcash(return_value), f)

if __name__ == '__main__':
    save_api_call_results(send_job_listings_to_codeforcash(get_job_listings_from_google()))

    # save_api_call_results(send_job_listings_to_codeforcash(remove_non_ascii(get_job_listings_from_google())))

    # send_job_listings_to_codeforcash(return_value)
    # save_api_call_results(return_value)

    # save_result_of_sending_job_listings_to_codeforcash(send_job_listings_to_codeforcash(return_value))

    # save_api_call_results(get_job_listings_from_google())

    # save_result_of_sending_job_listings_to_codeforcash(
    #     get_job_listings_from_google())
        
