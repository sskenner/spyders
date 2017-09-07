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
    {#"code":11 .. where is it?
        "cacheId": "--feGDrX2G0J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../3ad0e81a-ae43-48bd-a46a-2dde5a21b559",
        "htmlFormattedUrl": "https://jobs.lever.co/.../3ad0e81a-ae43-48bd-a46a-2dde5a21b559",
        "htmlSnippet": "The <b>Junior</b> Developer role will be fast paced from the moment you start; you will <br>\n... for the web, Hibernate, or any other persistence framework HTML/<b>JavaScript</b>/&nbsp;...",
        "htmlTitle": "RealDecoy - <b>Junior</b> Web Application Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/realdecoy.com/3ad0e81a-ae43-48bd-a46a-2dde5a21b559",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f956f020-8a8c-4eab-9384-b861ac443b41-1462393738256.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "34",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQYNds_tkLBKHSwiIi0xjxyrSN6Skc0nvmVeD_KjdYAch4PFsSLB_5mAg",
                    "width": "174"
                }
            ],
            "metatags": [
                {
                    "og:description": "RealDecoy is seeking to add a new Developer to the Ottawa team. The Junior Developer role will be fast paced from the moment you start; you will be learning new technologies, new ways of working and you will be collaborating with a variety of clients to ensure that we provide the best possible service to them. You will be responsible for implementing web sites and web applications using Java and related technologies. You will have the opportunity to work on concurrent projects with other professional developers, technical leads, project managers and planners. You will be expected to keep current of new and emerging techniques, understand when and how they can be applied to projects and assist in documenting trusted best practices. Typically, you will be required to: o Assist in designing the deployment architecture for web-based applications. o Perform program modifications following detailed technical specifications and resolve programming problems. o Create detailed technical specif",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f956f020-8a8c-4eab-9384-b861ac443b41-1462393738256.png",
                    "og:image:height": "200",
                    "og:title": "RealDecoy - Junior Web Application Developer",
                    "og:url": "https://jobs.lever.co/realdecoy.com/3ad0e81a-ae43-48bd-a46a-2dde5a21b559",
                    "twitter:description": "RealDecoy is seeking to add a new Developer to the Ottawa team. The Junior Developer role will be fast paced from the moment you start; you will be learning new technologies, new ways of working and you will be collaborating with a variety of clients to ensure that we provide the best possible service to them. You will be responsible for implementing web sites and web applications using Java and related technologies. You will have the opportunity to work on concurrent projects with other professional developers, technical leads, project managers and planners. You will be expected to keep current of new and emerging techniques, understand when and how they can be applied to projects and assist in documenting trusted best practices. Typically, you will be required to: o Assist in designing the deployment architecture for web-based applications. o Perform program modifications following detailed technical specifications and resolve programming problems. o Create detailed technical specif",
                    "twitter:title": "RealDecoy - Junior Web Application Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "The Junior Developer role will be fast paced from the moment you start; you will \n... for the web, Hibernate, or any other persistence framework HTML/JavaScript/\u00a0...",
        "title": "RealDecoy - Junior Web Application Developer"
    }
    # ,
    # {
    #     "cacheId": "sXmI99FsxgoJ",
    #     "displayLink": "jobs.lever.co",
    #     "formattedUrl": "https://jobs.lever.co/.../279677f7-02a3-4d89-a0b8-327a1624c4ea",
    #     "htmlFormattedUrl": "https://jobs.lever.co/.../279677f7-02a3-4d89-a0b8-327a1624c4ea",
    #     "htmlSnippet": "5+ years of hands-on product experience; \u201c<b>Junior</b>\u201d level experience with <br>\n<b>JavaScript</b> is desired. We&#39;ll train you to become effective with React.js; <br>\nWillingness to&nbsp;...",
    #     "htmlTitle": "Credit Karma - Senior Designer/UI Developer",
    #     "kind": "customsearch#result",
    #     "link": "https://jobs.lever.co/creditkarma/279677f7-02a3-4d89-a0b8-327a1624c4ea",
    #     "pagemap": {
    #         "cse_image": [
    #             {
    #                 "src": "https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png"
    #             }
    #         ],
    #         "cse_thumbnail": [
    #             {
    #                 "height": "159",
    #                 "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE",
    #                 "width": "318"
    #             }
    #         ],
    #         "metatags": [
    #             {
    #                 "og:description": "As a member of the credit cards experimentation team, you will need both design and some technical skills. You\u2019ll be the lead visual designer in a team of data-centric full stack engineers and product managers. You\u2019ll work closely within this cross-functional team to advocate for rapid experimentation and lean UX. Your main goal is to help Credit Karma increase the pace of our learnings. From an engineering perspective, your priority will be to develop scalable design systems (components, style guides etc) that can be used to ship products quickly.",
    #                 "og:image": "https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png",
    #                 "og:image:height": "630",
    #                 "og:image:width": "1200",
    #                 "og:title": "Credit Karma - Senior Designer/UI Developer",
    #                 "og:url": "https://jobs.lever.co/creditkarma/279677f7-02a3-4d89-a0b8-327a1624c4ea",
    #                 "twitter:description": "As a member of the credit cards experimentation team, you will need both design and some technical skills. You\u2019ll be the lead visual designer in a team of data-centric full stack engineers and product managers. You\u2019ll work closely within this cross-functional team to advocate for rapid experimentation and lean UX. Your main goal is to help Credit Karma increase the pace of our learnings. From an engineering perspective, your priority will be to develop scalable design systems (components, style guides etc) that can be used to ship products quickly.",
    #                 "twitter:image": "https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png",
    #                 "twitter:title": "Credit Karma - Senior Designer/UI Developer",
    #                 "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
    #             }
    #         ]
    #     },
    #     "snippet": "5+ years of hands-on product experience; \u201cJunior\u201d level experience with \nJavaScript is desired. We'll train you to become effective with React.js; \nWillingness to\u00a0...",
    #     "title": "Credit Karma - Senior Designer/UI Developer"
    # }
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
    
        # response_per_post = requests.post(
        #     url=CODEFORCASH_BASE_URL+'/api/metum/create',
        #     data=data_to_send_in_request_body)
        
        # with open('responseFromCodeforcash','ab+') as f:
        #     pickle.dump(response_per_post, f)

if __name__ == '__main__':
    save_gse_call_results(send_job_listings_to_codeforcash(get_job_listings_from_google()))

    # save_gse_call_results(send_job_listings_to_codeforcash(remove_non_ascii(get_job_listings_from_google())))

    # send_job_listings_to_codeforcash(return_value)
    # save_gse_call_results(return_value)

    # save_result_of_sending_job_listings_to_codeforcash(send_job_listings_to_codeforcash(return_value))

    # save_gse_call_results(get_job_listings_from_google())

    # save_result_of_sending_job_listings_to_codeforcash(
    #     get_job_listings_from_google())
        
