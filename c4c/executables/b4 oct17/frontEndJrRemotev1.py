import json, codecs, requests, pickle, datetime
from googleapiclient.discovery import build

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

NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN = 'ssk'

API_KEY_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['api_key']
CSE_ID_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['cse_id']

CODEFORCASH_BASE_URL = 'https://i.codefor.cash'
CODEFORCASH_API_KEY = '5b26197b391c5dab05c5606d43fba9c6'

def do_google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def get_job_listings_from_google():
    results = []
    for number_of_search_result_being_processed in range(1,31):
        results.append(do_google_search(
            search_term='junior+remote site:jobs.lever.co',
            api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN,
            num=1, start=number_of_search_result_being_processed)[0])
    return results
    

def save_api_call_results():
    with open('finalResults.txt','w') as f:
        f.write(json.dumps(get_job_listings_from_google(), sort_keys = True,
                indent = 4))

def send_job_listings_to_codeforcash(listings):
    data_to_send_in_request_body = {
        'key': CODEFORCASH_API_KEY,
        'title': listings[0]['title'],
        'website': listings[0]['link'],
        'desciption': listings[0]['snippet'],
        'utc_datetime': datetime.datetime.utcnow().isoformat(),
        'lat': '',
        'lng': '',
        'country': '',
        'employment_type': '',
        'remote_ok': '',
        'time_commitment': ''
    }
    return requests.post(
        url=CODEFORCASH_BASE_URL+'/api/metum/create',
        data=data_to_send_in_request_body)


def save_result_of_sending_job_listings_to_codeforcash(listings):
    with open('responseFromCodeforcash','wb') as f:
        pickle.dump(send_job_listings_to_codeforcash(listings), f)


if __name__ == '__main__':
    save_result_of_sending_job_listings_to_codeforcash(
        get_job_listings_from_google())
