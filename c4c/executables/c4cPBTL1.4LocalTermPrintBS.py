import json, codecs, requests, pickle, datetime
import urllib.request, urllib.parse, urllib.error
import html2text
import re
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

# CODEFORCASH_BASE_URL = 'https://i.codefor.cash'
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
    },
    # burned
    {
        "cacheId": "5-E22_ck7ZMJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../a631deac-26d8-491d-9238-400a206e40f4",
        "htmlFormattedUrl": "https://jobs.lever.co/.../a631deac-26d8-491d-9238-400a206e40f4",
        "htmlSnippet": "... asynchronous code; Database experience using CoreData, <b>SQLite</b> or <br>\nequivalent; Attention to quality through unit tests, automation scripts, and code <br>\nreviews&nbsp;...",
        "htmlTitle": "Eventbrite - Senior Mobile Software Engineer - iOS",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/eventbrite/a631deac-26d8-491d-9238-400a206e40f4",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1488492166844.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "225",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTTvFuICOfdvSfhbE4ObHsOali-3FCbYdpz22h0yVaHrVVzEgqRWhDCgXU",
                    "width": "225"
                }
            ],
            "metatags": [
                {
                    "og:description": "THE TEAM At Eventbrite we tackle tough problems. We learn, grow, and have fun in the process. The women and men of Eventbrite\u2019s Engineering team enjoy facing challenges as individuals, but we are also eager to collaborate and share our knowledge to drive the product forward. The Nashville Engineering team is charged with building our next generation organizer app, and the APIs and services that power it. We perform weekly demos of the code we ship, hone our skills through code reviews, and tell the world about it on Eventbrite\u2019s Engineering Blog. We believe in the value of community and the power of live experiences, and regularly host free events with top technical speakers. THE CHALLENGE We are committed to building an amazing user experience that both looks and feels great, and that we\u2019re shipping the highest quality apps possible. Our organizer apps power businesses of all sizes, from smaller conferences to massive international food, film, and music festivals. Their performance",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1488492166844.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Eventbrite - Senior Mobile Software Engineer - iOS",
                    "og:url": "https://jobs.lever.co/eventbrite/a631deac-26d8-491d-9238-400a206e40f4",
                    "twitter:description": "THE TEAM At Eventbrite we tackle tough problems. We learn, grow, and have fun in the process. The women and men of Eventbrite\u2019s Engineering team enjoy facing challenges as individuals, but we are also eager to collaborate and share our knowledge to drive the product forward. The Nashville Engineering team is charged with building our next generation organizer app, and the APIs and services that power it. We perform weekly demos of the code we ship, hone our skills through code reviews, and tell the world about it on Eventbrite\u2019s Engineering Blog. We believe in the value of community and the power of live experiences, and regularly host free events with top technical speakers. THE CHALLENGE We are committed to building an amazing user experience that both looks and feels great, and that we\u2019re shipping the highest quality apps possible. Our organizer apps power businesses of all sizes, from smaller conferences to massive international food, film, and music festivals. Their performance",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1476237511604.png",
                    "twitter:title": "Eventbrite - Senior Mobile Software Engineer - iOS",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... asynchronous code; Database experience using CoreData, SQLite or \nequivalent; Attention to quality through unit tests, automation scripts, and code \nreviews\u00a0...",
        "title": "Eventbrite - Senior Mobile Software Engineer - iOS"
    }
    ,
    # burned
    {
        "cacheId": "Al6HsfetCYYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../1deb20ec-ca6a-4807-8f43-74274104cd44",
        "htmlFormattedUrl": "https://jobs.lever.co/.../1deb20ec-ca6a-4807-8f43-74274104cd44",
        "htmlSnippet": "(<b>sqlite</b>, core data or equivalent. Strong understanding of concurrent programming <br>\narchitecture and best practices. Native UI development experience, especially&nbsp;...",
        "htmlTitle": "Livongo - Mobile Software Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/livongo/1deb20ec-ca6a-4807-8f43-74274104cd44",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/38293ecd-7516-43c9-9ddc-fe79b3423292-1492034311715.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "96",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWCaK8TdoDDI129m9h0cMBdxayzjfK6GcbVsMmlBXpTEU_ytFll3q7Xt0",
                    "width": "524"
                }
            ],
            "metatags": [
                {
                    "og:description": "Livongo is looking for a smart and capable mobile application engineer to join our ranks. The ideal candidate should have a passion for working on technology that is transformative and crucially important to helping the lives of those impacted by one of the fastest growing chronic conditions in the world. We are building an end to end service that integrates seamlessly into the lives of those affected by diabetes via a multitude of touchpoints on the front end while providing intelligent integrations and analytics on the backend. We value engineers that strive for excellence and have a sense of compassion and urgency to solving one of the most pressing healthcare crises of our generation.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/38293ecd-7516-43c9-9ddc-fe79b3423292-1492034311715.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Livongo - Mobile Software Engineer",
                    "og:url": "https://jobs.lever.co/livongo/1deb20ec-ca6a-4807-8f43-74274104cd44",
                    "twitter:description": "Livongo is looking for a smart and capable mobile application engineer to join our ranks. The ideal candidate should have a passion for working on technology that is transformative and crucially important to helping the lives of those impacted by one of the fastest growing chronic conditions in the world. We are building an end to end service that integrates seamlessly into the lives of those affected by diabetes via a multitude of touchpoints on the front end while providing intelligent integrations and analytics on the backend. We value engineers that strive for excellence and have a sense of compassion and urgency to solving one of the most pressing healthcare crises of our generation.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/38293ecd-7516-43c9-9ddc-fe79b3423292-1492034291479.png",
                    "twitter:title": "Livongo - Mobile Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "(sqlite, core data or equivalent. Strong understanding of concurrent programming \narchitecture and best practices. Native UI development experience, especially\u00a0...",
        "title": "Livongo - Mobile Software Engineer"
    }
    ,
    # burned
    {
        "cacheId": "Q2vxZkEZDQ0J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../660b02d8-6701-4499-9768-fbe1fceca9aa",
        "htmlFormattedUrl": "https://jobs.lever.co/.../660b02d8-6701-4499-9768-fbe1fceca9aa",
        "htmlSnippet": "... Experience with using databases (mysql, postgresql, <b>sqlite</b>); Experience with <br>\nGoogle Cloud or AWS; Experience using container technology (docker, coreOS,<br>\n&nbsp;...",
        "htmlTitle": "Bay Labs - Full-stack Software Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/baylabs/660b02d8-6701-4499-9768-fbe1fceca9aa",
        "pagemap": {
            "metatags": [
                {
                    "og:description": "Bay Labs is at the forefront of bringing deep learning advances to critical unsolved healthcare problems. We have gathered an extraordinary team of clinicians, engineers, and scientists who are developing breakthrough technologies in cardiovascular imaging and care addressing the largest cause of death in the US. Bay Labs has a diverse technical expertise with leaders in machine learning, visual neuroscience, robotics, and physics. We collaborate with a network of world renowned clinical and academic advisors, progressing in a very short period of time. Current investors in Bay Labs are recognized leaders in venture capital. The Full-Stack Software Engineer will be a core member of the Bay Labs engineering team responsible for full-stack development and deployment of our products and services.",
                    "og:image:height": "200",
                    "og:title": "Bay Labs - Full-stack Software Engineer",
                    "og:url": "https://jobs.lever.co/baylabs/660b02d8-6701-4499-9768-fbe1fceca9aa",
                    "twitter:description": "Bay Labs is at the forefront of bringing deep learning advances to critical unsolved healthcare problems. We have gathered an extraordinary team of clinicians, engineers, and scientists who are developing breakthrough technologies in cardiovascular imaging and care addressing the largest cause of death in the US. Bay Labs has a diverse technical expertise with leaders in machine learning, visual neuroscience, robotics, and physics. We collaborate with a network of world renowned clinical and academic advisors, progressing in a very short period of time. Current investors in Bay Labs are recognized leaders in venture capital. The Full-Stack Software Engineer will be a core member of the Bay Labs engineering team responsible for full-stack development and deployment of our products and services.",
                    "twitter:title": "Bay Labs - Full-stack Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... Experience with using databases (mysql, postgresql, sqlite); Experience with \nGoogle Cloud or AWS; Experience using container technology (docker, coreOS,\n\u00a0...",
        "title": "Bay Labs - Full-stack Software Engineer"
    }
    ,
    {
        "cacheId": "RJcRJMCSptQJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../7356ec04-84ca-4db8-810a-562ac67312da",
        "htmlFormattedUrl": "https://jobs.lever.co/.../7356ec04-84ca-4db8-810a-562ac67312da",
        "htmlSnippet": "Knowledge Android SDK, <b>SQLite</b>, MySQL or similar database management <br>\nsystem. \u00b7 Familiar with AndroidStudio. Understanding of other compiled <br>\nlanguages:.",
        "htmlTitle": "Telmate - Senior Mobile Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/telmate/7356ec04-84ca-4db8-810a-562ac67312da",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/telmate_logo_450.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQr0M3Pt0ieinKs2L87yS7pQhAf5z7Rg53cpK1oCTL9meCRWSDNt_upY2c",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "The Senior Mobile Application Engineer leads the development and maintenance of Android and iPhone apps. In addition to delivering the product, this is heavily involved in driving mobile strategy across all platforms. This role is heavy on the Android side, with kernel-level development skills needed.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/telmate_logo_450.png",
                    "og:image:height": "200",
                    "og:title": "Telmate - Senior Mobile Engineer",
                    "og:url": "https://jobs.lever.co/telmate/7356ec04-84ca-4db8-810a-562ac67312da",
                    "twitter:description": "The Senior Mobile Application Engineer leads the development and maintenance of Android and iPhone apps. In addition to delivering the product, this is heavily involved in driving mobile strategy across all platforms. This role is heavy on the Android side, with kernel-level development skills needed.",
                    "twitter:title": "Telmate - Senior Mobile Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Knowledge Android SDK, SQLite, MySQL or similar database management \nsystem. \u00b7 Familiar with AndroidStudio. Understanding of other compiled \nlanguages:.",
        "title": "Telmate - Senior Mobile Engineer"
    }
]

def get_job_listings_from_google():
    data_get_job_listings_from_google = results_from_GSE_query
    return data_get_job_listings_from_google

# def get_job_listings_from_google(number_of_listings_to_get = 5):
#     return_value = []
#     for search_result_number_from_which_api_query_results_start in range(1, number_of_listings_to_get + 1, MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY):
#         return_value.extend(do_google_search(
#             # https://i.codefor.cash/job_alerts/generate_subscriber_keywords
#             search_term='sqlite site:jobs.lever.co',
#             api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN,
#             num=MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY,
#             start=1))
#             # start=search_result_number_from_which_api_query_results_start))
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

            # data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key].replace(chr(128), '')
        
        # print(data_send_job_lisitings_to_codeforcash)
        
        
        #>>> break if no site available
        try:
            html = urllib.request.urlopen(data_of_each_listing["website"]).read()
        except urllib.error.HTTPError as e:
            print(e)
        else:
            only_tag_class = SoupStrainer("div", {"class" : "section-wrapper page-full-width"})
            soup = BeautifulSoup(html, "html.parser", parse_only=only_tag_class)
            htmlDecode = soup.encode('utf-8').decode('utf-8', 'ignore')
            htmlText = html2text.html2text(htmlDecode)
            htmlTextJoined =re.sub(r'\n+', '\n',htmlText)
            # print(htmlText)
            # print(htmlTextJoined)
            data_to_send_in_request_body["description"] = htmlTextJoined

            for data_key in data_to_send_in_request_body:
                data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key].encode('utf-8')
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
    save_gse_call_results(send_job_listings_to_codeforcash(get_job_listings_from_google()))

    # save_gse_call_results(send_job_listings_to_codeforcash(remove_non_ascii(get_job_listings_from_google())))

    # send_job_listings_to_codeforcash(return_value)
    # save_gse_call_results(return_value)

    # save_result_of_sending_job_listings_to_codeforcash(send_job_listings_to_codeforcash(return_value))

    # save_gse_call_results(get_job_listings_from_google())

    # save_result_of_sending_job_listings_to_codeforcash(
    #     get_job_listings_from_google())
        
