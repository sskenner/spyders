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

CSE_SEARCH_TERM = 'engineer software site:jobs.lever.co/'

CSE_INDEX_START = 1

client = ['brightedge']

def do_google_search(search_term=CSE_SEARCH_TERM, api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN, start=CSE_INDEX_START, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term + client[0], cx=cse_id, start=start, **kwargs).execute()
    print(res['queries']['request'][0]['totalResults'])
    return res['items']
    
    # print(res['items'])

# results_from_GSE_query = []

# #local manual per listing test
# def get_job_listings_from_google():
#     data_get_job_listings_from_google = results_from_GSE_query
#     return data_get_job_listings_from_google

# def get_job_listings_from_google(number_of_listings_to_get = 100):
#     return_value = []
#      # range(x, ...) = index to start from
#     for search_result_number_from_which_api_query_results_start in range(1, number_of_listings_to_get + 1, MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY):
#         return_value.extend(do_google_search(
#             # https://i.codefor.cash/job_alerts/generate_subscriber_keywords
#             # 'site:jobs.lever.co "c++" +engineer'
#             search_term='engineer software site:jobs.lever.co/brightedge/',
#             api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN, num=MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY,
#             # start=1))
#             start=search_result_number_from_which_api_query_results_start))
#     return return_value[:number_of_listings_to_get]

def save_gse_call_results(listings):
    with open('finalResults.txt','a+') as f:
        f.write(json.dumps(do_google_search(), sort_keys = True,
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
            try:
                f.write(htmlDecode)
            except:
                print('POTENTIAL ENCODE ERROR')
            f.close()

            #refactor as functions
            web_data = ''
            cmd = 'lynx -dump -width 1024 -nolist -notitle \"{0}\"'.format('./Lynx.htm')
            lynx = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            web_data = lynx.stdout.read()
            web_data = web_data.decode('utf-8', 'replace')
            
            #test print url and lynx formatted description
            print(data_of_each_listing["website"])
            # print(web_data)

            data_to_send_in_request_body["description"] = web_data

            for data_key in data_to_send_in_request_body:
                # data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key].encode('UTF8').decode('utf-8')
                data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key]

            # #test print json formatted complete listing
            # print(data_to_send_in_request_body)
    
        # response_per_post = requests.post(
        #     url=CODEFORCASH_BASE_URL+'/api/metum/create',
        #     data=data_to_send_in_request_body)
        
        # with open('responseFromCodeforcash','ab+') as f:
        #     pickle.dump(response_per_post, f)

if __name__ == '__main__':
    # save_gse_call_results(send_job_listings_to_codeforcash(do_google_search()))
    send_job_listings_to_codeforcash(do_google_search())

    # save_gse_call_results(send_job_listings_to_codeforcash(remove_non_ascii(get_job_listings_from_google())))

    # send_job_listings_to_codeforcash(return_value)
    # save_gse_call_results(return_value)

    # save_result_of_sending_job_listings_to_codeforcash(send_job_listings_to_codeforcash(return_value))

    # save_gse_call_results(get_job_listings_from_google())

    # save_result_of_sending_job_listings_to_codeforcash(
    #     get_job_listings_from_google())
        
