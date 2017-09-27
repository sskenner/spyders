import json, codecs, requests, pickle, datetime
from googleapiclient.discovery import build 
from itertools import repeat

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

def do_google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def get_job_listings_from_google(number_of_listings_to_get = 1):
    return_value = []
    for search_result_number_from_which_api_query_results_start in range(1, number_of_listings_to_get + 1, MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY):
        return_value.extend(do_google_search(
            search_term='scala+remote site:jobs.lever.co',
            api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN,
            num=MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY,
            start=search_result_number_from_which_api_query_results_start))
    return return_value[:number_of_listings_to_get]

def save_api_call_results(listings):
    with open('finalResults.txt','ab+') as f:
        f.write(json.dumps(get_job_listings_from_google(), sort_keys = True,
                indent = 4))
        # f.write(json.dumps(get_job_listings_from_google(), sort_keys = True,
        #         indent = 4))

def send_job_listings_to_codeforcash(listings):
    for listing in range(len(listings)):
        data_to_send_in_request_body = {
            'key': CODEFORCASH_API_KEY,
            'title': listings[listing]['title'],
            'website': listings[listing]['link'],
            'description': listings[listing]['snippet'],
            'utc_datetime': datetime.datetime.utcnow().isoformat(),
            'lat': '',
            'lng': '',
            'country': '',
            'employment_type': '',
            'remote_ok': '',
            'time_commitment': ''
        }
        for data_key in data_to_send_in_request_body:
            data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key].replace(chr(127), '')
        
        # print(data_to_send_in_request_body)
        
        response_per_post = requests.post(
            url=CODEFORCASH_BASE_URL+'/api/metum/create',
            data=data_to_send_in_request_body)
        
        with open('responseFromCodeforcash','ab+') as f:
            pickle.dump(response_per_post, f)

# def save_result_of_sending_job_listings_to_codeforcash(listings):
#     with open('responseFromCodeforcash','ab+') as f:
#         pickle.dump(send_job_listings_to_codeforcash(return_value), f)

if __name__ == '__main__':
    save_api_call_results(send_job_listings_to_codeforcash(get_job_listings_from_google()))

    # send_job_listings_to_codeforcash(return_value)
    # save_api_call_results(return_value)

    # save_result_of_sending_job_listings_to_codeforcash(send_job_listings_to_codeforcash(return_value))

    # save_api_call_results(get_job_listings_from_google())

    # save_result_of_sending_job_listings_to_codeforcash(
    #     get_job_listings_from_google())
        
