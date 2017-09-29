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

CSE_SEARCH_TERM_PREFIX = "'software engineer' site:jobs.lever.co/"

# clients = ['brightedge']
# clients = ['brightedge', 'voleon']
# clients = ['brightedge', 'blendlabs', 'voleon']

def pass_different_clients():
    for client in clients:
        cse_search_term = CSE_SEARCH_TERM_PREFIX + client
        print(cse_search_term)
        get_job_listings_from_google(cse_search_term)


# def do_google_search(search_term, api_key, cse_id, **kwargs):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
#     # print(res['items'])
#     print(res['queries']['request'][0]['totalResults'])
#     return res['items']

results_from_GSE_query = [
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Software Engineer',
    'htmlTitle': 'Twitch - <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/twitch/a5f652d5-4f30-40ae-a860-14b869b5a445',
    'displayLink': 'jobs.lever.co',
    'snippet': "Not all Software Engineers fit neatly into a bucket. Luckily, neither do all of the \nthings that need to get done here at Twitch. If you're a smart engineer who's\xa0...",
    'htmlSnippet': 'Not all <b>Software Engineers</b> fit neatly into a bucket. Luckily, neither do all of the <br>\nthings that need to get done here at Twitch. If you&#39;re a smart engineer who&#39;s&nbsp;...',
    'cacheId': 'Q51oEA-WB0QJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/a5f652d5-4f30-40ae-a860-14b869b5a445',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/a5f652d5-4f30-40ae-a860-14b869b5a445',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Software Engineer',
          'twitter:description': "Not all Software Engineers fit neatly into a bucket. Luckily, neither do all of the things that need to get done here at Twitch. If you▒re a smart engineer who▒s capable of learning things on the fly and isn't afraid to venture into the unknown, Twitch is definitely the place for you. As a Software Engineer at Twitch, some things you may be working on are: Our chat system, which supports millions of concurrent users Our video distribution system, which is one of the largest in the world Elegant, highly-available web services to support one of our many front end platforms Front end web engineering that is functional, beautiful, and delightful Building applications for one of the many non-web platforms we support, including iOS, Android, XBox 360, XBox One, and Playstation 4 Building new features that millions of users will be seeing Helping build robust deployment tools to help us move forward rapidly Building great tools that lets us support our custom",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Software Engineer',
          'og:description': "Not all Software Engineers fit neatly into a bucket. Luckily, neither do all of the things that need to get done here at Twitch. If you▒re a smart engineer who▒s capable of learning things on the fly and isn't afraid to venture into the unknown, Twitch is definitely the place for you. As a Software Engineer at Twitch, some things you may be working on are: Our chat system, which supports millions of concurrent users Our video distribution system, which is one of the largest in the world Elegant, highly-available web services to support one of our many front end platforms Front end web engineering that is functional, beautiful, and delightful Building applications for one of the many non-web platforms we support, including iOS, Android, XBox 360, XBox One, and Playstation 4 Building new features that millions of users will be seeing Helping build robust deployment tools to help us move forward rapidly Building great tools that lets us support our custom",
          'og:url': 'https://jobs.lever.co/twitch/a5f652d5-4f30-40ae-a860-14b869b5a445',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/twitch/c795ef2d-2621-4383-8aa1-c85c8750bfa2',
    'displayLink': 'jobs.lever.co',
    'snippet': 'We are rapidly expanding the engineering team at Twitch to deal with \nchallenging scale problem of being the 4th biggest consumer of bandwidth and \none of the\xa0...',
    'htmlSnippet': 'We are rapidly expanding the <b>engineering</b> team at Twitch to deal with <br>\nchallenging scale problem of being the 4th biggest consumer of bandwidth and <br>\none of the&nbsp;...',
    'cacheId': 'IfDwOzBaIzwJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/c795ef2d-2621-4383-8aa1-c85c8750bfa2',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/c795ef2d-2621-4383-8aa1-c85c8750bfa2',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer',
          'twitter:description': 'We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Here▒s a short list of current scale: -Serve more than 150 million unique visitors per month -More than 2 million peak concurrent users -16 billion minutes of video watched each month and growing -10 billion messages sent on chat per day and growing -Serving 5 million+ requests per second on the edge and growing -Anticipated scale year-over-year = 2.5x -Current Engineering Team Size: ~100 People Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. We are looking for the next set of engineering te',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer',
          'og:description': 'We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Here▒s a short list of current scale: -Serve more than 150 million unique visitors per month -More than 2 million peak concurrent users -16 billion minutes of video watched each month and growing -10 billion messages sent on chat per day and growing -Serving 5 million+ requests per second on the edge and growing -Anticipated scale year-over-year = 2.5x -Current Engineering Team Size: ~100 People Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. We are looking for the next set of engineering te',
          'og:url': 'https://jobs.lever.co/twitch/c795ef2d-2621-4383-8aa1-c85c8750bfa2',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Software Engineer - Data',
    'htmlTitle': 'Twitch - <b>Software Engineer</b> - Data',
    'link': 'https://jobs.lever.co/twitch/889401a7-d917-4947-97d7-8a2d2e2fd430',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Twitch is building the future of interactive entertainment, and data is critical to \nevery decision we make. The Science Engineering team is looking for a \ndeveloper\xa0...',
    'htmlSnippet': 'Twitch is building the future of interactive entertainment, and data is critical to <br>\nevery decision we make. The Science <b>Engineering</b> team is looking for a <br>\ndeveloper&nbsp;...',
    'cacheId': 'fWiE9VK-OKMJ',
    'formattedUrl': 'https://jobs.lever.co/.../889401a7-d917-4947-97d7-8a2d2e2fd430',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../889401a7-d917-4947-97d7-8a2d2e2fd430',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Software Engineer - Data',
          'twitter:description': 'Twitch is building the future of interactive entertainment, and data is critical to every decision we make. The Science Engineering team is looking for a developer to help us meet all the diverse data needs within Twitch and to scale with those needs. Our team develops and operates the real-time behavioral data pipeline, which collects, processes, and distributes data to other teams. We provide data to systems and decision making throughout the company, and we have a constantly growing list of data consumers. The core pipeline is open source -- check out our code at github.com/twitchscience',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Software Engineer - Data',
          'og:description': 'Twitch is building the future of interactive entertainment, and data is critical to every decision we make. The Science Engineering team is looking for a developer to help us meet all the diverse data needs within Twitch and to scale with those needs. Our team develops and operates the real-time behavioral data pipeline, which collects, processes, and distributes data to other teams. We provide data to systems and decision making throughout the company, and we have a constantly growing list of data consumers. The core pipeline is open source -- check out our code at github.com/twitchscience',
          'og:url': 'https://jobs.lever.co/twitch/889401a7-d917-4947-97d7-8a2d2e2fd430',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Software Engineer - Tools',
    'htmlTitle': 'Twitch - <b>Software Engineer</b> - Tools',
    'link': 'https://jobs.lever.co/twitch/e689e043-c062-4421-9dde-e973c509b818',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Twitch is building the future of interactive entertainment, and video is at the very \ncore of that vision. Our engineering teams are solving problems to help deliver\xa0...',
    'htmlSnippet': 'Twitch is building the future of interactive entertainment, and video is at the very <br>\ncore of that vision. Our <b>engineering</b> teams are solving problems to help deliver&nbsp;...',
    'cacheId': 'zOu9V_lHScEJ',
    'formattedUrl': 'https://jobs.lever.co/.../e689e043-c062-4421-9dde-e973c509b818',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../e689e043-c062-4421-9dde-e973c509b818',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Software Engineer - Tools',
          'twitter:description': "Twitch is building the future of interactive entertainment, and video is at the very core of that vision. Our engineering teams are solving problems to help deliver the best content available. If you are passionate about building tools to automate 'all the things' and you're excited to support other talented developers all around you...Twitch is the place to be.",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Software Engineer - Tools',
          'og:description': "Twitch is building the future of interactive entertainment, and video is at the very core of that vision. Our engineering teams are solving problems to help deliver the best content available. If you are passionate about building tools to automate 'all the things' and you're excited to support other talented developers all around you...Twitch is the place to be.",
          'og:url': 'https://jobs.lever.co/twitch/e689e043-c062-4421-9dde-e973c509b818',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Software Engineer',
    'htmlTitle': 'Twitch - <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/twitch/a5f652d5-4f30-40ae-a860-14b869b5a445/',
    'displayLink': 'jobs.lever.co',
    'snippet': '7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\xa0...',
    'htmlSnippet': '7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...',
    'cacheId': '7Wdemj2vppAJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/a5f652d5-4f30-40ae-a860.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/a5f652d5-4f30-40ae-a860.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Software Engineer',
          'twitter:description': "Not all Software Engineers fit neatly into a bucket. Luckily, neither do all of the things that need to get done here at Twitch. If you▒re a smart engineer who▒s capable of learning things on the fly and isn't afraid to venture into the unknown, Twitch is definitely the place for you. As a Software Engineer at Twitch, some things you may be working on are: Our chat system, which supports millions of concurrent users Our video distribution system, which is one of the largest in the world Elegant, highly-available web services to support one of our many front end platforms Front end web engineering that is functional, beautiful, and delightful Building applications for one of the many non-web platforms we support, including iOS, Android, XBox 360, XBox One, and Playstation 4 Building new features that millions of users will be seeing Helping build robust deployment tools to help us move forward rapidly Building great tools that lets us support our custom",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Software Engineer',
          'og:description': "Not all Software Engineers fit neatly into a bucket. Luckily, neither do all of the things that need to get done here at Twitch. If you▒re a smart engineer who▒s capable of learning things on the fly and isn't afraid to venture into the unknown, Twitch is definitely the place for you. As a Software Engineer at Twitch, some things you may be working on are: Our chat system, which supports millions of concurrent users Our video distribution system, which is one of the largest in the world Elegant, highly-available web services to support one of our many front end platforms Front end web engineering that is functional, beautiful, and delightful Building applications for one of the many non-web platforms we support, including iOS, Android, XBox 360, XBox One, and Playstation 4 Building new features that millions of users will be seeing Helping build robust deployment tools to help us move forward rapidly Building great tools that lets us support our custom",
          'og:url': 'https://jobs.lever.co/twitch/a5f652d5-4f30-40ae-a860-14b869b5a445/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Internationalization',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Internationalization',
    'link': 'https://jobs.lever.co/twitch/061a5dd7-bd54-4a06-8f62-6b44f5a19bfc',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Our team builds the foundations that ensure overall product quality and \nfunctionality for all software development at Twitch, including bringing all our \nproducts to\xa0...',
    'htmlSnippet': 'Our team builds the foundations that ensure overall product quality and <br>\nfunctionality for all <b>software</b> development at Twitch, including bringing all our <br>\nproducts to&nbsp;...',
    'cacheId': 'ZePYSCpWJMcJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/061a5dd7-bd54-4a06-8f62-6b44f5a19bfc',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/061a5dd7-bd54-4a06-8f62-6b44f5a19bfc',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Internationalization',
          'twitter:description': 'Millions of visitors per month watch billions of minutes of video on Twitch around the world in many locales and languages on the web, mobile and gaming consoles. Our team builds the foundations that ensure overall product quality and functionality for all software development at Twitch, including bringing all our products to world readiness. Agile and effective collaboration with other teams is at the heart of our charter, our challenge and our passion. You are passionate about software development and delivering a great product to all users around the world. You, keep up-to-date with your craft but often dabble beyond; you are intellectually curious, inventive and eager to grow. You understand how code is written up and down the stack and how to build, integrate, test and deploy global-ready solutions with the latest tools and best practices. You are equally excited to build a minimum viable product quickly as you are cementing a proven feature in maintainable and tested code; you f',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Internationalization',
          'og:description': 'Millions of visitors per month watch billions of minutes of video on Twitch around the world in many locales and languages on the web, mobile and gaming consoles. Our team builds the foundations that ensure overall product quality and functionality for all software development at Twitch, including bringing all our products to world readiness. Agile and effective collaboration with other teams is at the heart of our charter, our challenge and our passion. You are passionate about software development and delivering a great product to all users around the world. You, keep up-to-date with your craft but often dabble beyond; you are intellectually curious, inventive and eager to grow. You understand how code is written up and down the stack and how to build, integrate, test and deploy global-ready solutions with the latest tools and best practices. You are equally excited to build a minimum viable product quickly as you are cementing a proven feature in maintainable and tested code; you f',
          'og:url': 'https://jobs.lever.co/twitch/061a5dd7-bd54-4a06-8f62-6b44f5a19bfc',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Infrastructure',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Infrastructure',
    'link': 'https://jobs.lever.co/twitch/786045c4-5534-4d97-b04a-74771f6856bb',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Twitch has over 100 million users, and the Video Infra team is responsible for \nbuilding infra services and tools to help scale and manage the infrastructure that\n\xa0...',
    'htmlSnippet': 'Twitch has over 100 million users, and the Video Infra team is responsible for <br>\nbuilding infra services and tools to help scale and manage the infrastructure that<br>\n&nbsp;...',
    'cacheId': '3UywsZWkSyUJ',
    'formattedUrl': 'https://jobs.lever.co/.../786045c4-5534-4d97-b04a-74771f6856bb',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../786045c4-5534-4d97-b04a-74771f6856bb',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Infrastructure',
          'twitter:description': 'Twitch has over 100 million users, and the Video Infra team is responsible for building infra services and tools to help scale and manage the infrastructure that powers Twitch▒s video. We▒re building a number of features to make Twitch the most compelling destination for video. We▒re looking for engineers that love delighting people with incredible products and user experiences. On the infra team, you▒ll work closely with our other engineering and product teams to craft engaging systems collect feedback, and iterate quickly. We value expertise in distributed systems, microservices and Devops on AWS. We are working on building an even more robust video system to scale twitch to the next level .',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Infrastructure',
          'og:description': 'Twitch has over 100 million users, and the Video Infra team is responsible for building infra services and tools to help scale and manage the infrastructure that powers Twitch▒s video. We▒re building a number of features to make Twitch the most compelling destination for video. We▒re looking for engineers that love delighting people with incredible products and user experiences. On the infra team, you▒ll work closely with our other engineering and product teams to craft engaging systems collect feedback, and iterate quickly. We value expertise in distributed systems, microservices and Devops on AWS. We are working on building an even more robust video system to scale twitch to the next level .',
          'og:url': 'https://jobs.lever.co/twitch/786045c4-5534-4d97-b04a-74771f6856bb',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Video CDN',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Video CDN',
    'link': 'https://jobs.lever.co/twitch/2fae3239-fe4d-4582-bfdf-7d43727853d3',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Twitch is building the future of interactive entertainment, and our video CDN is at \nthe core of that vision. Ensuring smooth, low-latency video across the world\xa0...',
    'htmlSnippet': 'Twitch is building the future of interactive entertainment, and our video CDN is at <br>\nthe core of that vision. Ensuring smooth, low-latency video across the world&nbsp;...',
    'cacheId': 'aee-uZY0VS0J',
    'formattedUrl': 'https://jobs.lever.co/twitch/2fae3239-fe4d-4582-bfdf-7d43727853d3',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/2fae3239-fe4d-4582-bfdf-7d43727853d3',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Video CDN',
          'twitter:description': 'Twitch is building the future of interactive entertainment, and our video CDN is at the core of that vision. Ensuring smooth, low-latency video across the world requires large-scale, fault-tolerant systems that can keep up with millions of simultaneous viewers and thousands of broadcasters. We are looking for engineers who are excited by the thought of working across the entire CDN stack, from service load-balancing, to performance optimization, to backbone traffic management. You will help architect, develop, test, deploy, operate, and maintain our video software software. As part of the team, we will work together to enable our broadcasters and viewers to create and interact in new, innovative ways.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Video CDN',
          'og:description': 'Twitch is building the future of interactive entertainment, and our video CDN is at the core of that vision. Ensuring smooth, low-latency video across the world requires large-scale, fault-tolerant systems that can keep up with millions of simultaneous viewers and thousands of broadcasters. We are looking for engineers who are excited by the thought of working across the entire CDN stack, from service load-balancing, to performance optimization, to backbone traffic management. You will help architect, develop, test, deploy, operate, and maintain our video software software. As part of the team, we will work together to enable our broadcasters and viewers to create and interact in new, innovative ways.',
          'og:url': 'https://jobs.lever.co/twitch/2fae3239-fe4d-4582-bfdf-7d43727853d3',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - VOD',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - VOD',
    'link': 'https://jobs.lever.co/twitch/58d343d0-4aa6-4516-84c2-c542f68b649a',
    'displayLink': 'jobs.lever.co',
    'snippet': "Twitch has over 100 million users, and the VOD team is responsible for building a \nnew experience that helps Twitch users watch recorded video. We're building\xa0...",
    'htmlSnippet': 'Twitch has over 100 million users, and the VOD team is responsible for building a <br>\nnew experience that helps Twitch users watch recorded video. We&#39;re building&nbsp;...',
    'cacheId': 'sEnt9yZhqrgJ',
    'formattedUrl': 'https://jobs.lever.co/.../58d343d0-4aa6-4516-84c2-c542f68b649a',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../58d343d0-4aa6-4516-84c2-c542f68b649a',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - VOD',
          'twitter:description': 'Twitch has over 100 million users, and the VOD team is responsible for building a new experience that helps Twitch users watch recorded video. We▒re building a number of features to make Twitch the most compelling destination for gaming recorded video this year. Recently, we launched VOD upload, Clips and our HTML5 Video Player, and we▒re just getting started. We▒re looking for product engineers that love delighting people with incredible products and user experiences. On the VOD team, you▒ll work closely with our other engineering and product teams to craft engaging consumer products, collect feedback, and iterate quickly. We value expertise in programming for the Web, microservices and Devops on AWS. If you are also comfortable with JS and crafting beautiful interfaces, even better! We are working on building unique VOD watching experiences that are uniquely Twitch. We aspire to change the way people consume and interact with video.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - VOD',
          'og:description': 'Twitch has over 100 million users, and the VOD team is responsible for building a new experience that helps Twitch users watch recorded video. We▒re building a number of features to make Twitch the most compelling destination for gaming recorded video this year. Recently, we launched VOD upload, Clips and our HTML5 Video Player, and we▒re just getting started. We▒re looking for product engineers that love delighting people with incredible products and user experiences. On the VOD team, you▒ll work closely with our other engineering and product teams to craft engaging consumer products, collect feedback, and iterate quickly. We value expertise in programming for the Web, microservices and Devops on AWS. If you are also comfortable with JS and crafting beautiful interfaces, even better! We are working on building unique VOD watching experiences that are uniquely Twitch. We aspire to change the way people consume and interact with video.',
          'og:url': 'https://jobs.lever.co/twitch/58d343d0-4aa6-4516-84c2-c542f68b649a',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Global Infrastructure',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Global Infrastructure',
    'link': 'https://jobs.lever.co/twitch/7204c413-9e6b-449f-9536-39aaa75c0c78',
    'displayLink': 'jobs.lever.co',
    'snippet': 'We are rapidly expanding the engineering team at Twitch to deal with \nchallenging scale problem of being the 4th biggest consumer of bandwidth and \none of the\xa0...',
    'htmlSnippet': 'We are rapidly expanding the <b>engineering</b> team at Twitch to deal with <br>\nchallenging scale problem of being the 4th biggest consumer of bandwidth and <br>\none of the&nbsp;...',
    'cacheId': 'ra9NS2Ro7YgJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/7204c413-9e6b-449f-9536-39aaa75c0c78',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/7204c413-9e6b-449f-9536-39aaa75c0c78',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Global Infrastructure',
          'twitter:description': 'We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. We are looking for the next set of engineering tech leaders to help grow Twitch to the next level. We need strong senior tech leaders that are comfortable working cross-functionally and not be afraid to touch many portions of our code-base to ensure that Twitch services can scale and be robust. We are moving to an SOA world and we need people comfortable with balancing product innovation with building out robust systems.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Global Infrastructure',
          'og:description': 'We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. We are looking for the next set of engineering tech leaders to help grow Twitch to the next level. We need strong senior tech leaders that are comfortable working cross-functionally and not be afraid to touch many portions of our code-base to ensure that Twitch services can scale and be robust. We are moving to an SOA world and we need people comfortable with balancing product innovation with building out robust systems.',
          'og:url': 'https://jobs.lever.co/twitch/7204c413-9e6b-449f-9536-39aaa75c0c78',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Network Software Engineer',
    'htmlTitle': 'Twitch - Senior Network <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/twitch/e8915dbe-817e-4aec-af61-01088eb4867f',
    'displayLink': 'jobs.lever.co',
    'snippet': 'By joining the Network Development team, as a Sr. Network Software Engineer, \nyou can help shape the future of network automation at Twitch.The Network\xa0...',
    'htmlSnippet': 'By joining the Network Development team, as a Sr. Network <b>Software Engineer</b>, <br>\nyou can help shape the future of network automation at Twitch.The Network&nbsp;...',
    'cacheId': 'Z9iJllvaCKwJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/e8915dbe-817e-4aec-af61-01088eb4867f',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/e8915dbe-817e-4aec-af61-01088eb4867f',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Network Software Engineer',
          'twitter:description': 'We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. By joining the Network Development team, as a Sr. Network Software Engineer, you can help shape the future of network automation at Twitch.The Network Development team is responsible for building the framework and tooling for network: automation, orchestration, visualization, and alerting. This framework enables other teams to: increase efficiency, leverage network telemetry in their algorithms, and allows the Twitch network to dynamically react to c',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Network Software Engineer',
          'og:description': 'We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. By joining the Network Development team, as a Sr. Network Software Engineer, you can help shape the future of network automation at Twitch.The Network Development team is responsible for building the framework and tooling for network: automation, orchestration, visualization, and alerting. This framework enables other teams to: increase efficiency, leverage network telemetry in their algorithms, and allows the Twitch network to dynamically react to c',
          'og:url': 'https://jobs.lever.co/twitch/e8915dbe-817e-4aec-af61-01088eb4867f',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Identity',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Identity',
    'link': 'https://jobs.lever.co/twitch/9ef94e2c-40db-4cff-aa5a-5b7c5e9bf230',
    'displayLink': 'jobs.lever.co',
    'snippet': "We are looking for a Full Stack software developer to join the Identity Team at \nTwitch. We're building OAuth solutions for our community to make a Twitch \nIdentity\xa0...",
    'htmlSnippet': 'We are looking for a Full Stack <b>software</b> developer to join the Identity Team at <br>\nTwitch. We&#39;re building OAuth solutions for our community to make a Twitch <br>\nIdentity&nbsp;...',
    'cacheId': 'hEfrPswIQrgJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/9ef94e2c-40db-4cff-aa5a-5b7c5e9bf230',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/9ef94e2c-40db-4cff-aa5a-5b7c5e9bf230',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Identity',
          'twitter:description': 'We are looking for a Full Stack software developer to join the Identity Team at Twitch. We▒re building OAuth solutions for our community to make a Twitch Identity the last identity you▒ll ever need. This is a technical role that builds heavily on internet standards for authorization and authentication on the Twitch site and our OAuth enabled partners. Our products are highly scalable and highly available world wide. As we level up our architecture and features, you▒ll have the opportunity to influence design decisions, tooling choices, and every last detail that makes us the best product we can be.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Identity',
          'og:description': 'We are looking for a Full Stack software developer to join the Identity Team at Twitch. We▒re building OAuth solutions for our community to make a Twitch Identity the last identity you▒ll ever need. This is a technical role that builds heavily on internet standards for authorization and authentication on the Twitch site and our OAuth enabled partners. Our products are highly scalable and highly available world wide. As we level up our architecture and features, you▒ll have the opportunity to influence design decisions, tooling choices, and every last detail that makes us the best product we can be.',
          'og:url': 'https://jobs.lever.co/twitch/9ef94e2c-40db-4cff-aa5a-5b7c5e9bf230',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Commerce',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Commerce',
    'link': 'https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf',
    'displayLink': 'jobs.lever.co',
    'snippet': "We're looking for engineers that love solving hard technical problems related to \ngaming on PCs and Twitch. This project will require innovation and the ability to\xa0...",
    'htmlSnippet': 'We&#39;re looking for <b>engineers</b> that love solving hard technical problems related to <br>\ngaming on PCs and Twitch. This project will require innovation and the ability to&nbsp;...',
    'cacheId': 'FWP11B-32uQJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Commerce',
          'twitter:description': 'Twitch is building the future of interactive entertainment, and our windows client engineering team is growing in order to execute on a brand new, secret project. We▒re looking for engineers that love solving hard technical problems related to gaming on PCs and Twitch. This project will require innovation and the ability to come up with technical solutions in new spaces. You will also need to work with and be able to think like a game developer. We▒re working with top developers to help bring new experiences to customers. We▒re using a variety of tools and languages, but much of our work will be in C++, so you▒ll have to be willing to roll up your sleeves and get your hands dirty. You▒ll have to write a lot of code, but should also be able to mentor engineers around you and do whatever needs to be done for the team and product initiative to succeed.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Commerce',
          'og:description': 'Twitch is building the future of interactive entertainment, and our windows client engineering team is growing in order to execute on a brand new, secret project. We▒re looking for engineers that love solving hard technical problems related to gaming on PCs and Twitch. This project will require innovation and the ability to come up with technical solutions in new spaces. You will also need to work with and be able to think like a game developer. We▒re working with top developers to help bring new experiences to customers. We▒re using a variety of tools and languages, but much of our work will be in C++, so you▒ll have to be willing to roll up your sleeves and get your hands dirty. You▒ll have to write a lot of code, but should also be able to mentor engineers around you and do whatever needs to be done for the team and product initiative to succeed.',
          'og:url': 'https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Payments',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Payments',
    'link': 'https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7',
    'displayLink': 'jobs.lever.co',
    'snippet': 'We\'re looking for a software engineer who gets why the story, "I bought a sub \nusing my favorite streamer\'s sub button so I can talk in sub-only chat" starts off\xa0...',
    'htmlSnippet': 'We&#39;re looking for a <b>software engineer</b> who gets why the story, &quot;I bought a sub <br>\nusing my favorite streamer&#39;s sub button so I can talk in sub-only chat&quot; starts off&nbsp;...',
    'cacheId': 'hvR82k33zE0J',
    'formattedUrl': 'https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Payments',
          'twitter:description': 'Twitch is building the future of interactive entertainment. The services we create for our users have deep, lasting effects on their lives. For many of our partnered broadcasters, streaming on Twitch is a career, and our payments system is central to making that possible. We\'re looking for a software engineer who gets why the story, "I bought a sub using my favorite streamer\'s sub button so I can talk in sub-only chat" starts off looking simple, but isn\'t. You like wrangling existing technologies together to solve business problems. Maybe you\'ve built an e-commerce site or two. On our team, you\'ll specialize in payments and related products like emotes and Turbo. Together, we\'re transforming the gaming world, $4.99 at a time.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Payments',
          'og:description': 'Twitch is building the future of interactive entertainment. The services we create for our users have deep, lasting effects on their lives. For many of our partnered broadcasters, streaming on Twitch is a career, and our payments system is central to making that possible. We\'re looking for a software engineer who gets why the story, "I bought a sub using my favorite streamer\'s sub button so I can talk in sub-only chat" starts off looking simple, but isn\'t. You like wrangling existing technologies together to solve business problems. Maybe you\'ve built an e-commerce site or two. On our team, you\'ll specialize in payments and related products like emotes and Turbo. Together, we\'re transforming the gaming world, $4.99 at a time.',
          'og:url': 'https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Software Engineer - Tools & Automation',
    'htmlTitle': 'Twitch - <b>Software Engineer</b> - Tools &amp; Automation',
    'link': 'https://jobs.lever.co/twitch/fb787bb2-c616-4d63-94ef-a96ac7f86b79',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Twitch is seeking an experienced Software Engineer for our Quality Engineering \nteam, who will be responsible for our test infrastructure and will be the quality\xa0...',
    'htmlSnippet': 'Twitch is seeking an experienced <b>Software Engineer</b> for our Quality Engineering <br>\nteam, who will be responsible for our test infrastructure and will be the quality&nbsp;...',
    'cacheId': '4h_N4PalkYgJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/fb787bb2-c616-4d63-94ef-a96ac7f86b79',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/fb787bb2-c616-4d63-94ef-a96ac7f86b79',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Software Engineer - Tools & Automation',
          'twitter:description': 'Twitch is seeking an experienced Software Engineer for our Quality Engineering team, who will be responsible for our test infrastructure and will be the quality champion of Twitch. As a Software Engineer,Tools , you will be responsible for establishing a consistent testing methodology for all products we release and promoting best practices across our many product development teams.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Software Engineer - Tools & Automation',
          'og:description': 'Twitch is seeking an experienced Software Engineer for our Quality Engineering team, who will be responsible for our test infrastructure and will be the quality champion of Twitch. As a Software Engineer,Tools , you will be responsible for establishing a consistent testing methodology for all products we release and promoting best practices across our many product development teams.',
          'og:url': 'https://jobs.lever.co/twitch/fb787bb2-c616-4d63-94ef-a96ac7f86b79',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Video Client',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Video Client',
    'link': 'https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc',
    'displayLink': 'jobs.lever.co',
    'snippet': "Twitch's Video Client Engineering team is looking for experienced video \nengineers to help build a cross-platform video playback solution that will support \nweb,\xa0...",
    'htmlSnippet': 'Twitch&#39;s Video Client <b>Engineering</b> team is looking for experienced video <br>\n<b>engineers</b> to help build a cross-platform video playback solution that will support <br>\nweb,&nbsp;...',
    'cacheId': 'KKk1mIgltLMJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Video Client',
          'twitter:description': 'Twitch is building the future of interactive entertainment and video is at the very core of that vision. Twitch▒s Video Client Engineering team is looking for experienced video engineers to help build a cross-platform video playback solution that will support web, mobile, and other platforms. As a core video engineer, you will be helping shape the future of the Twitch playback experience used by millions of users across various web browsers, mobile devices, gaming consoles, and more. If you are passionate about media, streaming, or obsessed about performance and want to participate in creating the best video playback system out there then this position is for you. You will work with an extremely talented and accomplished team in the video space and will be building a major component of the Video on Demand video playback pipeline that will scale to millions of users. You will gain an in-depth knowledge on a highly scalable, end to end video streaming platform.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Video Client',
          'og:description': 'Twitch is building the future of interactive entertainment and video is at the very core of that vision. Twitch▒s Video Client Engineering team is looking for experienced video engineers to help build a cross-platform video playback solution that will support web, mobile, and other platforms. As a core video engineer, you will be helping shape the future of the Twitch playback experience used by millions of users across various web browsers, mobile devices, gaming consoles, and more. If you are passionate about media, streaming, or obsessed about performance and want to participate in creating the best video playback system out there then this position is for you. You will work with an extremely talented and accomplished team in the video space and will be building a major component of the Video on Demand video playback pipeline that will scale to millions of users. You will gain an in-depth knowledge on a highly scalable, end to end video streaming platform.',
          'og:url': 'https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Bits',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Bits',
    'link': 'https://jobs.lever.co/twitch/ebad0f08-c9b4-4b52-bfa1-78edd6aa136b',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Twitch is building the future of interactive entertainment, and our web client \nengineering team is preparing to scale to execute on critical product initiatives \nlike\xa0...',
    'htmlSnippet': 'Twitch is building the future of interactive entertainment, and our web client <br>\n<b>engineering</b> team is preparing to scale to execute on critical product initiatives <br>\nlike&nbsp;...',
    'cacheId': 'tkktVlD-AkcJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/ebad0f08-c9b4-4b52-bfa1-78edd6aa136b',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/ebad0f08-c9b4-4b52-bfa1-78edd6aa136b',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Bits',
          'twitter:description': 'Twitch is building the future of interactive entertainment, and our web client engineering team is preparing to scale to execute on critical product initiatives like Cheering with Bits, Subscriptions, Affiliates, Twitch Prime, and many great social interaction features. Our Seattle office is focused on exciting new e-commerce initiatives in 2017! We▒re looking for engineers that love delighting people with incredible products and user experiences. On the Commerce team, you▒ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in programming for the Web (including an understanding of modern JS tooling and cross-browser compatibility issues) and sensibilities for design and UX. The web client is written with Ember.js, builds using Ember CLI, uses ES6 features via Babel, and manifests backend systems like chat and video as user-facing products. We also are building some new featu',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Bits',
          'og:description': 'Twitch is building the future of interactive entertainment, and our web client engineering team is preparing to scale to execute on critical product initiatives like Cheering with Bits, Subscriptions, Affiliates, Twitch Prime, and many great social interaction features. Our Seattle office is focused on exciting new e-commerce initiatives in 2017! We▒re looking for engineers that love delighting people with incredible products and user experiences. On the Commerce team, you▒ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in programming for the Web (including an understanding of modern JS tooling and cross-browser compatibility issues) and sensibilities for design and UX. The web client is written with Ember.js, builds using Ember CLI, uses ES6 features via Babel, and manifests backend systems like chat and video as user-facing products. We also are building some new featu',
          'og:url': 'https://jobs.lever.co/twitch/ebad0f08-c9b4-4b52-bfa1-78edd6aa136b',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Twitch Crates',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Twitch Crates',
    'link': 'https://jobs.lever.co/twitch/4a17fcc9-b8da-4716-9e34-78663265b4f9',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Twitch is building the future of interactive entertainment and our Commerce \nengineering team builds key services which allow thousands of creative\xa0...',
    'htmlSnippet': 'Twitch is building the future of interactive entertainment and our Commerce <br>\n<b>engineering</b> team builds key services which allow thousands of creative&nbsp;...',
    'cacheId': 'mKIjAzgFIaAJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/4a17fcc9-b8da-4716-9e34-78663265b4f9',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/4a17fcc9-b8da-4716-9e34-78663265b4f9',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Twitch Crates',
          'twitter:description': 'Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing ▒gig economy▒ which allows these creators to earn part or all of their income by producing high quality content on Twitch. Twitch Crates was introduced earlier this year as part of our Game Commerce strategy and we are looking for engineers who want to take it to the next level and scale it across other dimensions on Twitch. Crates provides additional value to viewers engaging on Twitch, as well as more interesting and unique ways for Broadcasters, Game Developers and other influencers to reach their audience and monetize their content. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible Web application software. You are a full stack developer who is comfortable with Javascript',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Twitch Crates',
          'og:description': 'Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing ▒gig economy▒ which allows these creators to earn part or all of their income by producing high quality content on Twitch. Twitch Crates was introduced earlier this year as part of our Game Commerce strategy and we are looking for engineers who want to take it to the next level and scale it across other dimensions on Twitch. Crates provides additional value to viewers engaging on Twitch, as well as more interesting and unique ways for Broadcasters, Game Developers and other influencers to reach their audience and monetize their content. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible Web application software. You are a full stack developer who is comfortable with Javascript',
          'og:url': 'https://jobs.lever.co/twitch/4a17fcc9-b8da-4716-9e34-78663265b4f9',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Software Engineer, Mac',
    'htmlTitle': 'Twitch - <b>Software Engineer</b>, Mac',
    'link': 'https://jobs.lever.co/twitch/4bf8046f-aab3-4151-a6e0-d21ec251f38e',
    'displayLink': 'jobs.lever.co',
    'snippet': "Mac is an important piece of our desktop application strategy. As a software \nengineer, you'll be working on the Twitch Desktop Application for the Mac \nplatform.",
    'htmlSnippet': 'Mac is an important piece of our desktop application strategy. As a <b>software</b> <br>\n<b>engineer</b>, you&#39;ll be working on the Twitch Desktop Application for the Mac <br>\nplatform.',
    'cacheId': 'r9cbDeiOJ5wJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/4bf8046f-aab3-4151-a6e0-d21ec251f38e',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/4bf8046f-aab3-4151-a6e0-d21ec251f38e',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Software Engineer, Mac',
          'twitter:description': 'We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Mac is an important piece of our desktop application strategy. As a software engineer, you▒ll be working on the Twitch Desktop Application for the Mac platform.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Software Engineer, Mac',
          'og:description': 'We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Mac is an important piece of our desktop application strategy. As a software engineer, you▒ll be working on the Twitch Desktop Application for the Mac platform.',
          'og:url': 'https://jobs.lever.co/twitch/4bf8046f-aab3-4151-a6e0-d21ec251f38e',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '512',
          'og:image:width': '1024'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Software Engineer - Tools',
    'htmlTitle': 'Twitch - <b>Software Engineer</b> - Tools',
    'link': 'https://jobs.lever.co/twitch/e689e043-c062-4421-9dde-e973c509b818/',
    'displayLink': 'jobs.lever.co',
    'snippet': '7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\xa0...',
    'htmlSnippet': '7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...',
    'cacheId': '1BtXg298xp4J',
    'formattedUrl': 'https://jobs.lever.co/twitch/e689e043-c062-4421-9dde.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/e689e043-c062-4421-9dde.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Software Engineer - Tools',
          'twitter:description': "Twitch is building the future of interactive entertainment, and video is at the very core of that vision. Our engineering teams are solving problems to help deliver the best content available. If you are passionate about building tools to automate 'all the things' and you're excited to support other talented developers all around you...Twitch is the place to be.",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Software Engineer - Tools',
          'og:description': "Twitch is building the future of interactive entertainment, and video is at the very core of that vision. Our engineering teams are solving problems to help deliver the best content available. If you are passionate about building tools to automate 'all the things' and you're excited to support other talented developers all around you...Twitch is the place to be.",
          'og:url': 'https://jobs.lever.co/twitch/e689e043-c062-4421-9dde-e973c509b818/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Subscriptions',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Subscriptions',
    'link': 'https://jobs.lever.co/twitch/4d961614-d40d-4c70-b6cb-246a540901d4',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Twitch is building the future of interactive entertainment and our Commerce \nengineering team builds key services which allow thousands of creative\xa0...',
    'htmlSnippet': 'Twitch is building the future of interactive entertainment and our Commerce <br>\n<b>engineering</b> team builds key services which allow thousands of creative&nbsp;...',
    'cacheId': 'Rjw75Dg2q2YJ',
    'formattedUrl': 'https://jobs.lever.co/.../4d961614-d40d-4c70-b6cb-246a540901d4',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../4d961614-d40d-4c70-b6cb-246a540901d4',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Subscriptions',
          'twitter:description': 'Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing ▒gig economy▒ which allows these creators to earn part or all of their income by producing high quality content on Twitch. Our San Francisco office is focused on exciting new e-commerce initiatives in 2017! We▒re looking for engineers that love delighting people with incredible products and user experiences such as our Subscriptions for Affiliates feature released on June 28th, 2017 which allows thousands of streamers to receive subscribers to their channels. On the Commerce team, you▒ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible W',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Subscriptions',
          'og:description': 'Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing ▒gig economy▒ which allows these creators to earn part or all of their income by producing high quality content on Twitch. Our San Francisco office is focused on exciting new e-commerce initiatives in 2017! We▒re looking for engineers that love delighting people with incredible products and user experiences such as our Subscriptions for Affiliates feature released on June 28th, 2017 which allows thousands of streamers to receive subscribers to their channels. On the Commerce team, you▒ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible W',
          'og:url': 'https://jobs.lever.co/twitch/4d961614-d40d-4c70-b6cb-246a540901d4',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Discovery',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Discovery',
    'link': 'https://jobs.lever.co/twitch/4ca38bac-3695-4504-ac6d-cea7cdbd0a85',
    'displayLink': 'jobs.lever.co',
    'snippet': 'We are looking for a software engineer to contribute to key product roadmap \nitems, recommendations, search and machine learning infrastructure, internal\xa0...',
    'htmlSnippet': 'We are looking for a <b>software engineer</b> to contribute to key product roadmap <br>\nitems, recommendations, search and machine learning infrastructure, internal&nbsp;...',
    'cacheId': 'v8uGvJqnQFkJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/4ca38bac-3695-4504-ac6d-cea7cdbd0a85',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/4ca38bac-3695-4504-ac6d-cea7cdbd0a85',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Discovery',
          'twitter:description': "Twitch has over 100 million users, and the Metadata, Recommendations, and Search team is responsible for building products that improve the discovery experience for both viewers and broadcasters. We are looking for a software engineer to contribute to key product roadmap items, recommendations, search and machine learning infrastructure, internal machine learning tools. You will have the opportunity to develop and work on high-profile elements of the Twitch architecture and help create large scale distributed systems. You will be working with other highly motivated team members on building next generation recommendation and search systems at scale, using cutting edge ML/AI algorithms. You will develop services to run on Amazon's cloud computing infrastructure (AWS) and have opportunities to interact with teams inside and outside the organization as well as work on a variety of challenging problems.",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Discovery',
          'og:description': "Twitch has over 100 million users, and the Metadata, Recommendations, and Search team is responsible for building products that improve the discovery experience for both viewers and broadcasters. We are looking for a software engineer to contribute to key product roadmap items, recommendations, search and machine learning infrastructure, internal machine learning tools. You will have the opportunity to develop and work on high-profile elements of the Twitch architecture and help create large scale distributed systems. You will be working with other highly motivated team members on building next generation recommendation and search systems at scale, using cutting edge ML/AI algorithms. You will develop services to run on Amazon's cloud computing infrastructure (AWS) and have opportunities to interact with teams inside and outside the organization as well as work on a variety of challenging problems.",
          'og:url': 'https://jobs.lever.co/twitch/4ca38bac-3695-4504-ac6d-cea7cdbd0a85',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Store',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Store',
    'link': 'https://jobs.lever.co/twitch/6b7d7126-c77f-49c8-8ded-f19dce3c13aa',
    'displayLink': 'jobs.lever.co',
    'snippet': 'We are looking for mid to senior Software Development Engineer who want to \ntake our Commerce experiences to the next level and scale it across other\xa0...',
    'htmlSnippet': 'We are looking for mid to senior <b>Software</b> Development <b>Engineer</b> who want to <br>\ntake our Commerce experiences to the next level and scale it across other&nbsp;...',
    'cacheId': '16SDrFIXoHAJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/6b7d7126-c77f-49c8-8ded-f19dce3c13aa',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/6b7d7126-c77f-49c8-8ded-f19dce3c13aa',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Store',
          'twitter:description': 'Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing ▒gig economy▒ which allows these creators to earn part or all of their income by producing high quality content on Twitch. As an early joiner of the team you will, provide creative input into brand direction and drive high visibility projects across a number of commerce teams. We are looking for mid to senior Software Development Engineer who want to take our Commerce experiences to the next level and scale it across other dimensions on Twitch. The ideal candidate has strong organizational skills, web expertise, and acute attention to detail. They will have developed a deep technical understanding of the strengths and weaknesses of delivery platforms, and are able to identify opportunities and to work creatively within the cons',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Store',
          'og:description': 'Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing ▒gig economy▒ which allows these creators to earn part or all of their income by producing high quality content on Twitch. As an early joiner of the team you will, provide creative input into brand direction and drive high visibility projects across a number of commerce teams. We are looking for mid to senior Software Development Engineer who want to take our Commerce experiences to the next level and scale it across other dimensions on Twitch. The ideal candidate has strong organizational skills, web expertise, and acute attention to detail. They will have developed a deep technical understanding of the strengths and weaknesses of delivery platforms, and are able to identify opportunities and to work creatively within the cons',
          'og:url': 'https://jobs.lever.co/twitch/6b7d7126-c77f-49c8-8ded-f19dce3c13aa',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Video Player',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Video Player',
    'link': 'https://jobs.lever.co/twitch/65b04ed0-7b51-4be5-b81f-17a2d794a381',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Twitch has over 100 million users, and the Playback Technologies team is \nresponsible for helping them connect with content they love on both live and \nrecorded\xa0...',
    'htmlSnippet': 'Twitch has over 100 million users, and the Playback Technologies team is <br>\nresponsible for helping them connect with content they love on both live and <br>\nrecorded&nbsp;...',
    'cacheId': 'yLUp9kTcwxwJ',
    'formattedUrl': 'https://jobs.lever.co/.../65b04ed0-7b51-4be5-b81f-17a2d794a381',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../65b04ed0-7b51-4be5-b81f-17a2d794a381',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Video Player',
          'twitter:description': 'Twitch has over 100 million users, and the Playback Technologies team is responsible for helping them connect with content they love on both live and recorded video. We▒re building a number of features to make Twitch the most compelling destination for gaming video this year. Recently, we launched Clips and our HTML5 Video Player, and we▒re just getting started. We▒re looking for engineers that love delighting people with incredible products and user experiences. You▒ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in programming for the Web (including an understanding of modern JS tooling and cross-browser compatibility issues) and sensibilities for design and UX.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Video Player',
          'og:description': 'Twitch has over 100 million users, and the Playback Technologies team is responsible for helping them connect with content they love on both live and recorded video. We▒re building a number of features to make Twitch the most compelling destination for gaming video this year. Recently, we launched Clips and our HTML5 Video Player, and we▒re just getting started. We▒re looking for engineers that love delighting people with incredible products and user experiences. You▒ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in programming for the Web (including an understanding of modern JS tooling and cross-browser compatibility issues) and sensibilities for design and UX.',
          'og:url': 'https://jobs.lever.co/twitch/65b04ed0-7b51-4be5-b81f-17a2d794a381',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Frontend Software Engineer - Store',
    'htmlTitle': 'Twitch - Frontend <b>Software Engineer</b> - Store',
    'link': 'https://jobs.lever.co/twitch/0ee71b6e-bb91-47b9-8d28-4d3df21c09a9',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Twitch is launching a merchandise line featuring our own community inspired \nlogos and designs and are in need of a creative mind to help bring the right\xa0...',
    'htmlSnippet': 'Twitch is launching a merchandise line featuring our own community inspired <br>\nlogos and designs and are in need of a creative mind to help bring the right&nbsp;...',
    'cacheId': '3fE41pyF6nAJ',
    'formattedUrl': 'https://jobs.lever.co/.../0ee71b6e-bb91-47b9-8d28-4d3df21c09a9',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../0ee71b6e-bb91-47b9-8d28-4d3df21c09a9',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Frontend Software Engineer - Store',
          'twitter:description': 'Twitch is launching a merchandise line featuring our own community inspired logos and designs and are in need of a creative mind to help bring the right customer experience onto Twitch. As an early joiner of the team you will gain the opportunity to influence an international launch, provide creative input into brand direction and drive high visibility projects across a number of commerce teams. We are looking for an experienced Front End Developer who has successfully demonstrated taking business goals and turning them into inspiring designs. The ideal candidate has strong organizational skills, web expertise, and acute attention to detail. They will have developed a deep technical understanding of the strengths and weaknesses of delivery platforms, and are able to identify opportunities and to work creatively within the constraints they impose. In this role, you will be expected to work closely with a team of designers, researchers, developers, and project managers. Using your ski',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Frontend Software Engineer - Store',
          'og:description': 'Twitch is launching a merchandise line featuring our own community inspired logos and designs and are in need of a creative mind to help bring the right customer experience onto Twitch. As an early joiner of the team you will gain the opportunity to influence an international launch, provide creative input into brand direction and drive high visibility projects across a number of commerce teams. We are looking for an experienced Front End Developer who has successfully demonstrated taking business goals and turning them into inspiring designs. The ideal candidate has strong organizational skills, web expertise, and acute attention to detail. They will have developed a deep technical understanding of the strengths and weaknesses of delivery platforms, and are able to identify opportunities and to work creatively within the constraints they impose. In this role, you will be expected to work closely with a team of designers, researchers, developers, and project managers. Using your ski',
          'og:url': 'https://jobs.lever.co/twitch/0ee71b6e-bb91-47b9-8d28-4d3df21c09a9',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Social Products',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Social Products',
    'link': 'https://jobs.lever.co/twitch/cc6d80b0-93a4-4e59-bb25-3377e4a90413',
    'displayLink': 'jobs.lever.co',
    'snippet': 'The Community Success organization is responsible for building the products \nthat allow Twitch users to discover, communicate and keep in touch with over\xa0...',
    'htmlSnippet': 'The Community Success organization is responsible for building the products <br>\nthat allow Twitch users to discover, communicate and keep in touch with over&nbsp;...',
    'cacheId': 'vRmmPpP1Hd4J',
    'formattedUrl': 'https://jobs.lever.co/.../cc6d80b0-93a4-4e59-bb25-3377e4a90413',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../cc6d80b0-93a4-4e59-bb25-3377e4a90413',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Social Products',
          'twitter:description': "The Community Success organization is responsible for building the products that allow Twitch users to discover, communicate and keep in touch with over 100M Twitch users and broadcasters. We're focused on building features that keep users coming back to Twitch such as chat, whispers, feeds, and notifications, as well as game directories, communities, and other features to help Twitch broadcasters get discovered.We're looking for engineers that want to help the Twitch community. In this organization, you'll work alongside product, data science, and design to craft scalable, fault-tolerant backend systems and seamless front-end user experiences. If you want to help build the future of gaming-related discovery and interaction, you should join us!",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Social Products',
          'og:description': "The Community Success organization is responsible for building the products that allow Twitch users to discover, communicate and keep in touch with over 100M Twitch users and broadcasters. We're focused on building features that keep users coming back to Twitch such as chat, whispers, feeds, and notifications, as well as game directories, communities, and other features to help Twitch broadcasters get discovered.We're looking for engineers that want to help the Twitch community. In this organization, you'll work alongside product, data science, and design to craft scalable, fault-tolerant backend systems and seamless front-end user experiences. If you want to help build the future of gaming-related discovery and interaction, you should join us!",
          'og:url': 'https://jobs.lever.co/twitch/cc6d80b0-93a4-4e59-bb25-3377e4a90413',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Video Client',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Video Client',
    'link': 'https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc/',
    'displayLink': 'jobs.lever.co',
    'snippet': '7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\xa0...',
    'htmlSnippet': '7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...',
    'cacheId': 'WiD3DuFXIAQJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Video Client',
          'twitter:description': 'Twitch is building the future of interactive entertainment and video is at the very core of that vision. Twitch▒s Video Client Engineering team is looking for experienced video engineers to help build a cross-platform video playback solution that will support web, mobile, and other platforms. As a core video engineer, you will be helping shape the future of the Twitch playback experience used by millions of users across various web browsers, mobile devices, gaming consoles, and more. If you are passionate about media, streaming, or obsessed about performance and want to participate in creating the best video playback system out there then this position is for you. You will work with an extremely talented and accomplished team in the video space and will be building a major component of the Video on Demand video playback pipeline that will scale to millions of users. You will gain an in-depth knowledge on a highly scalable, end to end video streaming platform.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Video Client',
          'og:description': 'Twitch is building the future of interactive entertainment and video is at the very core of that vision. Twitch▒s Video Client Engineering team is looking for experienced video engineers to help build a cross-platform video playback solution that will support web, mobile, and other platforms. As a core video engineer, you will be helping shape the future of the Twitch playback experience used by millions of users across various web browsers, mobile devices, gaming consoles, and more. If you are passionate about media, streaming, or obsessed about performance and want to participate in creating the best video playback system out there then this position is for you. You will work with an extremely talented and accomplished team in the video space and will be building a major component of the Video on Demand video playback pipeline that will scale to millions of users. You will gain an in-depth knowledge on a highly scalable, end to end video streaming platform.',
          'og:url': 'https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Video Player',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Video Player',
    'link': 'https://jobs.lever.co/twitch/65b04ed0-7b51-4be5-b81f-17a2d794a381/',
    'displayLink': 'jobs.lever.co',
    'snippet': '7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\xa0...',
    'htmlSnippet': '7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...',
    'cacheId': 'Z_offpSdhUkJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/65b04ed0-7b51-4be5-b81f.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/65b04ed0-7b51-4be5-b81f.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Video Player',
          'twitter:description': 'Twitch has over 100 million users, and the Playback Technologies team is responsible for helping them connect with content they love on both live and recorded video. We▒re building a number of features to make Twitch the most compelling destination for gaming video this year. Recently, we launched Clips and our HTML5 Video Player, and we▒re just getting started. We▒re looking for engineers that love delighting people with incredible products and user experiences. You▒ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in programming for the Web (including an understanding of modern JS tooling and cross-browser compatibility issues) and sensibilities for design and UX.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Video Player',
          'og:description': 'Twitch has over 100 million users, and the Playback Technologies team is responsible for helping them connect with content they love on both live and recorded video. We▒re building a number of features to make Twitch the most compelling destination for gaming video this year. Recently, we launched Clips and our HTML5 Video Player, and we▒re just getting started. We▒re looking for engineers that love delighting people with incredible products and user experiences. You▒ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in programming for the Web (including an understanding of modern JS tooling and cross-browser compatibility issues) and sensibilities for design and UX.',
          'og:url': 'https://jobs.lever.co/twitch/65b04ed0-7b51-4be5-b81f-17a2d794a381/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Live Video Infrastructure',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Live Video Infrastructure',
    'link': 'https://jobs.lever.co/twitch/786045c4-5534-4d97-b04a-74771f6856bb/',
    'displayLink': 'jobs.lever.co',
    'snippet': '7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\xa0...',
    'htmlSnippet': '7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...',
    'cacheId': 'Rjl4__1ls54J',
    'formattedUrl': 'https://jobs.lever.co/twitch/786045c4-5534-4d97-b04a.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/786045c4-5534-4d97-b04a.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Live Video Infrastructure',
          'twitter:description': "Are you interested in the future of interactive video? Want to redefine what concurrent viewing experiences are like? Twitch is building the future of real time interactive entertainment and video is at the very core of that vision! The team is focused on designing large scale systems to power the Twitch video services which handle incoming video from thousands of broadcasters and viewed by massive audiences. You will help support them at a new level! You will develop services to run on Amazon's cloud computing infrastructure (AWS) and have opportunities to interact with teams inside and outside the organization as well as work on a variety of challenging problems.",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Live Video Infrastructure',
          'og:description': "Are you interested in the future of interactive video? Want to redefine what concurrent viewing experiences are like? Twitch is building the future of real time interactive entertainment and video is at the very core of that vision! The team is focused on designing large scale systems to power the Twitch video services which handle incoming video from thousands of broadcasters and viewed by massive audiences. You will help support them at a new level! You will develop services to run on Amazon's cloud computing infrastructure (AWS) and have opportunities to interact with teams inside and outside the organization as well as work on a variety of challenging problems.",
          'og:url': 'https://jobs.lever.co/twitch/786045c4-5534-4d97-b04a-74771f6856bb/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer in Test - Core Payments',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> in Test - Core Payments',
    'link': 'https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31/',
    'displayLink': 'jobs.lever.co',
    'snippet': '7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\xa0...',
    'htmlSnippet': '7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...',
    'cacheId': 'lI7M7zcLmYwJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer in Test - Core Payments',
          'twitter:description': 'Core Payments team owns product/systems that affect millions of users and broadcasters. Our platforms enable automated onboarding as well as payments processing so its role is essential for the company. The teams are directly responsible in ensuring high quality world class payments experiences for our users. As a Senior Software Engineer in Test for Core Payments team, you will be working closely with development and various other cross-functional teams to ensure the highest quality for our projects.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer in Test - Core Payments',
          'og:description': 'Core Payments team owns product/systems that affect millions of users and broadcasters. Our platforms enable automated onboarding as well as payments processing so its role is essential for the company. The teams are directly responsible in ensuring high quality world class payments experiences for our users. As a Senior Software Engineer in Test for Core Payments team, you will be working closely with development and various other cross-functional teams to ensure the highest quality for our projects.',
          'og:url': 'https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Backend Software Engineer- Developer Success',
    'htmlTitle': 'Twitch - Backend <b>Software Engineer</b>- Developer Success',
    'link': 'https://jobs.lever.co/twitch/1fe36347-5bc9-4620-9273-9f93554717e4?lever-source=stackshare.io/match',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Twitch seeks a talented back end software engineer to help us create features for \nthousands of game developers building the next generation of games.',
    'htmlSnippet': 'Twitch seeks a talented back end <b>software engineer</b> to help us create features for <br>\nthousands of game developers building the next generation of games.',
    'cacheId': '1FjDukRruCAJ',
    'formattedUrl': 'https://jobs.lever.co/.../1fe36347-5bc9-4620-9273-9f93554717e4?...',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../1fe36347-5bc9-4620-9273-9f93554717e4?...',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Backend Software Engineer- Developer Success',
          'twitter:description': 'Twitch seeks a talented back end software engineer to help us create features for thousands of game developers building the next generation of games. Your first project will be experienced by millions.  You will help set the foundation and execute on the construction of back end services and web apps. You have an instinct for code quality and a passion for craftsmanship. You thrive on rapid learning, the opportunity for innovation, and collaborating with top flight team members.  The Developer Success team helps creators, from the world▒s top game companies to amazing indie teams, present their products to viewers who may like them, engage with their existing users, and find innovative new ways to generate revenue. With your help we will delight developers and shape the landscape of the gaming industry.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Backend Software Engineer- Developer Success',
          'og:description': 'Twitch seeks a talented back end software engineer to help us create features for thousands of game developers building the next generation of games. Your first project will be experienced by millions.  You will help set the foundation and execute on the construction of back end services and web apps. You have an instinct for code quality and a passion for craftsmanship. You thrive on rapid learning, the opportunity for innovation, and collaborating with top flight team members.  The Developer Success team helps creators, from the world▒s top game companies to amazing indie teams, present their products to viewers who may like them, engage with their existing users, and find innovative new ways to generate revenue. With your help we will delight developers and shape the landscape of the gaming industry.',
          'og:url': 'https://jobs.lever.co/twitch/1fe36347-5bc9-4620-9273-9f93554717e4',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '512',
          'og:image:width': '1024'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Payments',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Payments',
    'link': 'https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7/',
    'displayLink': 'jobs.lever.co',
    'snippet': '7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\xa0...',
    'htmlSnippet': '7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...',
    'cacheId': 'h5OmuIfIA3EJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf.../apply?...',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf.../apply?...',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Payments',
          'twitter:description': 'Twitch is building the future of interactive entertainment. The services we create for our users have deep, lasting effects on their lives. For many of our partnered broadcasters, streaming on Twitch is a career, and our payments system is central to making that possible. We\'re looking for a software engineer who gets why the story, "I bought a sub using my favorite streamer\'s sub button so I can talk in sub-only chat" starts off looking simple, but isn\'t. You like wrangling existing technologies together to solve business problems. Maybe you\'ve built an e-commerce site or two. On our team, you\'ll specialize in payments and related products like emotes and Turbo. Together, we\'re transforming the gaming world, $4.99 at a time.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Payments',
          'og:description': 'Twitch is building the future of interactive entertainment. The services we create for our users have deep, lasting effects on their lives. For many of our partnered broadcasters, streaming on Twitch is a career, and our payments system is central to making that possible. We\'re looking for a software engineer who gets why the story, "I bought a sub using my favorite streamer\'s sub button so I can talk in sub-only chat" starts off looking simple, but isn\'t. You like wrangling existing technologies together to solve business problems. Maybe you\'ve built an e-commerce site or two. On our team, you\'ll specialize in payments and related products like emotes and Turbo. Together, we\'re transforming the gaming world, $4.99 at a time.',
          'og:url': 'https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Software Engineer - Console Apps',
    'htmlTitle': 'Twitch - <b>Software Engineer</b> - Console Apps',
    'link': 'https://jobs.lever.co/twitch/a0a99d06-bd2a-4ea1-8df1-f2d3705c7c6b',
    'displayLink': 'jobs.lever.co',
    'snippet': "The Client Applications team is responsible for developing Twitch's client \napplications on a wide variety of target platforms, including gaming consoles, \nmobile\xa0...",
    'htmlSnippet': 'The Client Applications team is responsible for developing Twitch&#39;s client <br>\napplications on a wide variety of target platforms, including gaming consoles, <br>\nmobile&nbsp;...',
    'cacheId': '6XSKNYvf33cJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/a0a99d06-bd2a-4ea1-8df1-f2d3705c7c6b',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/a0a99d06-bd2a-4ea1-8df1-f2d3705c7c6b',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Software Engineer - Console Apps',
          'twitter:description': 'The Client Applications team is responsible for developing Twitch▒s client applications on a wide variety of target platforms, including gaming consoles, mobile devices, smart TVs, set-top boxes, and other current and future video platforms (e.g. VR). As an Application Engineer, you will be using a variety of frameworks and languages to bring a great Twitch experience to each platform.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Software Engineer - Console Apps',
          'og:description': 'The Client Applications team is responsible for developing Twitch▒s client applications on a wide variety of target platforms, including gaming consoles, mobile devices, smart TVs, set-top boxes, and other current and future video platforms (e.g. VR). As an Application Engineer, you will be using a variety of frameworks and languages to bring a great Twitch experience to each platform.',
          'og:url': 'https://jobs.lever.co/twitch/a0a99d06-bd2a-4ea1-8df1-f2d3705c7c6b',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Software Engineer - Data',
    'htmlTitle': 'Twitch - <b>Software Engineer</b> - Data',
    'link': 'https://jobs.lever.co/twitch/889401a7-d917-4947-97d7-8a2d2e2fd430/',
    'displayLink': 'jobs.lever.co',
    'snippet': '7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\xa0...',
    'htmlSnippet': '7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...',
    'cacheId': 'FTyrTOuPX8EJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/889401a7-d917-4947-97d7.../apply?...',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/889401a7-d917-4947-97d7.../apply?...',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Software Engineer - Data',
          'twitter:description': 'Twitch is building the future of interactive entertainment, and data is critical to every decision we make. The Science Engineering team is looking for a developer to help us meet all the diverse data needs within Twitch and to scale with those needs. Our team develops and operates the real-time behavioral data pipeline, which collects, processes, and distributes data to other teams. We provide data to systems and decision making throughout the company, and we have a constantly growing list of data consumers. The core pipeline is open source -- check out our code at github.com/twitchscience',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Software Engineer - Data',
          'og:description': 'Twitch is building the future of interactive entertainment, and data is critical to every decision we make. The Science Engineering team is looking for a developer to help us meet all the diverse data needs within Twitch and to scale with those needs. Our team develops and operates the real-time behavioral data pipeline, which collects, processes, and distributes data to other teams. We provide data to systems and decision making throughout the company, and we have a constantly growing list of data consumers. The core pipeline is open source -- check out our code at github.com/twitchscience',
          'og:url': 'https://jobs.lever.co/twitch/889401a7-d917-4947-97d7-8a2d2e2fd430/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Store',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Store',
    'link': 'https://jobs.lever.co/twitch/6b7d7126-c77f-49c8-8ded-f19dce3c13aa/',
    'displayLink': 'jobs.lever.co',
    'snippet': 'U.S. Equal Employment Opportunity information (Completion is voluntary and will \nnot subject you to adverse treatment). Twitch provides equal employment and\xa0...',
    'htmlSnippet': 'U.S. Equal Employment Opportunity information (Completion is voluntary and will <br>\nnot subject you to adverse treatment). Twitch provides equal employment and&nbsp;...',
    'cacheId': 'VsZbB7Ar05cJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/6b7d7126-c77f-49c8-8ded.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/6b7d7126-c77f-49c8-8ded.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Store',
          'twitter:description': 'Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing ▒gig economy▒ which allows these creators to earn part or all of their income by producing high quality content on Twitch. As an early joiner of the team you will, provide creative input into brand direction and drive high visibility projects across a number of commerce teams. We are looking for mid to senior Software Development Engineer who want to take our Commerce experiences to the next level and scale it across other dimensions on Twitch. The ideal candidate has strong organizational skills, web expertise, and acute attention to detail. They will have developed a deep technical understanding of the strengths and weaknesses of delivery platforms, and are able to identify opportunities and to work creatively within the cons',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Store',
          'og:description': 'Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing ▒gig economy▒ which allows these creators to earn part or all of their income by producing high quality content on Twitch. As an early joiner of the team you will, provide creative input into brand direction and drive high visibility projects across a number of commerce teams. We are looking for mid to senior Software Development Engineer who want to take our Commerce experiences to the next level and scale it across other dimensions on Twitch. The ideal candidate has strong organizational skills, web expertise, and acute attention to detail. They will have developed a deep technical understanding of the strengths and weaknesses of delivery platforms, and are able to identify opportunities and to work creatively within the cons',
          'og:url': 'https://jobs.lever.co/twitch/6b7d7126-c77f-49c8-8ded-f19dce3c13aa/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Software Engineer - Twitch Crates',
    'htmlTitle': 'Twitch - Senior <b>Software Engineer</b> - Twitch Crates',
    'link': 'https://jobs.lever.co/twitch/4a17fcc9-b8da-4716-9e34-78663265b4f9/',
    'displayLink': 'jobs.lever.co',
    'snippet': '7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\xa0...',
    'htmlSnippet': '7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...',
    'cacheId': 'okYRq118HlMJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/4a17fcc9-b8da-4716-9e34.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/4a17fcc9-b8da-4716-9e34.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Software Engineer - Twitch Crates',
          'twitter:description': 'Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing ▒gig economy▒ which allows these creators to earn part or all of their income by producing high quality content on Twitch. Twitch Crates was introduced earlier this year as part of our Game Commerce strategy and we are looking for engineers who want to take it to the next level and scale it across other dimensions on Twitch. Crates provides additional value to viewers engaging on Twitch, as well as more interesting and unique ways for Broadcasters, Game Developers and other influencers to reach their audience and monetize their content. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible Web application software. You are a full stack developer who is comfortable with Javascript',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Software Engineer - Twitch Crates',
          'og:description': 'Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing ▒gig economy▒ which allows these creators to earn part or all of their income by producing high quality content on Twitch. Twitch Crates was introduced earlier this year as part of our Game Commerce strategy and we are looking for engineers who want to take it to the next level and scale it across other dimensions on Twitch. Crates provides additional value to viewers engaging on Twitch, as well as more interesting and unique ways for Broadcasters, Game Developers and other influencers to reach their audience and monetize their content. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible Web application software. You are a full stack developer who is comfortable with Javascript',
          'og:url': 'https://jobs.lever.co/twitch/4a17fcc9-b8da-4716-9e34-78663265b4f9/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Sr. Software Engineer - Tools & Automation',
    'htmlTitle': 'Twitch - Sr. <b>Software Engineer</b> - Tools &amp; Automation',
    'link': 'https://jobs.lever.co/twitch/fca29bb0-5212-4d26-8436-82533f079f88/',
    'displayLink': 'jobs.lever.co',
    'snippet': '7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\xa0...',
    'htmlSnippet': '7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...',
    'cacheId': 'rpqI5q91cI4J',
    'formattedUrl': 'https://jobs.lever.co/twitch/fca29bb0-5212-4d26-8436.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/fca29bb0-5212-4d26-8436.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Sr. Software Engineer - Tools & Automation',
          'twitter:description': 'Twitch is seeking an experienced Software Engineer for our Quality Engineering team, who will be responsible for our test infrastructure and will be the quality champion of Twitch. As a Software Engineer,Tools , you will be responsible for establishing a consistent testing methodology for all products we release and promoting best practices across our many product development teams.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Sr. Software Engineer - Tools & Automation',
          'og:description': 'Twitch is seeking an experienced Software Engineer for our Quality Engineering team, who will be responsible for our test infrastructure and will be the quality champion of Twitch. As a Software Engineer,Tools , you will be responsible for establishing a consistent testing methodology for all products we release and promoting best practices across our many product development teams.',
          'og:url': 'https://jobs.lever.co/twitch/fca29bb0-5212-4d26-8436-82533f079f88/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Quality Engineer - Core Payments',
    'htmlTitle': 'Twitch - Senior Quality <b>Engineer</b> - Core Payments',
    'link': 'https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31',
    'displayLink': 'jobs.lever.co',
    'snippet': 'As a Senior Software Engineer in Test for Core Payments team, you will be \nworking closely with development and various other cross-functional teams to \nensure\xa0...',
    'htmlSnippet': 'As a Senior <b>Software Engineer</b> in Test for Core Payments team, you will be <br>\nworking closely with development and various other cross-functional teams to <br>\nensure&nbsp;...',
    'cacheId': 'ujXW9reMdCoJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Quality Engineer - Core Payments',
          'twitter:description': 'Core Payments team owns product/systems that affect millions of users and broadcasters. Our platforms enable automated onboarding as well as payments processing so its role is essential for the company. The teams are directly responsible in ensuring high quality world class payments experiences for our users. As a Senior Software Engineer in Test for Core Payments team, you will be working closely with development and various other cross-functional teams to ensure the highest quality for our projects.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Quality Engineer - Core Payments',
          'og:description': 'Core Payments team owns product/systems that affect millions of users and broadcasters. Our platforms enable automated onboarding as well as payments processing so its role is essential for the company. The teams are directly responsible in ensuring high quality world class payments experiences for our users. As a Senior Software Engineer in Test for Core Payments team, you will be working closely with development and various other cross-functional teams to ensure the highest quality for our projects.',
          'og:url': 'https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - iOS Engineer',
    'htmlTitle': 'Twitch - iOS <b>Engineer</b>',
    'link': 'https://jobs.lever.co/twitch/5777f110-4e1f-4dbd-85dc-219187e9caae',
    'displayLink': 'jobs.lever.co',
    'snippet': 'As an iOS Software Engineer, you will make major contributions to a rapidly-\nevolving, native app that is a portal to the Twitch community for millions of users.',
    'htmlSnippet': 'As an iOS <b>Software Engineer</b>, you will make major contributions to a rapidly-<br>\nevolving, native app that is a portal to the Twitch community for millions of users.',
    'cacheId': 'D-LQ1zCdz1QJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/5777f110-4e1f-4dbd-85dc-219187e9caae',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/5777f110-4e1f-4dbd-85dc-219187e9caae',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - iOS Engineer',
          'twitter:description': 'Twitch▒s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As an iOS Software Engineer, you will make major contributions to a rapidly-evolving, native app that is a portal to the Twitch community for millions of users.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - iOS Engineer',
          'og:description': 'Twitch▒s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As an iOS Software Engineer, you will make major contributions to a rapidly-evolving, native app that is a portal to the Twitch community for millions of users.',
          'og:url': 'https://jobs.lever.co/twitch/5777f110-4e1f-4dbd-85dc-219187e9caae',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Mobile Web Engineer',
    'htmlTitle': 'Twitch - Mobile Web <b>Engineer</b>',
    'link': 'https://jobs.lever.co/twitch/8cfac0c5-5073-431f-a4bb-ed554d5f4f3b',
    'displayLink': 'jobs.lever.co',
    'snippet': 'As an engineer on the Mobile Web team you will have the opportunity to work ... 2\n+ years of web development experience; Strong software engineering\xa0...',
    'htmlSnippet': 'As an engineer on the Mobile Web team you will have the opportunity to work ... 2<br>\n+ years of web development experience; Strong <b>software engineering</b>&nbsp;...',
    'cacheId': 'AHrJKgI-EJgJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/8cfac0c5-5073-431f-a4bb-ed554d5f4f3b',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/8cfac0c5-5073-431f-a4bb-ed554d5f4f3b',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Mobile Web Engineer',
          'twitter:description': 'Usage of Twitch on mobile devices continues to grow very rapidly, most of which currently happens on our very popular, and highly rated, Android and iOS applications. We want to bring the same great experience to our mobile website and are building a team to craft a completely new Twitch experience for the millions of people that use the Twitch website on mobile devices. The new mobile website will be a multiple entry point, universal React/Redux application. As an engineer on the Mobile Web team you will have the opportunity to work throughout the stack and own major pieces of the mobile website.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Mobile Web Engineer',
          'og:description': 'Usage of Twitch on mobile devices continues to grow very rapidly, most of which currently happens on our very popular, and highly rated, Android and iOS applications. We want to bring the same great experience to our mobile website and are building a team to craft a completely new Twitch experience for the millions of people that use the Twitch website on mobile devices. The new mobile website will be a multiple entry point, universal React/Redux application. As an engineer on the Mobile Web team you will have the opportunity to work throughout the stack and own major pieces of the mobile website.',
          'og:url': 'https://jobs.lever.co/twitch/8cfac0c5-5073-431f-a4bb-ed554d5f4f3b',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Distributed Systems Engineer - Berlin (m/f)',
    'htmlTitle': 'Twitch - Distributed Systems <b>Engineer</b> - Berlin (m/f)',
    'link': 'https://jobs.lever.co/twitch/f7b4e33b-bea1-4da2-be16-94df0e57a87b',
    'displayLink': 'jobs.lever.co',
    'snippet': 'We are looking for engineers who are excited by the thought of working across \nthe ... working in a professional software engineering environment (with source\xa0...',
    'htmlSnippet': 'We are looking for engineers who are excited by the thought of working across <br>\nthe ... working in a professional <b>software engineering</b> environment (with source&nbsp;...',
    'cacheId': 'sHhkuAG1oygJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/f7b4e33b-bea1-4da2-be16-94df0e57a87b',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/f7b4e33b-bea1-4da2-be16-94df0e57a87b',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Distributed Systems Engineer - Berlin (m/f)',
          'twitter:description': 'Twitch is building the future of interactive entertainment. Ensuring smooth, low-latency video across the world requires large-scale, fault-tolerant systems that can keep up with millions of simultaneous viewers and thousands of broadcasters. We are looking for engineers who are excited by the thought of working across the entire stack, from service load-balancing, to performance optimization, to backbone traffic management. You will help architect, develop, test, deploy, operate, and maintain our video software software. As part of the team, we will work together to enable our broadcasters and viewers to create and interact in new, innovative ways.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Distributed Systems Engineer - Berlin (m/f)',
          'og:description': 'Twitch is building the future of interactive entertainment. Ensuring smooth, low-latency video across the world requires large-scale, fault-tolerant systems that can keep up with millions of simultaneous viewers and thousands of broadcasters. We are looking for engineers who are excited by the thought of working across the entire stack, from service load-balancing, to performance optimization, to backbone traffic management. You will help architect, develop, test, deploy, operate, and maintain our video software software. As part of the team, we will work together to enable our broadcasters and viewers to create and interact in new, innovative ways.',
          'og:url': 'https://jobs.lever.co/twitch/f7b4e33b-bea1-4da2-be16-94df0e57a87b',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Distributed Systems Engineer',
    'htmlTitle': 'Twitch - Distributed Systems <b>Engineer</b>',
    'link': 'https://jobs.lever.co/twitch/8929e219-138d-473c-8acd-4fcc3e01fc0a',
    'displayLink': 'jobs.lever.co',
    'snippet': 'We are looking for engineers who are excited by the thought of working across \nthe ... working in a professional software engineering environment (with source\xa0...',
    'htmlSnippet': 'We are looking for engineers who are excited by the thought of working across <br>\nthe ... working in a professional <b>software engineering</b> environment (with source&nbsp;...',
    'cacheId': '2WyXXOrIqOYJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/8929e219-138d-473c-8acd-4fcc3e01fc0a',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/8929e219-138d-473c-8acd-4fcc3e01fc0a',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Distributed Systems Engineer',
          'twitter:description': 'Twitch is building the future of interactive entertainment. Ensuring smooth, low-latency video across the world requires large-scale, fault-tolerant systems that can keep up with millions of simultaneous viewers and thousands of broadcasters. We are looking for engineers who are excited by the thought of working across the entire stack, from service load-balancing, to performance optimization, to backbone traffic management. You will help architect, develop, test, deploy, operate, and maintain our video software software. As part of the team, we will work together to enable our broadcasters and viewers to create and interact in new, innovative ways.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Distributed Systems Engineer',
          'og:description': 'Twitch is building the future of interactive entertainment. Ensuring smooth, low-latency video across the world requires large-scale, fault-tolerant systems that can keep up with millions of simultaneous viewers and thousands of broadcasters. We are looking for engineers who are excited by the thought of working across the entire stack, from service load-balancing, to performance optimization, to backbone traffic management. You will help architect, develop, test, deploy, operate, and maintain our video software software. As part of the team, we will work together to enable our broadcasters and viewers to create and interact in new, innovative ways.',
          'og:url': 'https://jobs.lever.co/twitch/8929e219-138d-473c-8acd-4fcc3e01fc0a',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior iOS Engineer',
    'htmlTitle': 'Twitch - Senior iOS <b>Engineer</b>',
    'link': 'https://jobs.lever.co/twitch/1a5a24ed-4bed-43f4-8774-195bf28f0cbd',
    'displayLink': 'jobs.lever.co',
    'snippet': 'As a Senior iOS Software Engineer, you will provide technical leadership and \nmake direct contributions to an app that is the portal to the Twitch community for\xa0...',
    'htmlSnippet': 'As a Senior iOS <b>Software Engineer</b>, you will provide technical leadership and <br>\nmake direct contributions to an app that is the portal to the Twitch community for&nbsp;...',
    'cacheId': 'xiBSutZWP9IJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/1a5a24ed-4bed-43f4-8774-195bf28f0cbd',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/1a5a24ed-4bed-43f4-8774-195bf28f0cbd',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior iOS Engineer',
          'twitter:description': 'Twitch▒s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As a Senior iOS Software Engineer, you will provide technical leadership and make direct contributions to an app that is the portal to the Twitch community for millions of users.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior iOS Engineer',
          'og:description': 'Twitch▒s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As a Senior iOS Software Engineer, you will provide technical leadership and make direct contributions to an app that is the portal to the Twitch community for millions of users.',
          'og:url': 'https://jobs.lever.co/twitch/1a5a24ed-4bed-43f4-8774-195bf28f0cbd',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch',
    'htmlTitle': 'Twitch',
    'link': 'https://jobs.lever.co/twitch?location=San%20Francisco%2C%20CA',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Senior Software Engineer - Video Client. San Francisco, CABroadcaster Success \n▒ Core Player TechnologiesFull-time ▒ Apply\xa0...',
    'htmlSnippet': 'Senior <b>Software Engineer</b> - Video Client. San Francisco, CABroadcaster Success <br>\n▒ Core Player TechnologiesFull-time &middot; Apply&nbsp;...',
    'cacheId': 'W-OkXRXYmOoJ',
    'formattedUrl': 'https://jobs.lever.co/twitch?location=San%20Francisco%2C%20CA',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch?location=San%20Francisco%2C%20CA',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch',
          'twitter:description': 'Job openings at Twitch',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch jobs',
          'og:description': 'Job openings at Twitch',
          'og:url': 'https://jobs.lever.co/twitch',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch',
    'htmlTitle': 'Twitch',
    'link': 'https://jobs.lever.co/twitch?by=location',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Senior Software Engineer - Internationalization. Irvine, CAClients Platform & \nProduct Development ▒ Clients EngineeringFull-time. Location Flexible / San\xa0...',
    'htmlSnippet': 'Senior <b>Software Engineer</b> - Internationalization. Irvine, CAClients Platform &amp; <br>\nProduct Development ▒ Clients EngineeringFull-time. Location Flexible / San&nbsp;...',
    'cacheId': '1PL04KCv1NgJ',
    'formattedUrl': 'https://jobs.lever.co/twitch?by=location',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch?by=location',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch',
          'twitter:description': 'Job openings at Twitch',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch jobs',
          'og:description': 'Job openings at Twitch',
          'og:url': 'https://jobs.lever.co/twitch',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Backend Engineer, Infrastructure (C#)',
    'htmlTitle': 'Twitch - Backend <b>Engineer</b>, Infrastructure (C#)',
    'link': 'https://jobs.lever.co/twitch/63a55490-942f-4717-ac81-c86c31dad2ae',
    'displayLink': 'jobs.lever.co',
    'snippet': 'As a software engineer working on the Client Platforms Engineering (CPE) team \nyou will help develop the systems and services powering the next generation of\xa0...',
    'htmlSnippet': 'As a <b>software engineer</b> working on the Client Platforms Engineering (CPE) team <br>\nyou will help develop the systems and services powering the next generation of&nbsp;...',
    'cacheId': 'DL8xqgPDu1cJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/63a55490-942f-4717-ac81-c86c31dad2ae',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/63a55490-942f-4717-ac81-c86c31dad2ae',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Backend Engineer, Infrastructure (C#)',
          'twitter:description': 'As a software engineer working on the Client Platforms Engineering (CPE) team you will help develop the systems and services powering the next generation of Twitch clients. We in CPE strive to provide Twitch developers the best development platform as well as building robust services for the deployed applications. The tools and services you develop will be used by hundreds of developers and help enhance the Twitch.tv experience for millions.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Backend Engineer, Infrastructure (C#)',
          'og:description': 'As a software engineer working on the Client Platforms Engineering (CPE) team you will help develop the systems and services powering the next generation of Twitch clients. We in CPE strive to provide Twitch developers the best development platform as well as building robust services for the deployed applications. The tools and services you develop will be used by hundreds of developers and help enhance the Twitch.tv experience for millions.',
          'og:url': 'https://jobs.lever.co/twitch/63a55490-942f-4717-ac81-c86c31dad2ae',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch',
    'htmlTitle': 'Twitch',
    'link': 'https://jobs.lever.co/twitch?by=location&location=San%20Francisco%2C%20CA',
    'displayLink': 'jobs.lever.co',
    'snippet': 'San Francisco, CACommerce ▒ Developer Product EngineeringFull-time ▒ Apply \n.... Senior Software Engineer - Global Infrastructure. San Francisco\xa0...',
    'htmlSnippet': 'San Francisco, CACommerce ▒ Developer Product EngineeringFull-time &middot; Apply <br>\n.... Senior <b>Software Engineer</b> - Global Infrastructure. San Francisco&nbsp;...',
    'cacheId': 'fBjr9tLpOBgJ',
    'formattedUrl': 'https://jobs.lever.co/twitch?by=location&location...',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch?by=location&amp;location...',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch',
          'twitter:description': 'Job openings at Twitch',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch jobs',
          'og:description': 'Job openings at Twitch',
          'og:url': 'https://jobs.lever.co/twitch',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Engineering Manager - Mobile',
    'htmlTitle': 'Twitch - <b>Engineering</b> Manager - Mobile',
    'link': 'https://jobs.lever.co/twitch/0bfcaf1e-0059-4ed6-b9a7-644a205dad55',
    'displayLink': 'jobs.lever.co',
    'snippet': "Twitch's Mobile Engineering team is responsible for developing viewing \napplications ... software development experience; 2+ years experience as \nengineering\xa0...",
    'htmlSnippet': 'Twitch&#39;s Mobile <b>Engineering</b> team is responsible for developing viewing <br>\napplications ... <b>software</b> development experience; 2+ years experience as <br>\n<b>engineering</b>&nbsp;...',
    'cacheId': 'Sc7-F37rqz4J',
    'formattedUrl': 'https://jobs.lever.co/twitch/0bfcaf1e-0059-4ed6-b9a7-644a205dad55',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/0bfcaf1e-0059-4ed6-b9a7-644a205dad55',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Engineering Manager - Mobile',
          'twitter:description': 'Twitch▒s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet, and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As an Engineering Manager you▒ll help grow our Mobile Engineering team to deliver on our expanding mobile product scope, while maintaining a very high quality and stability bar for the applications.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Engineering Manager - Mobile',
          'og:description': 'Twitch▒s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet, and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As an Engineering Manager you▒ll help grow our Mobile Engineering team to deliver on our expanding mobile product scope, while maintaining a very high quality and stability bar for the applications.',
          'og:url': 'https://jobs.lever.co/twitch/0bfcaf1e-0059-4ed6-b9a7-644a205dad55',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - IT Support Engineer',
    'htmlTitle': 'Twitch - IT Support <b>Engineer</b>',
    'link': 'https://jobs.lever.co/twitch/3c9d03da-50b2-452e-9b85-b81760987f81',
    'displayLink': 'jobs.lever.co',
    'snippet': 'The IT Support engineer will provide hands-on support for client hardware and \nsoftware on Windows, Mac, and Linux systems. They also support networking\xa0...',
    'htmlSnippet': 'The IT Support <b>engineer</b> will provide hands-on support for client hardware and <br>\n<b>software</b> on Windows, Mac, and Linux systems. They also support networking&nbsp;...',
    'cacheId': 'riEjFLvBkBwJ',
    'formattedUrl': 'https://jobs.lever.co/.../3c9d03da-50b2-452e-9b85-b81760987f81',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../3c9d03da-50b2-452e-9b85-b81760987f81',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - IT Support Engineer',
          'twitter:description': "How do we take millions of content creators, connect them with tens of millions of viewers, on a platform that is second to none? It starts with welcoming everyone but choosing only the best. It's the willingness to experiment to decide, and about commitment, not compliance. These are just a few of the driving principles behind the Twitch IT organization. Twitch has an immediate opening for an IT Support Engineer in our San Francisco office. The IT Support Engineer serves as IT Support for Twitch business units and corporate offices within the San Francisco area. The IT Support engineer will provide hands-on support for client hardware and software on Windows, Mac, and Linux systems. They also support networking and local server resources for their site. Regular activities include PC imaging and repair, network troubleshooting, project management, mentor-ship of junior technicians, systems administration in a variety of software and hardware environments, telecom administration, a",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - IT Support Engineer',
          'og:description': "How do we take millions of content creators, connect them with tens of millions of viewers, on a platform that is second to none? It starts with welcoming everyone but choosing only the best. It's the willingness to experiment to decide, and about commitment, not compliance. These are just a few of the driving principles behind the Twitch IT organization. Twitch has an immediate opening for an IT Support Engineer in our San Francisco office. The IT Support Engineer serves as IT Support for Twitch business units and corporate offices within the San Francisco area. The IT Support engineer will provide hands-on support for client hardware and software on Windows, Mac, and Linux systems. They also support networking and local server resources for their site. Regular activities include PC imaging and repair, network troubleshooting, project management, mentor-ship of junior technicians, systems administration in a variety of software and hardware environments, telecom administration, a",
          'og:url': 'https://jobs.lever.co/twitch/3c9d03da-50b2-452e-9b85-b81760987f81',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior Director of Engineering - Payments Platform',
    'htmlTitle': 'Twitch - Senior Director of <b>Engineering</b> - Payments Platform',
    'link': 'https://jobs.lever.co/twitch/beef5266-833a-4570-8a7c-79101ad558b3',
    'displayLink': 'jobs.lever.co',
    'snippet': 'BS in Computer Science or Engineering (or equivalent); Strong technical \ncredentials, with at least 10 years experience managing software development \nteams,\xa0...',
    'htmlSnippet': 'BS in Computer Science or <b>Engineering</b> (or equivalent); Strong technical <br>\ncredentials, with at least 10 years experience managing <b>software</b> development <br>\nteams,&nbsp;...',
    'cacheId': 'x9hYjn88feMJ',
    'formattedUrl': 'https://jobs.lever.co/.../beef5266-833a-4570-8a7c-79101ad558b3',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../beef5266-833a-4570-8a7c-79101ad558b3',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior Director of Engineering - Payments Platform',
          'twitter:description': 'Twitch is building the future of interactive entertainment and Commerce is ensuring our content creators can make a living doing what they love. The Payments team in Commerce is focused on ensuring our global audience is able to pay in a localized experienced with payment methods that are familiar and accessible and ensuring our tens of thousands of creators are paid accurately, timely, and conveniently. These experiences are the foundation of Twitch▒s explosive growth and we are hiring a senior technical leader to lead multiple engineering teams enhancing these capabilities. You will play a leading role in defining the vision for our service and in building a world-class engineering organization to execute to that vision. You will work closely with the individual contributors and managers on your teams, as well as cross-team with engineering, product, operations and business leadership to deliver high visible results. The ideal candidate must have demonstrated ability to build a',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior Director of Engineering - Payments Platform',
          'og:description': 'Twitch is building the future of interactive entertainment and Commerce is ensuring our content creators can make a living doing what they love. The Payments team in Commerce is focused on ensuring our global audience is able to pay in a localized experienced with payment methods that are familiar and accessible and ensuring our tens of thousands of creators are paid accurately, timely, and conveniently. These experiences are the foundation of Twitch▒s explosive growth and we are hiring a senior technical leader to lead multiple engineering teams enhancing these capabilities. You will play a leading role in defining the vision for our service and in building a world-class engineering organization to execute to that vision. You will work closely with the individual contributors and managers on your teams, as well as cross-team with engineering, product, operations and business leadership to deliver high visible results. The ideal candidate must have demonstrated ability to build a',
          'og:url': 'https://jobs.lever.co/twitch/beef5266-833a-4570-8a7c-79101ad558b3',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Video Processing Engineer',
    'htmlTitle': 'Twitch - Video Processing <b>Engineer</b>',
    'link': 'https://jobs.lever.co/twitch/85cb890f-baa2-4cc6-8c20-33ec707bd1fe',
    'displayLink': 'jobs.lever.co',
    'snippet': 'As a Video Processing Engineer, you will be working on the core transcoding \nand transmuxing software which produces all of the video data we serve to our\xa0...',
    'htmlSnippet': 'As a Video Processing <b>Engineer</b>, you will be working on the core transcoding <br>\nand transmuxing <b>software</b> which produces all of the video data we serve to our&nbsp;...',
    'cacheId': 't-zGalr_ppMJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/85cb890f-baa2-4cc6-8c20-33ec707bd1fe',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/85cb890f-baa2-4cc6-8c20-33ec707bd1fe',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Video Processing Engineer',
          'twitter:description': 'Video/audio processing and delivery is one of Twitch▒s core competencies. We operate one of the largest private CDNs (Content Delivery Network) and deliver live video to millions of concurrent viewers (10 millions daily active users). Our ingest system processes 4 years of video every hour and services 2+ million unique streamers per month. As a Video Processing Engineer, you will be working on the core transcoding and transmuxing software which produces all of the video data we serve to our viewers on various platforms. This will include both research and development projects as well as ongoing software maintenance, all in the interest of providing the best viewing experience possible to our users.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Video Processing Engineer',
          'og:description': 'Video/audio processing and delivery is one of Twitch▒s core competencies. We operate one of the largest private CDNs (Content Delivery Network) and deliver live video to millions of concurrent viewers (10 millions daily active users). Our ingest system processes 4 years of video every hour and services 2+ million unique streamers per month. As a Video Processing Engineer, you will be working on the core transcoding and transmuxing software which produces all of the video data we serve to our viewers on various platforms. This will include both research and development projects as well as ongoing software maintenance, all in the interest of providing the best viewing experience possible to our users.',
          'og:url': 'https://jobs.lever.co/twitch/85cb890f-baa2-4cc6-8c20-33ec707bd1fe',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch',
    'htmlTitle': 'Twitch',
    'link': 'https://jobs.lever.co/twitch?location=Irvine%2C%20CA',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Engineering Manager - Browser Clients. Irvine, CAClients ... Frontend Engineer - \nBrowser Clients. Irvine ... Software Engineer - Desktop Clients (C#). Irvine\xa0...',
    'htmlSnippet': 'Engineering Manager - Browser Clients. Irvine, CAClients ... Frontend Engineer - <br>\nBrowser Clients. Irvine ... <b>Software Engineer</b> - Desktop Clients (C#). Irvine&nbsp;...',
    'cacheId': 'YwweuHgiZF8J',
    'formattedUrl': 'https://jobs.lever.co/twitch?location=Irvine%2C%20CA',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch?location=Irvine%2C%20CA',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch',
          'twitter:description': 'Job openings at Twitch',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch jobs',
          'og:description': 'Job openings at Twitch',
          'og:url': 'https://jobs.lever.co/twitch',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch',
    'htmlTitle': 'Twitch',
    'link': 'https://jobs.lever.co/twitch?by=location&location=Irvine%2C%20CA',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Frontend Engineer - Browser Clients ... Irvine, CACommerce ▒ Developer \nRelations EngineeringFull-time ▒ Apply ▒ Software Engineer - Desktop Clients (C\n#).',
    'htmlSnippet': 'Frontend Engineer - Browser Clients ... Irvine, CACommerce ▒ Developer <br>\nRelations EngineeringFull-time &middot; Apply &middot; <b>Software Engineer</b> - Desktop Clients (C<br>\n#).',
    'cacheId': '__X4k5eEjgEJ',
    'formattedUrl': 'https://jobs.lever.co/twitch?by=location&location...',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch?by=location&amp;location...',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch',
          'twitter:description': 'Job openings at Twitch',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch jobs',
          'og:description': 'Job openings at Twitch',
          'og:url': 'https://jobs.lever.co/twitch',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Frontend Engineer - Twitch Crates',
    'htmlTitle': 'Twitch - Frontend <b>Engineer</b> - Twitch Crates',
    'link': 'https://jobs.lever.co/twitch/7f6218d3-ca90-4daf-abfe-cd693a5ad76b',
    'displayLink': 'jobs.lever.co',
    'snippet': 'This role is perfect for an engineer who has a passion for building high quality, \nreliable, extensible Web application software. You are passionate about best\xa0...',
    'htmlSnippet': 'This role is perfect for an <b>engineer</b> who has a passion for building high quality, <br>\nreliable, extensible Web application <b>software</b>. You are passionate about best&nbsp;...',
    'cacheId': 'YgRjcZC4EQwJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/7f6218d3-ca90-4daf-abfe-cd693a5ad76b',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/7f6218d3-ca90-4daf-abfe-cd693a5ad76b',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Frontend Engineer - Twitch Crates',
          'twitter:description': 'Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing ▒gig economy▒ which allows these creators to earn part or all of their income by producing high quality content on Twitch. Twitch Crates was introduced earlier this year as part of our Game Commerce strategy and we are looking for engineers who want to take it to the next level and scale it across other dimensions on Twitch. Crates provides additional value to viewers engaging on Twitch, as well as more interesting and unique ways for Broadcasters, Game Developers and other influencers to reach their audience and monetize their content. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible Web application software. You are passionate about best practices and comfortable with Jav',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Frontend Engineer - Twitch Crates',
          'og:description': 'Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing ▒gig economy▒ which allows these creators to earn part or all of their income by producing high quality content on Twitch. Twitch Crates was introduced earlier this year as part of our Game Commerce strategy and we are looking for engineers who want to take it to the next level and scale it across other dimensions on Twitch. Crates provides additional value to viewers engaging on Twitch, as well as more interesting and unique ways for Broadcasters, Game Developers and other influencers to reach their audience and monetize their content. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible Web application software. You are passionate about best practices and comfortable with Jav',
          'og:url': 'https://jobs.lever.co/twitch/7f6218d3-ca90-4daf-abfe-cd693a5ad76b',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior DevOps Engineer - Extensions',
    'htmlTitle': 'Twitch - Senior DevOps <b>Engineer</b> - Extensions',
    'link': 'https://jobs.lever.co/twitch/aad8df8f-9b94-4141-8805-0e9eeae5c08c',
    'displayLink': 'jobs.lever.co',
    'snippet': 'This team needs a senior DevOps engineer, who is able to channel their ... \nautomated CI/CD pipelines, managing the lifecycle of software infrastructure, and\n\xa0...',
    'htmlSnippet': 'This team needs a senior DevOps <b>engineer</b>, who is able to channel their ... <br>\nautomated CI/CD pipelines, managing the lifecycle of <b>software</b> infrastructure, and<br>\n&nbsp;...',
    'cacheId': 'UNG3yr518MUJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/aad8df8f-9b94-4141-8805-0e9eeae5c08c',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/aad8df8f-9b94-4141-8805-0e9eeae5c08c',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior DevOps Engineer - Extensions',
          'twitter:description': 'Twitch developer products power the connections between millions of broadcasters and users. This position will be part of the team responsible for providing new interactive ways to connect on Twitch. This team needs a senior DevOps engineer, who is able to channel their years of experience in building automated CI/CD pipelines, managing the lifecycle of software infrastructure, and driving a shared vision for such work forward with the team.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior DevOps Engineer - Extensions',
          'og:description': 'Twitch developer products power the connections between millions of broadcasters and users. This position will be part of the team responsible for providing new interactive ways to connect on Twitch. This team needs a senior DevOps engineer, who is able to channel their years of experience in building automated CI/CD pipelines, managing the lifecycle of software infrastructure, and driving a shared vision for such work forward with the team.',
          'og:url': 'https://jobs.lever.co/twitch/aad8df8f-9b94-4141-8805-0e9eeae5c08c',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Software Development Manager - Game Commerce',
    'htmlTitle': 'Twitch - <b>Software</b> Development Manager - Game Commerce',
    'link': 'https://jobs.lever.co/twitch/d253d6be-f921-4b2c-8059-e0ad45090a62',
    'displayLink': 'jobs.lever.co',
    'snippet': "You'll lead a talented and nimble team of engineers to create innovative ways to \n... for software within the team, and management of resources across teams.",
    'htmlSnippet': 'You&#39;ll lead a talented and nimble team of <b>engineers</b> to create innovative ways to <br>\n... for <b>software</b> within the team, and management of resources across teams.',
    'cacheId': 'ccNyH9ZgP_MJ',
    'formattedUrl': 'https://jobs.lever.co/.../d253d6be-f921-4b2c-8059-e0ad45090a62',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../d253d6be-f921-4b2c-8059-e0ad45090a62',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Software Development Manager - Game Commerce',
          'twitter:description': "The Game Commerce team at Twitch is looking for a passionate, results-oriented, inventive software manager to continue our rapid feature development for Twitch Game Commerce. The candidate thrives in a fast-paced environment, understands the gaming and streaming space, and will help us bring new and innovative solutions to our viewers and broadcasters. As the development manager, you will have technical ownership of the customer experience for Game Commerce. You'll lead a talented and nimble team of engineers to create innovative ways to maintain a high velocity delivery of features from our product roadmap. Responsibilities include direct management of 5+ engineers, process and quality of service improvements, strategic planning, project management for software within the team, and management of resources across teams. Successful candidates will be strong leaders who can prioritize well, communicate clearly, and have a consistent track record of delivery. The Game Commerce business r",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Software Development Manager - Game Commerce',
          'og:description': "The Game Commerce team at Twitch is looking for a passionate, results-oriented, inventive software manager to continue our rapid feature development for Twitch Game Commerce. The candidate thrives in a fast-paced environment, understands the gaming and streaming space, and will help us bring new and innovative solutions to our viewers and broadcasters. As the development manager, you will have technical ownership of the customer experience for Game Commerce. You'll lead a talented and nimble team of engineers to create innovative ways to maintain a high velocity delivery of features from our product roadmap. Responsibilities include direct management of 5+ engineers, process and quality of service improvements, strategic planning, project management for software within the team, and management of resources across teams. Successful candidates will be strong leaders who can prioritize well, communicate clearly, and have a consistent track record of delivery. The Game Commerce business r",
          'og:url': 'https://jobs.lever.co/twitch/d253d6be-f921-4b2c-8059-e0ad45090a62',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Application Security Engineer',
    'htmlTitle': 'Twitch - Application Security <b>Engineer</b>',
    'link': 'https://jobs.lever.co/twitch/f2537fe4-6c4e-4f22-a002-4455dda80675',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Twitch is looking for a focused Application Security Engineer with a desire to ... \nDemonstrated software development proficiency (Go, Ruby, Python, Java, C#,\xa0...',
    'htmlSnippet': 'Twitch is looking for a focused Application Security <b>Engineer</b> with a desire to ... <br>\nDemonstrated <b>software</b> development proficiency (Go, Ruby, Python, Java, C#,&nbsp;...',
    'cacheId': 'bqpGsYN3G3sJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/f2537fe4-6c4e-4f22-a002-4455dda80675',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/f2537fe4-6c4e-4f22-a002-4455dda80675',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Application Security Engineer',
          'twitter:description': 'Twitch is looking for a focused Application Security Engineer with a desire to play on the Blue Team. Maybe you▒re a pentester who is bored of always winning; maybe you▒re the local security champion within your development organization. However you got to where you are, we want one thing from you - help make Twitch▒s products as safe as they can be for our partners and viewers. In this role, you will be escorting Twitch▒s products and features from ideation to deployment. You will be providing consulting to product teams looking to try new things safely. You will be reviewing critical passages of code for adherence to standards and safe practices. Most importantly, you will be helping to build and automate the tools that do the above for you as a force multiplier. And yes, where warranted, there▒s some pentesting in it for you as well. You know, if you▒re into that.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Application Security Engineer',
          'og:description': 'Twitch is looking for a focused Application Security Engineer with a desire to play on the Blue Team. Maybe you▒re a pentester who is bored of always winning; maybe you▒re the local security champion within your development organization. However you got to where you are, we want one thing from you - help make Twitch▒s products as safe as they can be for our partners and viewers. In this role, you will be escorting Twitch▒s products and features from ideation to deployment. You will be providing consulting to product teams looking to try new things safely. You will be reviewing critical passages of code for adherence to standards and safe practices. Most importantly, you will be helping to build and automate the tools that do the above for you as a force multiplier. And yes, where warranted, there▒s some pentesting in it for you as well. You know, if you▒re into that.',
          'og:url': 'https://jobs.lever.co/twitch/f2537fe4-6c4e-4f22-a002-4455dda80675',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Event Marketing Manager',
    'htmlTitle': 'Twitch - Event Marketing Manager',
    'link': 'https://jobs.lever.co/twitch/752ef652-23af-4228-8221-f9bd4b2f35ad',
    'displayLink': 'jobs.lever.co',
    'snippet': '... Success marketing a B2B solution specified or purchased by software \nengineers; ideally in gaming; Success in using data to inform your campaign \nplanning\xa0...',
    'htmlSnippet': '... Success marketing a B2B solution specified or purchased by <b>software</b> <br>\n<b>engineers</b>; ideally in gaming; Success in using data to inform your campaign <br>\nplanning&nbsp;...',
    'cacheId': 'jFc8D0ii-aEJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/752ef652-23af-4228-8221-f9bd4b2f35ad',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/752ef652-23af-4228-8221-f9bd4b2f35ad',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Event Marketing Manager',
          'twitter:description': 'As creators of the games and apps Twitch broadcasters and viewers revel in, developers are incredibly important partners for Twitch. They are already reaching tens of millions of viewers on Twitch today; we want to help them wrap even more broadcasters, viewers and users into their products. The Developer Success team helps creators make compelling apps that stand out, present their products to viewers who may like them, engage with their existing users, and find innovative new ways to generate revenue. We▒d like you to build and scale the event channels through which we invite developers to engage with us. You▒ll apply your expertise in event marketing to event experiences that help developers understand how Twitch can help them succeed. Through creating scalable campaigns both pre / post events , you will measure outcomes against business goals using data. We win when thousands of companies clamor to partner with us; you win when you▒ve created event marketing experiences that inspi',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Event Marketing Manager',
          'og:description': 'As creators of the games and apps Twitch broadcasters and viewers revel in, developers are incredibly important partners for Twitch. They are already reaching tens of millions of viewers on Twitch today; we want to help them wrap even more broadcasters, viewers and users into their products. The Developer Success team helps creators make compelling apps that stand out, present their products to viewers who may like them, engage with their existing users, and find innovative new ways to generate revenue. We▒d like you to build and scale the event channels through which we invite developers to engage with us. You▒ll apply your expertise in event marketing to event experiences that help developers understand how Twitch can help them succeed. Through creating scalable campaigns both pre / post events , you will measure outcomes against business goals using data. We win when thousands of companies clamor to partner with us; you win when you▒ve created event marketing experiences that inspi',
          'og:url': 'https://jobs.lever.co/twitch/752ef652-23af-4228-8221-f9bd4b2f35ad',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Senior UX Designer - Games Commerce',
    'htmlTitle': 'Twitch - Senior UX Designer - Games Commerce',
    'link': 'https://jobs.lever.co/twitch/0097ec3a-9863-4771-8001-24022b058536',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Commerce ▒ Games Store Engineering ... use your passion, ingenuity, \nexperience, and pragmatism to build very cool software that affects millions of \ncustomers.',
    'htmlSnippet': 'Commerce ▒ Games Store <b>Engineering</b> ... use your passion, ingenuity, <br>\nexperience, and pragmatism to build very cool <b>software</b> that affects millions of <br>\ncustomers.',
    'cacheId': 'NjJ4nomD3uYJ',
    'formattedUrl': 'https://jobs.lever.co/.../0097ec3a-9863-4771-8001-24022b058536',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../0097ec3a-9863-4771-8001-24022b058536',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Senior UX Designer - Games Commerce',
          'twitter:description': "The Twitch Seattle team is seeking a gifted Senior UX Designer to drive user experiences for exciting new opportunities and projects. We offer a series of stimulating problems, an environment that's exciting, motivating, fun, and new. You will have colleagues who will challenge you to achieve more than you thought possible, as well as great camaraderie. Joining our team will give you endless opportunities to use your passion, ingenuity, experience, and pragmatism to build very cool software that affects millions of customers. Our ideal Senior UX Designer will exhibit a strong passion for building top-notch gamer-oriented web and software experiences based on a well-rounded set of design skills that range from wireframes to full fidelity design comps.",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Senior UX Designer - Games Commerce',
          'og:description': "The Twitch Seattle team is seeking a gifted Senior UX Designer to drive user experiences for exciting new opportunities and projects. We offer a series of stimulating problems, an environment that's exciting, motivating, fun, and new. You will have colleagues who will challenge you to achieve more than you thought possible, as well as great camaraderie. Joining our team will give you endless opportunities to use your passion, ingenuity, experience, and pragmatism to build very cool software that affects millions of customers. Our ideal Senior UX Designer will exhibit a strong passion for building top-notch gamer-oriented web and software experiences based on a well-rounded set of design skills that range from wireframes to full fidelity design comps.",
          'og:url': 'https://jobs.lever.co/twitch/0097ec3a-9863-4771-8001-24022b058536',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Procurement Specialist',
    'htmlTitle': 'Twitch - Procurement Specialist',
    'link': 'https://jobs.lever.co/twitch/a0132b95-70e7-46e7-8726-4abdaaac129a',
    'displayLink': 'jobs.lever.co',
    'snippet': 'The Procurement Specialist must have a working understanding of computers (\nboth hardware and software) and a demonstrated willingness to learn and apply\n\xa0...',
    'htmlSnippet': 'The Procurement Specialist must have a working understanding of computers (<br>\nboth hardware and <b>software</b>) and a demonstrated willingness to learn and apply<br>\n&nbsp;...',
    'cacheId': 'NbL3YUZi8FsJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/a0132b95-70e7-46e7-8726-4abdaaac129a',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/a0132b95-70e7-46e7-8726-4abdaaac129a',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Procurement Specialist',
          'twitter:description': "How do we take millions of content creators, connect them with tens of millions of viewers, on a platform that is second to none? It starts with welcoming everyone but choosing only the best. It's the willingness to experiment to decide, and about commitment, not compliance. These are just a few of the driving principles behind the Twitch IT organization. Twitch has an immediate opening for a Procurement Specialist in our San Francisco office. The Procurement Specialist serves as a procurement agent for Twitch IT Services & Customer Success. The IT Procurement Specialist will be responsible for working with Twitch IT to define & implement standards and best practices for procurement, logistics and inventory management in the Twitch environment. Regular activities include inventory management across multiple sites, coordination and planning with IT leads, vendor pricing review and negotiations, regular procurement and inventory reporting to management, placing orders and ensuring",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Procurement Specialist',
          'og:description': "How do we take millions of content creators, connect them with tens of millions of viewers, on a platform that is second to none? It starts with welcoming everyone but choosing only the best. It's the willingness to experiment to decide, and about commitment, not compliance. These are just a few of the driving principles behind the Twitch IT organization. Twitch has an immediate opening for a Procurement Specialist in our San Francisco office. The Procurement Specialist serves as a procurement agent for Twitch IT Services & Customer Success. The IT Procurement Specialist will be responsible for working with Twitch IT to define & implement standards and best practices for procurement, logistics and inventory management in the Twitch environment. Regular activities include inventory management across multiple sites, coordination and planning with IT leads, vendor pricing review and negotiations, regular procurement and inventory reporting to management, placing orders and ensuring",
          'og:url': 'https://jobs.lever.co/twitch/a0132b95-70e7-46e7-8726-4abdaaac129a',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Technical Writer',
    'htmlTitle': 'Twitch - Technical Writer',
    'link': 'https://jobs.lever.co/twitch/f6d721a0-f549-443d-bcbc-51006f911079',
    'displayLink': 'jobs.lever.co',
    'snippet': 'You will collaborate closely with engineers, product managers, and usability \nexperts ... Good foundation in programming, API design, and software \narchitecture\xa0...',
    'htmlSnippet': 'You will collaborate closely with <b>engineers</b>, product managers, and usability <br>\nexperts ... Good foundation in programming, API design, and <b>software</b> <br>\narchitecture&nbsp;...',
    'cacheId': 'H8EfHaxW2XUJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/f6d721a0-f549-443d-bcbc-51006f911079',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/f6d721a0-f549-443d-bcbc-51006f911079',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Technical Writer',
          'twitter:description': 'Twitch is looking for an experienced Technical Writer to produce high-quality documentation which will contribute to the overall success of our products. Most importantly, you should specialize in API documentation and other highly technical deliverables. You will collaborate closely with engineers, product managers, and usability experts in order to enhance our product. \xa0The ideal candidate has excellent communications skills and has a passion for extracting complex systems and concepts into user documentation.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Technical Writer',
          'og:description': 'Twitch is looking for an experienced Technical Writer to produce high-quality documentation which will contribute to the overall success of our products. Most importantly, you should specialize in API documentation and other highly technical deliverables. You will collaborate closely with engineers, product managers, and usability experts in order to enhance our product. \xa0The ideal candidate has excellent communications skills and has a passion for extracting complex systems and concepts into user documentation.',
          'og:url': 'https://jobs.lever.co/twitch/f6d721a0-f549-443d-bcbc-51006f911079',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '512',
          'og:image:width': '1024'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Twitch - Technical Program Manager - Associates',
    'htmlTitle': 'Twitch - Technical Program Manager - Associates',
    'link': 'https://jobs.lever.co/twitch/effc0e76-15be-423c-a836-7fc50dba2913',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Commerce ▒ Games Store Engineering ... Minimum of 4 years of experience as a \ntechnical program manager in software/web development organizations.',
    'htmlSnippet': 'Commerce ▒ Games Store <b>Engineering</b> ... Minimum of 4 years of experience as a <br>\ntechnical program manager in <b>software</b>/web development organizations.',
    'cacheId': '66w9a6EQ6qoJ',
    'formattedUrl': 'https://jobs.lever.co/twitch/effc0e76-15be-423c-a836-7fc50dba2913',
    'htmlFormattedUrl': 'https://jobs.lever.co/twitch/effc0e76-15be-423c-a836-7fc50dba2913',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '258',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Twitch - Technical Program Manager - Associates',
          'twitter:description': 'The Technical Program Management team at Twitch is leading execution of high priority and impactful product initiatives while Twitch is going through hyper growth. TPMs find the right balance between being strategic and tactical to lead cross-functional teams to successfully deliver strategic and complex programs that move the needles for Twitch. We are the glue for the company, and we are playing a key role in scaling the organization.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png',
          'og:title': 'Twitch - Technical Program Manager - Associates',
          'og:description': 'The Technical Program Management team at Twitch is leading execution of high priority and impactful product initiatives while Twitch is going through hyper growth. TPMs find the right balance between being strategic and tactical to lead cross-functional teams to successfully deliver strategic and complex programs that move the needles for Twitch. We are the glue for the company, and we are playing a key role in scaling the organization.',
          'og:url': 'https://jobs.lever.co/twitch/effc0e76-15be-423c-a836-7fc50dba2913',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Everlaw - Software Engineer',
    'htmlTitle': 'Everlaw - <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/everlaw/72e5bdd8-0373-4714-a90e-7aebbb61b181',
    'displayLink': 'jobs.lever.co',
    'snippet': "We care a lot about finding the best engineers, writing correct software, using the \nright tools for the job, and avoiding dogma. As a result we've been able to build\xa0...",
    'htmlSnippet': 'We care a lot about finding the best <b>engineers</b>, writing correct <b>software</b>, using the <br>\nright tools for the job, and avoiding dogma. As a result we&#39;ve been able to build&nbsp;...',
    'cacheId': 're4ece5a_mkJ',
    'formattedUrl': 'https://jobs.lever.co/.../72e5bdd8-0373-4714-a90e-7aebbb61b181',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../72e5bdd8-0373-4714-a90e-7aebbb61b181',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '389',
          'height': '129',
          'src': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTzeNOrZ2dzqly0qqhaN-yRxAorvyxeNv8skGRAm_SAJJb6gLDoQPHC_SE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Everlaw - Software Engineer',
          'twitter:description': "Join a growing, venture-funded startup! You'll be developing core components of our litigation infrastructure, an online platform for lawyers to review, analyze, and collaborate on millions of documents. Tackling litigation with technology is a surprisingly deep challenge, and it requires in-depth computer science, including machine learning, data visualization, search, distributed systems, databases, real-time collaboration, nifty user interfaces, and more. We're looking for full-stack generalists. We value great CS fundamentals, native ability, and humility, over experience with any particular platform, technology, or specialization. If you happen to have a specialty, we'll put that to use -- but we won't restrict you to that area. We care a lot about finding the best engineers, writing correct software, using the right tools for the job, and avoiding dogma. As a result we've been able to build quite a bit of sophisticated technology with a small, talented team. It's the kind",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729581767.png',
          'og:title': 'Everlaw - Software Engineer',
          'og:description': "Join a growing, venture-funded startup! You'll be developing core components of our litigation infrastructure, an online platform for lawyers to review, analyze, and collaborate on millions of documents. Tackling litigation with technology is a surprisingly deep challenge, and it requires in-depth computer science, including machine learning, data visualization, search, distributed systems, databases, real-time collaboration, nifty user interfaces, and more. We're looking for full-stack generalists. We value great CS fundamentals, native ability, and humility, over experience with any particular platform, technology, or specialization. If you happen to have a specialty, we'll put that to use -- but we won't restrict you to that area. We care a lot about finding the best engineers, writing correct software, using the right tools for the job, and avoiding dogma. As a result we've been able to build quite a bit of sophisticated technology with a small, talented team. It's the kind",
          'og:url': 'https://jobs.lever.co/everlaw/72e5bdd8-0373-4714-a90e-7aebbb61b181',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Everlaw - Software Engineer',
    'htmlTitle': 'Everlaw - <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/everlaw/72e5bdd8-0373-4714-a90e-7aebbb61b181/',
    'displayLink': 'jobs.lever.co',
    'snippet': "Please attach a sample (can be an individual file or zip/gzip of multiple files) of \nsome code you've written, along with a README file or comment describing the\xa0...",
    'htmlSnippet': 'Please attach a sample (can be an individual file or zip/gzip of multiple files) of <br>\nsome code you&#39;ve written, along with a README file or comment describing the&nbsp;...',
    'cacheId': 'lyuBw8rNavUJ',
    'formattedUrl': 'https://jobs.lever.co/everlaw/72e5bdd8-0373-4714-a90e.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/everlaw/72e5bdd8-0373-4714-a90e.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '389',
          'height': '129',
          'src': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTzeNOrZ2dzqly0qqhaN-yRxAorvyxeNv8skGRAm_SAJJb6gLDoQPHC_SE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Everlaw - Software Engineer',
          'twitter:description': "Join a growing, venture-funded startup! You'll be developing core components of our litigation infrastructure, an online platform for lawyers to review, analyze, and collaborate on millions of documents. Tackling litigation with technology is a surprisingly deep challenge, and it requires a lot of computer science, including machine learning, data visualization, search, distributed systems, databases, real-time collaboration, nifty user interfaces, and more. We're looking for full-stack generalists. We value great CS fundamentals, native ability, and humility, over experience with any particular platform, technology, or specialization. If you happen to have a specialty, we'll put that to use -- but we won't restrict you to that area. We care a lot about finding the best engineers, writing correct software, using the right tools for the job, and avoiding dogma, and as a result we've been able to build quite a bit of sophisticated technology with a small, talented team. It's the ki",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729581767.png',
          'og:title': 'Everlaw - Software Engineer',
          'og:description': "Join a growing, venture-funded startup! You'll be developing core components of our litigation infrastructure, an online platform for lawyers to review, analyze, and collaborate on millions of documents. Tackling litigation with technology is a surprisingly deep challenge, and it requires a lot of computer science, including machine learning, data visualization, search, distributed systems, databases, real-time collaboration, nifty user interfaces, and more. We're looking for full-stack generalists. We value great CS fundamentals, native ability, and humility, over experience with any particular platform, technology, or specialization. If you happen to have a specialty, we'll put that to use -- but we won't restrict you to that area. We care a lot about finding the best engineers, writing correct software, using the right tools for the job, and avoiding dogma, and as a result we've been able to build quite a bit of sophisticated technology with a small, talented team. It's the ki",
          'og:url': 'https://jobs.lever.co/everlaw/72e5bdd8-0373-4714-a90e-7aebbb61b181/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Everlaw - Lever',
    'htmlTitle': 'Everlaw - Lever',
    'link': 'https://jobs.lever.co/everlaw?team=Engineering',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Berkeley, CAEngineeringFull-time ▒ Apply ▒ Software Engineer. Berkeley, CA\nEngineeringFull-time ▒ Everlaw Home Page ▒ Jobs powered by.',
    'htmlSnippet': 'Berkeley, CAEngineeringFull-time &middot; Apply &middot; <b>Software Engineer</b>. Berkeley, CA<br>\nEngineeringFull-time &middot; Everlaw Home Page &middot; Jobs powered by.',
    'cacheId': 'bWmlYexckt4J',
    'formattedUrl': 'https://jobs.lever.co/everlaw?team=Engineering',
    'htmlFormattedUrl': 'https://jobs.lever.co/everlaw?team=<b>Engineering</b>',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '389',
          'height': '129',
          'src': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTzeNOrZ2dzqly0qqhaN-yRxAorvyxeNv8skGRAm_SAJJb6gLDoQPHC_SE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Everlaw',
          'twitter:description': 'Job openings at Everlaw',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729581767.png',
          'og:title': 'Everlaw jobs',
          'og:description': 'Job openings at Everlaw',
          'og:url': 'https://jobs.lever.co/everlaw',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Everlaw',
    'htmlTitle': 'Everlaw',
    'link': 'https://jobs.lever.co/everlaw',
    'displayLink': 'jobs.lever.co',
    'snippet': 'DevOps/Site Reliability Engineer. Berkeley, CAEngineeringFull-time ▒ Apply ▒ \nSoftware Engineer. Berkeley, CAEngineeringFull-time ▒ Everlaw Home Page.',
    'htmlSnippet': 'DevOps/Site Reliability Engineer. Berkeley, CAEngineeringFull-time &middot; Apply &middot; <br>\n<b>Software Engineer</b>. Berkeley, CAEngineeringFull-time &middot; Everlaw Home Page.',
    'cacheId': 'bik64e5OiYQJ',
    'formattedUrl': 'https://jobs.lever.co/everlaw',
    'htmlFormattedUrl': 'https://jobs.lever.co/everlaw',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '389',
          'height': '129',
          'src': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTzeNOrZ2dzqly0qqhaN-yRxAorvyxeNv8skGRAm_SAJJb6gLDoQPHC_SE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Everlaw',
          'twitter:description': 'Job openings at Everlaw',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729581767.png',
          'og:title': 'Everlaw jobs',
          'og:description': 'Job openings at Everlaw',
          'og:url': 'https://jobs.lever.co/everlaw',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Everlaw - Lever',
    'htmlTitle': 'Everlaw - Lever',
    'link': 'https://jobs.lever.co/everlaw?by=location&commitment=Full-time',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Berkeley, CAAccountsFull-time ▒ Apply ▒ DevOps/Site Reliability Engineer. \nBerkeley, CAEngineeringFull-time ▒ Apply ▒ Software Engineer. Berkeley\xa0...',
    'htmlSnippet': 'Berkeley, CAAccountsFull-time &middot; Apply &middot; DevOps/Site Reliability Engineer. <br>\nBerkeley, CAEngineeringFull-time &middot; Apply &middot; <b>Software Engineer</b>. Berkeley&nbsp;...',
    'cacheId': '3AFdcBYzl5QJ',
    'formattedUrl': 'https://jobs.lever.co/everlaw?by=location&commitment=Full...',
    'htmlFormattedUrl': 'https://jobs.lever.co/everlaw?by=location&amp;commitment=Full...',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '389',
          'height': '129',
          'src': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTzeNOrZ2dzqly0qqhaN-yRxAorvyxeNv8skGRAm_SAJJb6gLDoQPHC_SE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Everlaw',
          'twitter:description': 'Job openings at Everlaw',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729581767.png',
          'og:title': 'Everlaw jobs',
          'og:description': 'Job openings at Everlaw',
          'og:url': 'https://jobs.lever.co/everlaw',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Everlaw',
    'htmlTitle': 'Everlaw',
    'link': 'https://jobs.lever.co/everlaw?by=team&location=Berkeley%2C%20CA&commitment=Full-time',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Berkeley, CABusiness DevelopmentFull-time. Engineering. Apply ▒ Software \nEngineer. Berkeley, CAEngineeringFull-time. User-Facing Operations. Apply\xa0...',
    'htmlSnippet': 'Berkeley, CABusiness DevelopmentFull-time. Engineering. Apply &middot; <b>Software</b> <br>\n<b>Engineer</b>. Berkeley, CAEngineeringFull-time. User-Facing Operations. Apply&nbsp;...',
    'cacheId': 'MgDoJHyJOzAJ',
    'formattedUrl': 'https://jobs.lever.co/everlaw?by=team&location...Full-time',
    'htmlFormattedUrl': 'https://jobs.lever.co/everlaw?by=team&amp;location...Full-time',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '389',
          'height': '129',
          'src': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTzeNOrZ2dzqly0qqhaN-yRxAorvyxeNv8skGRAm_SAJJb6gLDoQPHC_SE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Everlaw',
          'twitter:description': 'Job openings at Everlaw',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729581767.png',
          'og:title': 'Everlaw jobs',
          'og:description': 'Job openings at Everlaw',
          'og:url': 'https://jobs.lever.co/everlaw',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Everlaw - DevOps/Site Reliability Engineer',
    'htmlTitle': 'Everlaw - DevOps/Site Reliability <b>Engineer</b>',
    'link': 'https://jobs.lever.co/everlaw/c5dd0fe3-68a9-4b94-87c6-fa494dd23f82',
    'displayLink': 'jobs.lever.co',
    'snippet': 'To date, our team of a dozen full-stack engineers has been managing this ... We \nhave a history of building reliable software (we have averaged 99.9% uptime\xa0...',
    'htmlSnippet': 'To date, our team of a dozen full-stack <b>engineers</b> has been managing this ... We <br>\nhave a history of building reliable <b>software</b> (we have averaged 99.9% uptime&nbsp;...',
    'cacheId': 'woEhiLcTWiwJ',
    'formattedUrl': 'https://jobs.lever.co/.../c5dd0fe3-68a9-4b94-87c6-fa494dd23f82',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../c5dd0fe3-68a9-4b94-87c6-fa494dd23f82',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '389',
          'height': '129',
          'src': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTzeNOrZ2dzqly0qqhaN-yRxAorvyxeNv8skGRAm_SAJJb6gLDoQPHC_SE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Everlaw - DevOps/Site Reliability Engineer',
          'twitter:description': 'Join a growing, venture-funded startup! We manage dozens of terabytes of data and dozens of AWS Instances across multiple VPCs. Our clients use Everlaw to operate on mission-critical and highly confidential data. To date, our team of a dozen full-stack engineers has been managing this infrastructure. We are looking for someone to own the administration of our architecture as Everlaw grows. We have a history of building reliable software (we have averaged 99.9% uptime since 2014). You▒ll help us keep it that way -- and get even better -- as we expand our offerings and host orders of magnitude more data. You▒ll work closely with our developers and other core team members to improve our processes and automation with respect to the responsibilities listed below.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729581767.png',
          'og:title': 'Everlaw - DevOps/Site Reliability Engineer',
          'og:description': 'Join a growing, venture-funded startup! We manage dozens of terabytes of data and dozens of AWS Instances across multiple VPCs. Our clients use Everlaw to operate on mission-critical and highly confidential data. To date, our team of a dozen full-stack engineers has been managing this infrastructure. We are looking for someone to own the administration of our architecture as Everlaw grows. We have a history of building reliable software (we have averaged 99.9% uptime since 2014). You▒ll help us keep it that way -- and get even better -- as we expand our offerings and host orders of magnitude more data. You▒ll work closely with our developers and other core team members to improve our processes and automation with respect to the responsibilities listed below.',
          'og:url': 'https://jobs.lever.co/everlaw/c5dd0fe3-68a9-4b94-87c6-fa494dd23f82',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Everlaw',
    'htmlTitle': 'Everlaw',
    'link': 'https://jobs.lever.co/everlaw?commitment=Intern',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Team. All ▒ Engineering. Intern. All ▒ Full-time. No job postings match these filters. \nGo back to all job postings ▒ Everlaw Home Page ▒ Jobs powered by.',
    'htmlSnippet': 'Team. All &middot; <b>Engineering</b>. Intern. All &middot; Full-time. No job postings match these filters. <br>\nGo back to all job postings &middot; Everlaw Home Page &middot; Jobs powered by.',
    'cacheId': 'DMfixWGlvoQJ',
    'formattedUrl': 'https://jobs.lever.co/everlaw?commitment=Intern',
    'htmlFormattedUrl': 'https://jobs.lever.co/everlaw?commitment=Intern',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '389',
          'height': '129',
          'src': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTzeNOrZ2dzqly0qqhaN-yRxAorvyxeNv8skGRAm_SAJJb6gLDoQPHC_SE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Everlaw',
          'twitter:description': 'Job openings at Everlaw',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729581767.png',
          'og:title': 'Everlaw jobs',
          'og:description': 'Job openings at Everlaw',
          'og:url': 'https://jobs.lever.co/everlaw',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4fe4ef7e-6b7f-4eed-b3e0-a50513749cec-1485729575263.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Upserve - Software Engineer (Infrastructure)',
    'htmlTitle': 'Upserve - <b>Software Engineer</b> (Infrastructure)',
    'link': 'https://jobs.lever.co/upserve/cd52e901-484c-4fa6-9dae-6fa7cd268d40',
    'displayLink': 'jobs.lever.co',
    'snippet': "Upserve is the industry's leading full-service Restaurant Management Platform. In \na single platform, Upserve offers the market-leading cloud point of sale for\xa0...",
    'htmlSnippet': 'Upserve is the industry&#39;s leading full-service Restaurant Management Platform. In <br>\na single platform, Upserve offers the market-leading cloud point of sale for&nbsp;...',
    'cacheId': 'pjFQazKiq2AJ',
    'formattedUrl': 'https://jobs.lever.co/.../cd52e901-484c-4fa6-9dae-6fa7cd268d40',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../cd52e901-484c-4fa6-9dae-6fa7cd268d40',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '480',
          'height': '105',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQqUh9C3RDscXoRJeXSfKHY95D5rw4caEaiJQKg1z9WxZzTh-qv_CY5xg'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Upserve - Software Engineer (Infrastructure)',
          'twitter:description': "===== About the Role ===== We are seeking a talented Engineer to join our infrastructure team. This group includes some of our top coders, who want to do more and go faster. They are obsessed with automation, and play a critical role improving the tools that keep our products running smoothly. They enable our developers to execute quickly, and strive to maximize product uptime while minimizing developer lag. Our Infrastructure Engineers are also the first line of defense when identifying and diagnosing challenging performance issues, and they play a key role in shaping the direction of Upserve▒s engineering processes. If you're a pragmatic idealist -- you strive for efficient and practical solutions not just theoretically ideal ones, and have a passion for Amazon Web Services (AWS) and operating system internals and databases -- then come join the team! ===== The Right Ingredients ===== Upserve's engineering organization aims to minimize the impacts of Conway▒s law by organizing into",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1499959630563.png',
          'og:title': 'Upserve - Software Engineer (Infrastructure)',
          'og:description': "===== About the Role ===== We are seeking a talented Engineer to join our infrastructure team. This group includes some of our top coders, who want to do more and go faster. They are obsessed with automation, and play a critical role improving the tools that keep our products running smoothly. They enable our developers to execute quickly, and strive to maximize product uptime while minimizing developer lag. Our Infrastructure Engineers are also the first line of defense when identifying and diagnosing challenging performance issues, and they play a key role in shaping the direction of Upserve▒s engineering processes. If you're a pragmatic idealist -- you strive for efficient and practical solutions not just theoretically ideal ones, and have a passion for Amazon Web Services (AWS) and operating system internals and databases -- then come join the team! ===== The Right Ingredients ===== Upserve's engineering organization aims to minimize the impacts of Conway▒s law by organizing into",
          'og:url': 'https://jobs.lever.co/upserve/cd52e901-484c-4fa6-9dae-6fa7cd268d40',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Upserve - Software Engineer',
    'htmlTitle': 'Upserve - <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/upserve/9d4ec303-c93c-412d-b2a2-52c60343eef4',
    'displayLink': 'jobs.lever.co',
    'snippet': "Software Engineer. San Francisco, CA. Engineering. Full-time. Apply for this job. \nUpserve is a restaurant management system that transforms a restaurant's point\xa0...",
    'htmlSnippet': '<b>Software Engineer</b>. San Francisco, CA. Engineering. Full-time. Apply for this job. <br>\nUpserve is a restaurant management system that transforms a restaurant&#39;s point&nbsp;...',
    'cacheId': 'pzgVX6P51UEJ',
    'formattedUrl': 'https://jobs.lever.co/.../9d4ec303-c93c-412d-b2a2-52c60343eef4',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../9d4ec303-c93c-412d-b2a2-52c60343eef4',
    'pagemap': {
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Upserve - Software Engineer',
          'twitter:description': "Upserve is a restaurant management system that transforms a restaurant▒s point of sale into a point of service - offering up pointed and timely guidance on guests, staff, marketing, finances, and even the menu. \xa0Get to know more about our Teams and Culture by checking out our\xa0blog.\xa0  About our Product: - Over the last 6 months, Upserve received NPS scores of +43, +65, +55 +52, +72 +80, higher than any other tech firm selling software to small businesses. - Our business is in hyper growth, doubling since last year, with thousands of restaurant customers relying on Upserve. - Our platform has massive data from which to make decisions: we manage over 11 million meals per month and over 16 million active diners (see our recent press release). - Our LTV to CAC and our SaaS 'Quick Ratio' both exceed 4x - Our newest product feature enjoys 70% weekly active users and nearly 50% daily active users. - Some of the technologies in our stack include React / React Native, Kinesis, DynamoDB, Machine Learning, RedShift,",
          'og:title': 'Upserve - Software Engineer',
          'og:description': "Upserve is a restaurant management system that transforms a restaurant▒s point of sale into a point of service - offering up pointed and timely guidance on guests, staff, marketing, finances, and even the menu. \xa0Get to know more about our Teams and Culture by checking out our\xa0blog.\xa0  About our Product: - Over the last 6 months, Upserve received NPS scores of +43, +65, +55 +52, +72 +80, higher than any other tech firm selling software to small businesses. - Our business is in hyper growth, doubling since last year, with thousands of restaurant customers relying on Upserve. - Our platform has massive data from which to make decisions: we manage over 11 million meals per month and over 16 million active diners (see our recent press release). - Our LTV to CAC and our SaaS 'Quick Ratio' both exceed 4x - Our newest product feature enjoys 70% weekly active users and nearly 50% daily active users. - Some of the technologies in our stack include React / React Native, Kinesis, DynamoDB, Machine Learning, RedShift,",
          'og:url': 'https://jobs.lever.co/upserve/9d4ec303-c93c-412d-b2a2-52c60343eef4',
          'og:image:height': '200'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Upserve - Software Engineer (Infrastructure)',
    'htmlTitle': 'Upserve - <b>Software Engineer</b> (Infrastructure)',
    'link': 'https://jobs.lever.co/upserve/cd52e901-484c-4fa6-9dae-6fa7cd268d40',
    'displayLink': 'jobs.lever.co',
    'snippet': 'U.S. Equal Employment Opportunity information (Completion is voluntary and will \nnot subject you to adverse treatment). Our company values diversity.',
    'htmlSnippet': 'U.S. Equal Employment Opportunity information (Completion is voluntary and will <br>\nnot subject you to adverse treatment). Our company values diversity.',
    'cacheId': 'Vt08fQXdimAJ',
    'formattedUrl': 'https://jobs.lever.co/upserve/cd52e901-484c-4fa6-9dae.../apply?...',
    'htmlFormattedUrl': 'https://jobs.lever.co/upserve/cd52e901-484c-4fa6-9dae.../apply?...',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '480',
          'height': '105',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQqUh9C3RDscXoRJeXSfKHY95D5rw4caEaiJQKg1z9WxZzTh-qv_CY5xg'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Upserve - Software Engineer (Infrastructure)',
          'twitter:description': "===== About the Role ===== We are seeking a talented Engineer to join our infrastructure team. This group includes some of our top coders, who want to do more and go faster. They are obsessed with automation, and play a critical role improving the tools that keep our products running smoothly. They enable our developers to execute quickly, and strive to maximize product uptime while minimizing developer lag. Our Infrastructure Engineers are also the first line of defense when identifying and diagnosing challenging performance issues, and they play a key role in shaping the direction of Upserve▒s engineering processes. If you're a pragmatic idealist -- you strive for efficient and practical solutions not just theoretically ideal ones, and have a passion for Amazon Web Services (AWS) and operating system internals and databases -- then come join the team! ===== The Right Ingredients ===== Upserve's engineering organization aims to minimize the impacts of Conway▒s law by organizing into",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1499959630563.png',
          'og:title': 'Upserve - Software Engineer (Infrastructure)',
          'og:description': "===== About the Role ===== We are seeking a talented Engineer to join our infrastructure team. This group includes some of our top coders, who want to do more and go faster. They are obsessed with automation, and play a critical role improving the tools that keep our products running smoothly. They enable our developers to execute quickly, and strive to maximize product uptime while minimizing developer lag. Our Infrastructure Engineers are also the first line of defense when identifying and diagnosing challenging performance issues, and they play a key role in shaping the direction of Upserve▒s engineering processes. If you're a pragmatic idealist -- you strive for efficient and practical solutions not just theoretically ideal ones, and have a passion for Amazon Web Services (AWS) and operating system internals and databases -- then come join the team! ===== The Right Ingredients ===== Upserve's engineering organization aims to minimize the impacts of Conway▒s law by organizing into",
          'og:url': 'https://jobs.lever.co/upserve/cd52e901-484c-4fa6-9dae-6fa7cd268d40/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Upserve - Software Engineer (Infrastructure)',
    'htmlTitle': 'Upserve - <b>Software Engineer</b> (Infrastructure)',
    'link': 'https://jobs.lever.co/upserve/0a4d4f4c-0de7-4fcf-95e5-b0c7be4e5a5f/',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Software Engineer (Infrastructure). San Francisco, CA. Engineering ... Please \ndescribe your experience with infrastructure engineering for cloud-based web\xa0...',
    'htmlSnippet': '<b>Software Engineer</b> (Infrastructure). San Francisco, CA. Engineering ... Please <br>\ndescribe your experience with infrastructure engineering for cloud-based web&nbsp;...',
    'cacheId': 'i36St1XYnigJ',
    'formattedUrl': 'https://jobs.lever.co/upserve/0a4d4f4c-0de7-4fcf-95e5.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/upserve/0a4d4f4c-0de7-4fcf-95e5.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '480',
          'height': '105',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQqUh9C3RDscXoRJeXSfKHY95D5rw4caEaiJQKg1z9WxZzTh-qv_CY5xg'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Upserve - Software Engineer (Infrastructure)',
          'twitter:description': "Upserve is a restaurant management system that transforms a restaurant▒s point of sale into a point of service- offering up pointed and timely guidance on guests, staff, marketing, finances, and even the menu. Get to know us, and our culture, by checking out careers.upserve.com or our blog. About the Software Engineer role We are seeking a talented Engineer to join our infrastructure team. This group includes some of our top coders, who want to do more and go faster. They are obsessed with automation, and play a critical role improving the tools that keep our products running smoothly. They enable our developers to execute quickly, and strive to maximize product uptime while minimizing developer lag. Our Infrastructure Engineers are also the first line of defense when identifying and diagnosing challenging performance issues, and they play a key role in shaping the direction of Upserve▒s engineering processes. If you're a pragmatic idealist -- you strive for efficient and practical",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1499959630563.png',
          'og:title': 'Upserve - Software Engineer (Infrastructure)',
          'og:description': "Upserve is a restaurant management system that transforms a restaurant▒s point of sale into a point of service- offering up pointed and timely guidance on guests, staff, marketing, finances, and even the menu. Get to know us, and our culture, by checking out careers.upserve.com or our blog. About the Software Engineer role We are seeking a talented Engineer to join our infrastructure team. This group includes some of our top coders, who want to do more and go faster. They are obsessed with automation, and play a critical role improving the tools that keep our products running smoothly. They enable our developers to execute quickly, and strive to maximize product uptime while minimizing developer lag. Our Infrastructure Engineers are also the first line of defense when identifying and diagnosing challenging performance issues, and they play a key role in shaping the direction of Upserve▒s engineering processes. If you're a pragmatic idealist -- you strive for efficient and practical",
          'og:url': 'https://jobs.lever.co/upserve/0a4d4f4c-0de7-4fcf-95e5-b0c7be4e5a5f/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Upserve - Software Engineer (Infrastructure)',
    'htmlTitle': 'Upserve - <b>Software Engineer</b> (Infrastructure)',
    'link': 'https://jobs.lever.co/upserve/c22ee599-0a20-46a7-8982-30f5b64b7858/',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Software Engineer (Infrastructure). New York, NY. Engineering ... Please \ndescribe your experience with infrastructure engineering for cloud-based web \nservices\xa0...',
    'htmlSnippet': '<b>Software Engineer</b> (Infrastructure). New York, NY. Engineering ... Please <br>\ndescribe your experience with infrastructure engineering for cloud-based web <br>\nservices&nbsp;...',
    'cacheId': 'KQMy6U8Mz54J',
    'formattedUrl': 'https://jobs.lever.co/upserve/c22ee599-0a20-46a7-8982.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/upserve/c22ee599-0a20-46a7-8982.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '480',
          'height': '105',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQqUh9C3RDscXoRJeXSfKHY95D5rw4caEaiJQKg1z9WxZzTh-qv_CY5xg'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Upserve - Software Engineer (Infrastructure)',
          'twitter:description': "Upserve is a restaurant management system that transforms a restaurant▒s point of sale into a point of service- offering up pointed and timely guidance on guests, staff, marketing, finances, and even the menu. Get to know us, and our culture, by checking out careers.upserve.com or our blog. About the Software Engineer role We are seeking a talented Engineer to join our infrastructure team. This group includes some of our top coders, who want to do more and go faster. They are obsessed with automation, and play a critical role improving the tools that keep our products running smoothly. They enable our developers to execute quickly, and strive to maximize product uptime while minimizing developer lag. Our Infrastructure Engineers are also the first line of defense when identifying and diagnosing challenging performance issues, and they play a key role in shaping the direction of Upserve▒s engineering processes. If you're a pragmatic idealist -- you strive for efficient and practical",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1499959630563.png',
          'og:title': 'Upserve - Software Engineer (Infrastructure)',
          'og:description': "Upserve is a restaurant management system that transforms a restaurant▒s point of sale into a point of service- offering up pointed and timely guidance on guests, staff, marketing, finances, and even the menu. Get to know us, and our culture, by checking out careers.upserve.com or our blog. About the Software Engineer role We are seeking a talented Engineer to join our infrastructure team. This group includes some of our top coders, who want to do more and go faster. They are obsessed with automation, and play a critical role improving the tools that keep our products running smoothly. They enable our developers to execute quickly, and strive to maximize product uptime while minimizing developer lag. Our Infrastructure Engineers are also the first line of defense when identifying and diagnosing challenging performance issues, and they play a key role in shaping the direction of Upserve▒s engineering processes. If you're a pragmatic idealist -- you strive for efficient and practical",
          'og:url': 'https://jobs.lever.co/upserve/c22ee599-0a20-46a7-8982-30f5b64b7858/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Upserve',
    'htmlTitle': 'Upserve',
    'link': 'https://jobs.lever.co/upserve?by=location&team=Engineering',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Providence, RIEngineeringFull-time ▒ Apply ▒ Software Engineer (Infrastructure). \nProvidence, RIEngineeringFull-time. San Francisco, CA. Apply ▒ Software\xa0...',
    'htmlSnippet': 'Providence, RIEngineeringFull-time &middot; Apply &middot; <b>Software Engineer</b> (Infrastructure). <br>\nProvidence, RIEngineeringFull-time. San Francisco, CA. Apply &middot; Software&nbsp;...',
    'cacheId': 'V4l7ceeVyqUJ',
    'formattedUrl': 'https://jobs.lever.co/upserve?by=location&team=Engineering',
    'htmlFormattedUrl': 'https://jobs.lever.co/upserve?by=location&amp;team=<b>Engineering</b>',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '480',
          'height': '105',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQqUh9C3RDscXoRJeXSfKHY95D5rw4caEaiJQKg1z9WxZzTh-qv_CY5xg'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Upserve',
          'twitter:description': 'Job openings at Upserve',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1499959630563.png',
          'og:title': 'Upserve jobs',
          'og:description': 'Job openings at Upserve',
          'og:url': 'https://jobs.lever.co/upserve',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Upserve',
    'htmlTitle': 'Upserve',
    'link': 'https://jobs.lever.co/upserve',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Javascript Engineer. Providence, RIEngineeringFull-time ▒ Apply ▒ Software \nEngineer (Infrastructure) ... San Francisco, CAEngineeringFull-time. Marketing. \nApply\xa0...',
    'htmlSnippet': 'Javascript Engineer. Providence, RIEngineeringFull-time &middot; Apply &middot; <b>Software</b> <br>\n<b>Engineer</b> (Infrastructure) ... San Francisco, CAEngineeringFull-time. Marketing. <br>\nApply&nbsp;...',
    'cacheId': '1j5pjfPlQrcJ',
    'formattedUrl': 'https://jobs.lever.co/upserve',
    'htmlFormattedUrl': 'https://jobs.lever.co/upserve',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '480',
          'height': '105',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQqUh9C3RDscXoRJeXSfKHY95D5rw4caEaiJQKg1z9WxZzTh-qv_CY5xg'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Upserve',
          'twitter:description': 'Job openings at Upserve',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1499959630563.png',
          'og:title': 'Upserve jobs',
          'og:description': 'Job openings at Upserve',
          'og:url': 'https://jobs.lever.co/upserve',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Upserve',
    'htmlTitle': 'Upserve',
    'link': 'https://jobs.lever.co/upserve?by=location&commitment=Full-time',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Javascript Engineer. Providence, RIEngineeringFull-time ▒ Apply ... Software \nEngineer (Infrastructure). Providence, RIEngineeringFull-time. San Francisco, CA\n.',
    'htmlSnippet': 'Javascript Engineer. Providence, RIEngineeringFull-time &middot; Apply ... <b>Software</b> <br>\n<b>Engineer</b> (Infrastructure). Providence, RIEngineeringFull-time. San Francisco, CA<br>\n.',
    'cacheId': 'B6CWyJOHM7UJ',
    'formattedUrl': 'https://jobs.lever.co/upserve?by=location&commitment=Full...',
    'htmlFormattedUrl': 'https://jobs.lever.co/upserve?by=location&amp;commitment=Full...',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '480',
          'height': '105',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQqUh9C3RDscXoRJeXSfKHY95D5rw4caEaiJQKg1z9WxZzTh-qv_CY5xg'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Upserve',
          'twitter:description': 'Job openings at Upserve',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1499959630563.png',
          'og:title': 'Upserve jobs',
          'og:description': 'Job openings at Upserve',
          'og:url': 'https://jobs.lever.co/upserve',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Upserve',
    'htmlTitle': 'Upserve',
    'link': 'https://jobs.lever.co/upserve?by=commitment',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Javascript Engineer. Providence, RIEngineeringFull-time ▒ Apply ... Software \nEngineer (Infrastructure). Providence, RIEngineeringFull-time ▒ Upserve Home\xa0...',
    'htmlSnippet': 'Javascript Engineer. Providence, RIEngineeringFull-time &middot; Apply ... <b>Software</b> <br>\n<b>Engineer</b> (Infrastructure). Providence, RIEngineeringFull-time &middot; Upserve Home&nbsp;...',
    'cacheId': '8HBgvqOk3J0J',
    'formattedUrl': 'https://jobs.lever.co/upserve?by=commitment',
    'htmlFormattedUrl': 'https://jobs.lever.co/upserve?by=commitment',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '480',
          'height': '105',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQqUh9C3RDscXoRJeXSfKHY95D5rw4caEaiJQKg1z9WxZzTh-qv_CY5xg'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Upserve',
          'twitter:description': 'Job openings at Upserve',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1499959630563.png',
          'og:title': 'Upserve jobs',
          'og:description': 'Job openings at Upserve',
          'og:url': 'https://jobs.lever.co/upserve',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Upserve',
    'htmlTitle': 'Upserve',
    'link': 'https://jobs.lever.co/upserve?by=location&location=San%20Francisco%2C%20CA',
    'displayLink': 'jobs.lever.co',
    'snippet': 'San Francisco, CA. All ▒ Multi Location ▒ Providence, RI ▒ San Francisco, CA. \nTeam. All ▒ Channel ▒ Customer Success ▒ Engineering ▒ Marketing ▒ Revenue\xa0...',
    'htmlSnippet': 'San Francisco, CA. All &middot; Multi Location &middot; Providence, RI &middot; San Francisco, CA. <br>\nTeam. All &middot; Channel &middot; Customer Success &middot; <b>Engineering</b> &middot; Marketing &middot; Revenue&nbsp;...',
    'cacheId': 'iU6YN5aZELwJ',
    'formattedUrl': 'https://jobs.lever.co/upserve?by=location&location...',
    'htmlFormattedUrl': 'https://jobs.lever.co/upserve?by=location&amp;location...',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '480',
          'height': '105',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQqUh9C3RDscXoRJeXSfKHY95D5rw4caEaiJQKg1z9WxZzTh-qv_CY5xg'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Upserve',
          'twitter:description': 'Job openings at Upserve',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1499959630563.png',
          'og:title': 'Upserve jobs',
          'og:description': 'Job openings at Upserve',
          'og:url': 'https://jobs.lever.co/upserve',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Upserve - Javascript Engineer',
    'htmlTitle': 'Upserve - Javascript <b>Engineer</b>',
    'link': 'https://jobs.lever.co/upserve/3784e28b-73b7-4e4f-9077-3ed6dbfa2a1f',
    'displayLink': 'jobs.lever.co',
    'snippet': "As a JavaScript Engineer, you'll play a pivotal role in architecting, expanding, and \n... over the last six months are higher than any other SMB software company.",
    'htmlSnippet': 'As a JavaScript <b>Engineer</b>, you&#39;ll play a pivotal role in architecting, expanding, and <br>\n... over the last six months are higher than any other SMB <b>software</b> company.',
    'cacheId': 'MBym_uLb_ocJ',
    'formattedUrl': 'https://jobs.lever.co/.../3784e28b-73b7-4e4f-9077-3ed6dbfa2a1f',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../3784e28b-73b7-4e4f-9077-3ed6dbfa2a1f',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '480',
          'height': '105',
          'src': 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQqUh9C3RDscXoRJeXSfKHY95D5rw4caEaiJQKg1z9WxZzTh-qv_CY5xg'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Upserve - Javascript Engineer',
          'twitter:description': "===== About the Role ===== As a JavaScript Engineer, you▒ll play a pivotal role in architecting, expanding, and evolving unified experiences across our products. You'll work alongside senior engineers and product managers in a small, focused team, as part of a geographically dispersed, product-centric and agile environment. Day to day, this means: - Collaborating with our product and UX team to develop interfaces and clarify product requirements. - Balancing issue and bug resolution, platform improvements and new feature builds. - Contributing to and informally mentoring other engineers by contributing to PR feedback. ===== The Right Ingredients ===== For this role, you have to be passionate about frequently shipping intuitive, quality products to large numbers of end users. You also need a keen eye for design and thoughtful user experiences - all with an eye towards both online and offline operations. Lastly, you need strong debugging skills to support full lifecycle product o",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1499959630563.png',
          'og:title': 'Upserve - Javascript Engineer',
          'og:description': "===== About the Role ===== As a JavaScript Engineer, you▒ll play a pivotal role in architecting, expanding, and evolving unified experiences across our products. You'll work alongside senior engineers and product managers in a small, focused team, as part of a geographically dispersed, product-centric and agile environment. Day to day, this means: - Collaborating with our product and UX team to develop interfaces and clarify product requirements. - Balancing issue and bug resolution, platform improvements and new feature builds. - Contributing to and informally mentoring other engineers by contributing to PR feedback. ===== The Right Ingredients ===== For this role, you have to be passionate about frequently shipping intuitive, quality products to large numbers of end users. You also need a keen eye for design and thoughtful user experiences - all with an eye towards both online and offline operations. Lastly, you need strong debugging skills to support full lifecycle product o",
          'og:url': 'https://jobs.lever.co/upserve/3784e28b-73b7-4e4f-9077-3ed6dbfa2a1f',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/58a3b574-4618-40e1-a1ce-15dfb529de71-1500051197088.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Software Engineer *',
    'htmlTitle': 'Credit Karma - <b>Software Engineer</b> *',
    'link': 'https://jobs.lever.co/creditkarma/07b20074-9bdf-4aca-9b38-f051fe1f14cf',
    'displayLink': 'jobs.lever.co',
    'snippet': "Credit Karma's mission is to make financial progress possible for everyone. We \nhave over 60 million US members and are a true mission-oriented business,\xa0...",
    'htmlSnippet': 'Credit Karma&#39;s mission is to make financial progress possible for everyone. We <br>\nhave over 60 million US members and are a true mission-oriented business,&nbsp;...',
    'cacheId': 'XFUzzKlV58YJ',
    'formattedUrl': 'https://jobs.lever.co/.../07b20074-9bdf-4aca-9b38-f051fe1f14cf',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../07b20074-9bdf-4aca-9b38-f051fe1f14cf',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Software Engineer *',
          'twitter:description': "Credit Karma's mission is to make financial progress possible for everyone. We have over 60 million US members and are a true mission-oriented business, a rare case where our incentives are aligned with our users - we succeed by helping our members. If you're motivated by growth and impact, Credit Karma is one of the best places to work in tech today. We are growing our product beyond credit scores (e.g. Credit Karma Tax) and are well-positioned to become the main touchpoint for consumer finance, but there is so much work left to do! Engineers joining now have tons of opportunities to take on responsibility and ownership and have a meaningful impact. We embrace a culture where engineers are encouraged to identify opportunities to scale the product, technology, and organization, and then launch them into action. See some of our stories at engineering.creditkarma.com. As a software engineer, you will be able to contribute to a wide variety of projects that power our business and help o",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - Software Engineer *',
          'og:description': "Credit Karma's mission is to make financial progress possible for everyone. We have over 60 million US members and are a true mission-oriented business, a rare case where our incentives are aligned with our users - we succeed by helping our members. If you're motivated by growth and impact, Credit Karma is one of the best places to work in tech today. We are growing our product beyond credit scores (e.g. Credit Karma Tax) and are well-positioned to become the main touchpoint for consumer finance, but there is so much work left to do! Engineers joining now have tons of opportunities to take on responsibility and ownership and have a meaningful impact. We embrace a culture where engineers are encouraged to identify opportunities to scale the product, technology, and organization, and then launch them into action. See some of our stories at engineering.creditkarma.com. As a software engineer, you will be able to contribute to a wide variety of projects that power our business and help o",
          'og:url': 'https://jobs.lever.co/creditkarma/07b20074-9bdf-4aca-9b38-f051fe1f14cf',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Software Engineer: Charlotte, NC',
    'htmlTitle': 'Credit Karma - <b>Software Engineer</b>: Charlotte, NC',
    'link': 'https://jobs.lever.co/creditkarma/92153ce9-445f-4ecc-a814-a4dafd5c80e4',
    'displayLink': 'jobs.lever.co',
    'snippet': "As a Software Engineer, you'll be a member of a small cross-functional Scrum \nteam and get involved in every aspect of the product development cycle. You'll\xa0...",
    'htmlSnippet': 'As a <b>Software Engineer</b>, you&#39;ll be a member of a small cross-functional Scrum <br>\nteam and get involved in every aspect of the product development cycle. You&#39;ll&nbsp;...',
    'cacheId': 'cXiV7tq_WVoJ',
    'formattedUrl': 'https://jobs.lever.co/.../92153ce9-445f-4ecc-a814-a4dafd5c80e4',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../92153ce9-445f-4ecc-a814-a4dafd5c80e4',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Software Engineer: Charlotte, NC',
          'twitter:description': "As a Software Engineer, you▒ll be a member of a small cross-functional Scrum team and get involved in every aspect of the product development cycle. You▒ll work closely with a Product Manager and be in charge of the development of your product features--you'll figure out how they should be architected, design the DB schema, write the code, write the unit tests, and make sure that loose ends are tied up. We are a growing Engineering team, yet we offer a great deal of autonomy and flexibility. If you're a person who enjoys working with a lot of freedom, but knows how to take full ownership of a project and meet deadlines with quality, then this is the role for you.",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - Software Engineer: Charlotte, NC',
          'og:description': "As a Software Engineer, you▒ll be a member of a small cross-functional Scrum team and get involved in every aspect of the product development cycle. You▒ll work closely with a Product Manager and be in charge of the development of your product features--you'll figure out how they should be architected, design the DB schema, write the code, write the unit tests, and make sure that loose ends are tied up. We are a growing Engineering team, yet we offer a great deal of autonomy and flexibility. If you're a person who enjoys working with a lot of freedom, but knows how to take full ownership of a project and meet deadlines with quality, then this is the role for you.",
          'og:url': 'https://jobs.lever.co/creditkarma/92153ce9-445f-4ecc-a814-a4dafd5c80e4',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Software Engineer, Infrastructure Services',
    'htmlTitle': 'Credit Karma - <b>Software Engineer</b>, Infrastructure Services',
    'link': 'https://jobs.lever.co/creditkarma/13af1b42-9ec0-47c6-8417-673a5b6bee19',
    'displayLink': 'jobs.lever.co',
    'snippet': "Software engineers on our Infrastructure Services team have a responsibility \nthat's simply-stated but extremely challenging: provide our large (and growing)\xa0...",
    'htmlSnippet': '<b>Software engineers</b> on our Infrastructure Services team have a responsibility <br>\nthat&#39;s simply-stated but extremely challenging: provide our large (and growing)&nbsp;...',
    'cacheId': 'wrTy08h7QRcJ',
    'formattedUrl': 'https://jobs.lever.co/.../13af1b42-9ec0-47c6-8417-673a5b6bee19',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../13af1b42-9ec0-47c6-8417-673a5b6bee19',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Software Engineer, Infrastructure Services',
          'twitter:description': "Software engineers on our Infrastructure Services team have a responsibility that's simply-stated but extremely challenging: provide our large (and growing) engineering organization with Platform-as-a-Service offerings that allow them to be self-sufficient, productive, and focus on business impact. On this team you'll strive to give developers building services complete ownership of their code from development through testing to production by ensuring they have the visibility and tools needed to make effective, continual change. You will build and integrate tools that enable teams to work with containers at-will and at-scale. Your efforts will enable rapid iteration and self-management of services for all of Credit Karma's engineers. Your days will be heavily collaborative with our Operations and Engineering teams to understand and deliver on their needs. If you want to be part of a small and impactful team, enjoy collaborating, thrive on building and maintaining highly-scalable criti",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - Software Engineer, Infrastructure Services',
          'og:description': "Software engineers on our Infrastructure Services team have a responsibility that's simply-stated but extremely challenging: provide our large (and growing) engineering organization with Platform-as-a-Service offerings that allow them to be self-sufficient, productive, and focus on business impact. On this team you'll strive to give developers building services complete ownership of their code from development through testing to production by ensuring they have the visibility and tools needed to make effective, continual change. You will build and integrate tools that enable teams to work with containers at-will and at-scale. Your efforts will enable rapid iteration and self-management of services for all of Credit Karma's engineers. Your days will be heavily collaborative with our Operations and Engineering teams to understand and deliver on their needs. If you want to be part of a small and impactful team, enjoy collaborating, thrive on building and maintaining highly-scalable criti",
          'og:url': 'https://jobs.lever.co/creditkarma/13af1b42-9ec0-47c6-8417-673a5b6bee19',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Node.js Software Engineer',
    'htmlTitle': 'Credit Karma - Node.js <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/creditkarma/80a2b884-ff6c-4f87-a3b1-a142d12647b2',
    'displayLink': 'jobs.lever.co',
    'snippet': 'We are looking for a senior Node.js software engineer to help lead the design \nand evolution of our GraphQL API gateway, which will eventually handle all\xa0...',
    'htmlSnippet': 'We are looking for a senior Node.js <b>software engineer</b> to help lead the design <br>\nand evolution of our GraphQL API gateway, which will eventually handle all&nbsp;...',
    'cacheId': '4j17LUp8-NIJ',
    'formattedUrl': 'https://jobs.lever.co/.../80a2b884-ff6c-4f87-a3b1-a142d12647b2',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../80a2b884-ff6c-4f87-a3b1-a142d12647b2',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Node.js Software Engineer',
          'twitter:description': 'Credit Karma▒s Client Infrastructure team is responsible for building the frameworks and platforms that application engineers leverage to quickly connect different systems to deliver new features and products for our customers. We are looking for a senior Node.js software engineer to help lead the design and evolution of our GraphQL API gateway, which will eventually handle all asynchronous data requests across all of our clients. Responsibilities include designing systems for high throughput and availability, collaborating with other engineers and teams, leading software and system design discussions, delivering high quality, well-tested software, and supporting 24/7/365 site operations of critical components of our infrastructure. Our ideal candidate is self-aware, has strong interpersonal skills, enjoys mentoring other engineers, and has experience designing and supporting high-traffic Node.js applications in production, diagnosing and addressing critical production issues, and',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - Node.js Software Engineer',
          'og:description': 'Credit Karma▒s Client Infrastructure team is responsible for building the frameworks and platforms that application engineers leverage to quickly connect different systems to deliver new features and products for our customers. We are looking for a senior Node.js software engineer to help lead the design and evolution of our GraphQL API gateway, which will eventually handle all asynchronous data requests across all of our clients. Responsibilities include designing systems for high throughput and availability, collaborating with other engineers and teams, leading software and system design discussions, delivering high quality, well-tested software, and supporting 24/7/365 site operations of critical components of our infrastructure. Our ideal candidate is self-aware, has strong interpersonal skills, enjoys mentoring other engineers, and has experience designing and supporting high-traffic Node.js applications in production, diagnosing and addressing critical production issues, and',
          'og:url': 'https://jobs.lever.co/creditkarma/80a2b884-ff6c-4f87-a3b1-a142d12647b2',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Software Engineer: Charlotte,NC',
    'htmlTitle': 'Credit Karma - <b>Software Engineer</b>: Charlotte,NC',
    'link': 'https://jobs.lever.co/creditkarma/b3dadddd-a037-4216-baa3-03bb13be0101',
    'displayLink': 'jobs.lever.co',
    'snippet': "Credit Karma's mission is to make financial progress possible for everyone. We \nhave over 60 million US members and are a true mission-oriented business,\xa0...",
    'htmlSnippet': 'Credit Karma&#39;s mission is to make financial progress possible for everyone. We <br>\nhave over 60 million US members and are a true mission-oriented business,&nbsp;...',
    'cacheId': 'p2zp2dJ0tHsJ',
    'formattedUrl': 'https://jobs.lever.co/.../b3dadddd-a037-4216-baa3-03bb13be0101',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../b3dadddd-a037-4216-baa3-03bb13be0101',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Software Engineer: Charlotte,NC',
          'twitter:description': "Credit Karma's mission is to make financial progress possible for everyone. We have over 60 million US members and are a true mission-oriented business, a rare case where our incentives are aligned with our users ▒ we succeed by helping our members. If you're motivated by growth and impact, Credit Karma is one of the best places to work in tech today. We are growing our product beyond credit scores (e.g. Credit Karma Tax) and are well-positioned to become the main touchpoint for consumer finance, but there is so much work left to do! Engineers joining now have tons of opportunities to take on responsibility and ownership and have a meaningful impact. We embrace a culture where engineers are encouraged to identify opportunities to scale the product, technology, and organization, and then launch them into action. See some of our stories at engineering.creditkarma.com. As a software engineer, you will contribute to a wide variety of projects that power our business and help deliver valu",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - Software Engineer: Charlotte,NC',
          'og:description': "Credit Karma's mission is to make financial progress possible for everyone. We have over 60 million US members and are a true mission-oriented business, a rare case where our incentives are aligned with our users ▒ we succeed by helping our members. If you're motivated by growth and impact, Credit Karma is one of the best places to work in tech today. We are growing our product beyond credit scores (e.g. Credit Karma Tax) and are well-positioned to become the main touchpoint for consumer finance, but there is so much work left to do! Engineers joining now have tons of opportunities to take on responsibility and ownership and have a meaningful impact. We embrace a culture where engineers are encouraged to identify opportunities to scale the product, technology, and organization, and then launch them into action. See some of our stories at engineering.creditkarma.com. As a software engineer, you will contribute to a wide variety of projects that power our business and help deliver valu",
          'og:url': 'https://jobs.lever.co/creditkarma/b3dadddd-a037-4216-baa3-03bb13be0101',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Security Software Engineer: Charlotte, NC',
    'htmlTitle': 'Credit Karma - Security <b>Software Engineer</b>: Charlotte, NC',
    'link': 'https://jobs.lever.co/creditkarma/e3124671-6634-499f-886d-de61a50f8aae',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Your unique mission as a Software Security Engineer is to identify potential \nweaknesses in the foundational infrastructure and strategically reinforce them,\xa0...',
    'htmlSnippet': 'Your unique mission as a <b>Software</b> Security <b>Engineer</b> is to identify potential <br>\nweaknesses in the foundational infrastructure and strategically reinforce them,&nbsp;...',
    'cacheId': '4LxXx-gewi0J',
    'formattedUrl': 'https://jobs.lever.co/.../e3124671-6634-499f-886d-de61a50f8aae',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../e3124671-6634-499f-886d-de61a50f8aae',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Security Software Engineer: Charlotte, NC',
          'twitter:description': 'Security is a core value at Credit Karma. We help millions of people better manage their credit. Safeguarding their sensitive information is critical to our continued success. From the CEO down to each individual developer, everyone views security as a personal responsibility. Your unique mission as a Software Security Engineer is to identify potential weaknesses in the foundational infrastructure and strategically reinforce them, enabling the engineering team to focus fiercely on new features.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - Security Software Engineer: Charlotte, NC',
          'og:description': 'Security is a core value at Credit Karma. We help millions of people better manage their credit. Safeguarding their sensitive information is critical to our continued success. From the CEO down to each individual developer, everyone views security as a personal responsibility. Your unique mission as a Software Security Engineer is to identify potential weaknesses in the foundational infrastructure and strategically reinforce them, enabling the engineering team to focus fiercely on new features.',
          'og:url': 'https://jobs.lever.co/creditkarma/e3124671-6634-499f-886d-de61a50f8aae',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Senior Software Engineer, Deployment Efficiency',
    'htmlTitle': 'Credit Karma - Senior <b>Software Engineer</b>, Deployment Efficiency',
    'link': 'https://jobs.lever.co/creditkarma/5818b9c4-d9e5-4d9f-9ee7-ea84a5630ea9',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Senior Software Engineer, Deployment Efficiency. San Francisco, CA. \nEngineering. Full-time. Apply for this job. Your objective is simply stated but \nextremely\xa0...',
    'htmlSnippet': 'Senior <b>Software Engineer</b>, Deployment Efficiency. San Francisco, CA. <br>\nEngineering. Full-time. Apply for this job. Your objective is simply stated but <br>\nextremely&nbsp;...',
    'cacheId': 'ysPiK90trOkJ',
    'formattedUrl': 'https://jobs.lever.co/.../5818b9c4-d9e5-4d9f-9ee7-ea84a5630ea9',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../5818b9c4-d9e5-4d9f-9ee7-ea84a5630ea9',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '541',
          'height': '93',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTJ_MyGMTa8ldvbcBh0lOtkD3-vsqEO5B4sA6C7RMGhgw24lCLt-OQk5Q'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Senior Software Engineer, Deployment Efficiency',
          'twitter:description': 'Your objective is simply stated but extremely challenging: provide our engineering staff with Platform-as-a-Service offerings that allow them to be self-sufficient, productive, and focus on business impact. \xa0You will work with development teams to get code, tools, and policies in place to quickly, efficiently, and securely deploy their work. \xa0You will give teams complete ownership of their code, all the way into production; ensuring they have the visibility and tools needed to make effective, continual change. \xa0The deployment efficiency team plays a central role with high impact and visibility across all of engineering. \xa0Your days will be heavily collaborative with our operations and development teams to understand and deliver on their needs. \xa0If you want to be part of a small but impactful team, enjoy collaboration, thrive on building and maintaining highly-scalable critical systems, and have passion and tenacity for tackling complex problems, this is a great opportunity!',
          'og:title': 'Credit Karma - Senior Software Engineer, Deployment Efficiency',
          'og:description': 'Your objective is simply stated but extremely challenging: provide our engineering staff with Platform-as-a-Service offerings that allow them to be self-sufficient, productive, and focus on business impact. \xa0You will work with development teams to get code, tools, and policies in place to quickly, efficiently, and securely deploy their work. \xa0You will give teams complete ownership of their code, all the way into production; ensuring they have the visibility and tools needed to make effective, continual change. \xa0The deployment efficiency team plays a central role with high impact and visibility across all of engineering. \xa0Your days will be heavily collaborative with our operations and development teams to understand and deliver on their needs. \xa0If you want to be part of a small but impactful team, enjoy collaboration, thrive on building and maintaining highly-scalable critical systems, and have passion and tenacity for tackling complex problems, this is a great opportunity!',
          'og:url': 'https://jobs.lever.co/creditkarma/5818b9c4-d9e5-4d9f-9ee7-ea84a5630ea9',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1450394750591.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1450394750591.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Software Engineer: Charlotte, NC',
    'htmlTitle': 'Credit Karma - <b>Software Engineer</b>: Charlotte, NC',
    'link': 'https://jobs.lever.co/creditkarma/c718f478-bbb8-46ed-a6ef-d655bb5cb856/',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Self-identification of veteran status (Completion is voluntary and will not subject \nyou to adverse treatment). Credit Karma is a Government contractor subject to\xa0...',
    'htmlSnippet': 'Self-identification of veteran status (Completion is voluntary and will not subject <br>\nyou to adverse treatment). Credit Karma is a Government contractor subject to&nbsp;...',
    'cacheId': 'heYzBitTgE0J',
    'formattedUrl': 'https://jobs.lever.co/creditkarma/c718f478-bbb8-46ed-a6ef.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/creditkarma/c718f478-bbb8-46ed-a6ef.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Software Engineer: Charlotte, NC',
          'twitter:description': "As a Software Engineer, you▒ll be a member of a small cross-functional Scrum team and get involved in every aspect of the product development cycle. You▒ll work closely with a Product Manager and be in charge of the development of your product features--you'll figure out how they should be architected, design the DB schema, write the code, write the unit tests, and make sure that loose ends are tied up. We are a growing Engineering team, yet we offer a great deal of autonomy and flexibility. If you're a person who enjoys working with a lot of freedom, but knows how to take full ownership of a project and meet deadlines with quality, then this is the role for you.",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - Software Engineer: Charlotte, NC',
          'og:description': "As a Software Engineer, you▒ll be a member of a small cross-functional Scrum team and get involved in every aspect of the product development cycle. You▒ll work closely with a Product Manager and be in charge of the development of your product features--you'll figure out how they should be architected, design the DB schema, write the code, write the unit tests, and make sure that loose ends are tied up. We are a growing Engineering team, yet we offer a great deal of autonomy and flexibility. If you're a person who enjoys working with a lot of freedom, but knows how to take full ownership of a project and meet deadlines with quality, then this is the role for you.",
          'og:url': 'https://jobs.lever.co/creditkarma/c718f478-bbb8-46ed-a6ef-d655bb5cb856/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Software Engineer in Testing: Charlotte, NC',
    'htmlTitle': 'Credit Karma - <b>Software Engineer</b> in Testing: Charlotte, NC',
    'link': 'https://jobs.lever.co/creditkarma/5d743ad2-d74b-4727-ab61-9a20a9561c78/',
    'displayLink': 'jobs.lever.co',
    'snippet': 'U.S. Equal Employment Opportunity information (Completion is voluntary and will \nnot subject you to adverse treatment). Credit Karma provides equal\xa0...',
    'htmlSnippet': 'U.S. Equal Employment Opportunity information (Completion is voluntary and will <br>\nnot subject you to adverse treatment). Credit Karma provides equal&nbsp;...',
    'cacheId': '9jaziMVesJcJ',
    'formattedUrl': 'https://jobs.lever.co/creditkarma/5d743ad2-d74b-4727.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/creditkarma/5d743ad2-d74b-4727.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Software Engineer in Testing: Charlotte, NC',
          'twitter:description': "Credit Karma is looking for a quick-thinking quality enthusiast who understands releasing great software is not just about reactive testing. As a QA engineer at Credit Karma you'll be assessing and mitigating risks for our iOS, Android and Web releases. Solving quality challenges, performing exploratory testing, training and coaching software engineers in the art of quality testing and improving development processes, all as part of a team of highly talented and supportive QA engineers.",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - Software Engineer in Testing: Charlotte, NC',
          'og:description': "Credit Karma is looking for a quick-thinking quality enthusiast who understands releasing great software is not just about reactive testing. As a QA engineer at Credit Karma you'll be assessing and mitigating risks for our iOS, Android and Web releases. Solving quality challenges, performing exploratory testing, training and coaching software engineers in the art of quality testing and improving development processes, all as part of a team of highly talented and supportive QA engineers.",
          'og:url': 'https://jobs.lever.co/creditkarma/5d743ad2-d74b-4727-ab61-9a20a9561c78/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Senior Software Engineer, Deployment Efficiency',
    'htmlTitle': 'Credit Karma - Senior <b>Software Engineer</b>, Deployment Efficiency',
    'link': 'https://jobs.lever.co/creditkarma/5818b9c4-d9e5-4d9f-9ee7-ea84a5630ea9/',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Our company values diversity. To ensure that we comply with reporting \nrequirements and to learn more about how we can increase diversity in our \ncandidate\xa0...',
    'htmlSnippet': 'Our company values diversity. To ensure that we comply with reporting <br>\nrequirements and to learn more about how we can increase diversity in our <br>\ncandidate&nbsp;...',
    'cacheId': 'gYHFNBGby9gJ',
    'formattedUrl': 'https://jobs.lever.co/creditkarma/5818b9c4-d9e5-4d9f.../apply?...',
    'htmlFormattedUrl': 'https://jobs.lever.co/creditkarma/5818b9c4-d9e5-4d9f.../apply?...',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '585',
          'height': '86',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS1_m0_0Y4oWVrIZjLciIG2Nnp4HqeXTFT30q8mY9JaEZkk_WCZyFlsfw'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Senior Software Engineer, Deployment Efficiency',
          'twitter:description': 'Your objective is simply stated but extremely challenging: provide our engineering staff with Platform-as-a-Service offerings that allow them to be self-sufficient, productive, and focus on business impact. \xa0You will work with development teams to get code, tools, and policies in place to quickly, efficiently, and securely deploy their work. \xa0You will give teams complete ownership of their code, all the way into production; ensuring they have the visibility and tools needed to make effective, continual change. \xa0The deployment efficiency team plays a central role with high impact and visibility across all of engineering. \xa0Your days will be heavily collaborative with our operations and development teams to understand and deliver on their needs. \xa0If you want to be part of a small but impactful team, enjoy collaboration, thrive on building and maintaining highly-scalable critical systems, and have passion and tenacity for tackling complex problems, this is a great opportunity!',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - Senior Software Engineer, Deployment Efficiency',
          'og:description': 'Your objective is simply stated but extremely challenging: provide our engineering staff with Platform-as-a-Service offerings that allow them to be self-sufficient, productive, and focus on business impact. \xa0You will work with development teams to get code, tools, and policies in place to quickly, efficiently, and securely deploy their work. \xa0You will give teams complete ownership of their code, all the way into production; ensuring they have the visibility and tools needed to make effective, continual change. \xa0The deployment efficiency team plays a central role with high impact and visibility across all of engineering. \xa0Your days will be heavily collaborative with our operations and development teams to understand and deliver on their needs. \xa0If you want to be part of a small but impactful team, enjoy collaboration, thrive on building and maintaining highly-scalable critical systems, and have passion and tenacity for tackling complex problems, this is a great opportunity!',
          'og:url': 'https://jobs.lever.co/creditkarma/5818b9c4-d9e5-4d9f-9ee7-ea84a5630ea9/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481138372169.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481138372169.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Full-Stack QA Engineer: San Francisco, CA',
    'htmlTitle': 'Credit Karma - Full-Stack QA <b>Engineer</b>: San Francisco, CA',
    'link': 'https://jobs.lever.co/creditkarma/66290e6f-aec6-4a8b-ae93-d0b9b876475a',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Credit Karma is looking for a quick-thinking, quality enthusiast who understands \nreleasing great software is not just about reactive testing. As a QA Engineer at\xa0...',
    'htmlSnippet': 'Credit Karma is looking for a quick-thinking, quality enthusiast who understands <br>\nreleasing great <b>software</b> is not just about reactive testing. As a QA <b>Engineer</b> at&nbsp;...',
    'cacheId': 'ku9z2amkxO0J',
    'formattedUrl': 'https://jobs.lever.co/.../66290e6f-aec6-4a8b-ae93-d0b9b876475a',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../66290e6f-aec6-4a8b-ae93-d0b9b876475a',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Full-Stack QA Engineer: San Francisco, CA',
          'twitter:description': 'Credit Karma is looking for a quick-thinking, quality enthusiast who understands releasing great software is not just about reactive testing. As a QA Engineer at Credit Karma▒s you▒ll be proactively assessing and mitigating risks for our Web, Native and Service platform releases, within one of our exciting product verticals. You▒ll be solving big quality challenges, coaching Software Engineers and Product Managers in the art of quality testing and helping to create a long term vision of quality features for our members. You are a passionate member of the team who wants to have high impact; looking for a hands-on technical career with both manual and automated testing. This isn▒t just about ▒Quality Assurance▒; we want you to help us create a better product and proactively improve our quality efforts on the whole.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - Full-Stack QA Engineer: San Francisco, CA',
          'og:description': 'Credit Karma is looking for a quick-thinking, quality enthusiast who understands releasing great software is not just about reactive testing. As a QA Engineer at Credit Karma▒s you▒ll be proactively assessing and mitigating risks for our Web, Native and Service platform releases, within one of our exciting product verticals. You▒ll be solving big quality challenges, coaching Software Engineers and Product Managers in the art of quality testing and helping to create a long term vision of quality features for our members. You are a passionate member of the team who wants to have high impact; looking for a hands-on technical career with both manual and automated testing. This isn▒t just about ▒Quality Assurance▒; we want you to help us create a better product and proactively improve our quality efforts on the whole.',
          'og:url': 'https://jobs.lever.co/creditkarma/66290e6f-aec6-4a8b-ae93-d0b9b876475a',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma',
    'htmlTitle': 'Credit Karma',
    'link': 'https://jobs.lever.co/creditkarma',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Node.js Software Engineer. San Francisco ... Security Software Engineer: \nCharlotte, NC. Charlotte ... Software Engineer, Infrastructure Services. San \nFrancisco\xa0...',
    'htmlSnippet': 'Node.js <b>Software Engineer</b>. San Francisco ... Security <b>Software Engineer</b>: <br>\nCharlotte, NC. Charlotte ... <b>Software Engineer</b>, Infrastructure Services. San <br>\nFrancisco&nbsp;...',
    'cacheId': 'zhIXo5SSm2gJ',
    'formattedUrl': 'https://jobs.lever.co/creditkarma',
    'htmlFormattedUrl': 'https://jobs.lever.co/creditkarma',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma',
          'twitter:description': 'Job openings at Credit Karma',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma jobs',
          'og:description': 'Job openings at Credit Karma',
          'og:url': 'https://jobs.lever.co/creditkarma',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Full-Stack Engineer *',
    'htmlTitle': 'Credit Karma - Full-Stack <b>Engineer</b> *',
    'link': 'https://jobs.lever.co/creditkarma/19d67124-196b-4f83-ab17-f0a179d327c7',
    'displayLink': 'jobs.lever.co',
    'snippet': 'As a full-stack software engineer, you will contribute to a wide variety of projects \nthat power our business and help deliver value to our members. We have a wide\n\xa0...',
    'htmlSnippet': 'As a full-stack <b>software engineer</b>, you will contribute to a wide variety of projects <br>\nthat power our business and help deliver value to our members. We have a wide<br>\n&nbsp;...',
    'cacheId': 'vZoxMrqQSd4J',
    'formattedUrl': 'https://jobs.lever.co/.../19d67124-196b-4f83-ab17-f0a179d327c7',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../19d67124-196b-4f83-ab17-f0a179d327c7',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Full-Stack Engineer *',
          'twitter:description': "Credit Karma's mission is to make financial progress possible for everyone. We have over 60 million US members and are a true mission-oriented business, a rare case where our incentives are aligned with our users ▒ we succeed by helping our members. If you're motivated by growth and impact, Credit Karma is one of the best places to work in tech today. We are growing our product beyond credit scores (e.g. Credit Karma Tax) and are well-positioned to become the main touchpoint for consumer finance, but there is so much work left to do! Engineers joining now have tons of opportunities to take on responsibility and ownership and have a meaningful impact. We embrace a culture where engineers are encouraged to identify opportunities to scale the product, technology, and organization, and then launch them into action. See some of our stories at engineering.creditkarma.com. As a full-stack software engineer, you will contribute to a wide variety of projects that power our business and help d",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - Full-Stack Engineer *',
          'og:description': "Credit Karma's mission is to make financial progress possible for everyone. We have over 60 million US members and are a true mission-oriented business, a rare case where our incentives are aligned with our users ▒ we succeed by helping our members. If you're motivated by growth and impact, Credit Karma is one of the best places to work in tech today. We are growing our product beyond credit scores (e.g. Credit Karma Tax) and are well-positioned to become the main touchpoint for consumer finance, but there is so much work left to do! Engineers joining now have tons of opportunities to take on responsibility and ownership and have a meaningful impact. We embrace a culture where engineers are encouraged to identify opportunities to scale the product, technology, and organization, and then launch them into action. See some of our stories at engineering.creditkarma.com. As a full-stack software engineer, you will contribute to a wide variety of projects that power our business and help d",
          'og:url': 'https://jobs.lever.co/creditkarma/19d67124-196b-4f83-ab17-f0a179d327c7',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma',
    'htmlTitle': 'Credit Karma',
    'link': 'https://jobs.lever.co/creditkarma?by=commitment',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Android Engineer *. San Francisco, CAEngineeringFull-time ▒ Apply ... Security \nSoftware Engineer: Charlotte, NC. Charlotte, NCEngineeringFull-time ▒ Apply\xa0...',
    'htmlSnippet': 'Android Engineer *. San Francisco, CAEngineeringFull-time &middot; Apply ... Security <br>\n<b>Software Engineer</b>: Charlotte, NC. Charlotte, NCEngineeringFull-time &middot; Apply&nbsp;...',
    'cacheId': 'lDdS0Kr-REEJ',
    'formattedUrl': 'https://jobs.lever.co/creditkarma?by=commitment',
    'htmlFormattedUrl': 'https://jobs.lever.co/creditkarma?by=commitment',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma',
          'twitter:description': 'Job openings at Credit Karma',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma jobs',
          'og:description': 'Job openings at Credit Karma',
          'og:url': 'https://jobs.lever.co/creditkarma',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Director, Platform Engineering',
    'htmlTitle': 'Credit Karma - Director, Platform <b>Engineering</b>',
    'link': 'https://jobs.lever.co/creditkarma/cca3085a-f9d3-4789-8c3e-8888d9ad566a',
    'displayLink': 'jobs.lever.co',
    'snippet': 'The Director of Engineering Efficiency is responsible for the vision, strategy, ... \nand infrastructure, have an expert understanding of software best practices,\xa0...',
    'htmlSnippet': 'The Director of <b>Engineering</b> Efficiency is responsible for the vision, strategy, ... <br>\nand infrastructure, have an expert understanding of <b>software</b> best practices,&nbsp;...',
    'cacheId': 'X622n2-LuPUJ',
    'formattedUrl': 'https://jobs.lever.co/.../cca3085a-f9d3-4789-8c3e-8888d9ad566a',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../cca3085a-f9d3-4789-8c3e-8888d9ad566a',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Director, Platform Engineering',
          'twitter:description': 'Credit Karma is working to make financial progress possible for everyone. Engineering Efficiency plays a pivotal role in this mission by providing our engineering organization with the tools and frameworks needed to develop and ship code as quickly as possible in a controlled, self-service manner. The Director of Engineering Efficiency is responsible for the vision, strategy, roadmap and implementation of our development environments, testing platforms, and deployment frameworks across all surfaces (web, iOS, and android). You will manage multiple teams and develop an organization that is centered on improving our time-to-market. A successful Engineering Efficiency team will act as a force multiplier for our entire engineering organization by removing friction from development processes and empowering individual teams to be self-sufficient. Reporting to the Sr. Director of Platform Engineering, the DIrector of Engineering Efficiency has significant cross-functional experience, is adep',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - Director, Platform Engineering',
          'og:description': 'Credit Karma is working to make financial progress possible for everyone. Engineering Efficiency plays a pivotal role in this mission by providing our engineering organization with the tools and frameworks needed to develop and ship code as quickly as possible in a controlled, self-service manner. The Director of Engineering Efficiency is responsible for the vision, strategy, roadmap and implementation of our development environments, testing platforms, and deployment frameworks across all surfaces (web, iOS, and android). You will manage multiple teams and develop an organization that is centered on improving our time-to-market. A successful Engineering Efficiency team will act as a force multiplier for our entire engineering organization by removing friction from development processes and empowering individual teams to be self-sufficient. Reporting to the Sr. Director of Platform Engineering, the DIrector of Engineering Efficiency has significant cross-functional experience, is adep',
          'og:url': 'https://jobs.lever.co/creditkarma/cca3085a-f9d3-4789-8c3e-8888d9ad566a',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Program Manager, Marketing',
    'htmlTitle': 'Credit Karma - Program Manager, Marketing',
    'link': 'https://jobs.lever.co/creditkarma/14d75029-5171-4c34-bf35-0b4795b604fd',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Software start-up experience, with an early background as a software engineer or \nother technical role. Experience project managing multiple teams toward a\xa0...',
    'htmlSnippet': 'Software start-up experience, with an early background as a <b>software engineer</b> or <br>\nother technical role. Experience project managing multiple teams toward a&nbsp;...',
    'cacheId': '0-45vzqZELIJ',
    'formattedUrl': 'https://jobs.lever.co/.../14d75029-5171-4c34-bf35-0b4795b604fd',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../14d75029-5171-4c34-bf35-0b4795b604fd',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '541',
          'height': '93',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTJ_MyGMTa8ldvbcBh0lOtkD3-vsqEO5B4sA6C7RMGhgw24lCLt-OQk5Q'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Program Manager, Marketing',
          'twitter:description': 'Credit Karma is looking for a Program Manager of Marketing to bring leadership and organization, to our Performance Marketing and Member Engagement Programs. This role is a unique opportunity to help develop new processes that will shape the future of rapidly growing organizations within Marketing. You will focus on establishing leadership, roadmap execution, project reporting, and team efficiency.   We are seeking people who are passionate about taking action in order to get things done quickly and efficiently. You are well organized, proactively look for areas to provide value, and never let little things drop. You excel at building relationships, establishing good communication channels, and clarifying milestones and end goals. You▒ll work closely with your program teams to drive dialog that brings together Marketing, Copy, Design, Brand, Product, Development, Quality Assurance, Security, Legal, Analytics and anyone else needed to deliver successful initiatives. \xa0',
          'og:title': 'Credit Karma - Program Manager, Marketing',
          'og:description': 'Credit Karma is looking for a Program Manager of Marketing to bring leadership and organization, to our Performance Marketing and Member Engagement Programs. This role is a unique opportunity to help develop new processes that will shape the future of rapidly growing organizations within Marketing. You will focus on establishing leadership, roadmap execution, project reporting, and team efficiency.   We are seeking people who are passionate about taking action in order to get things done quickly and efficiently. You are well organized, proactively look for areas to provide value, and never let little things drop. You excel at building relationships, establishing good communication channels, and clarifying milestones and end goals. You▒ll work closely with your program teams to drive dialog that brings together Marketing, Copy, Design, Brand, Product, Development, Quality Assurance, Security, Legal, Analytics and anyone else needed to deliver successful initiatives. \xa0',
          'og:url': 'https://jobs.lever.co/creditkarma/14d75029-5171-4c34-bf35-0b4795b604fd',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1450394750591.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1450394750591.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma',
    'htmlTitle': 'Credit Karma',
    'link': 'https://jobs.lever.co/creditkarma?location=Venice%2C%20CA',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Full-Stack QA Engineer: Venice, CA. Venice, CAEngineeringFull-time ▒ Apply ▒ \nSoftware Engineer, Venice CA. Venice, CAEngineeringFull-time ▒ Credit Karma\xa0...',
    'htmlSnippet': 'Full-Stack QA Engineer: Venice, CA. Venice, CAEngineeringFull-time &middot; Apply &middot; <br>\n<b>Software Engineer</b>, Venice CA. Venice, CAEngineeringFull-time &middot; Credit Karma&nbsp;...',
    'cacheId': '5yZRrO_hiLgJ',
    'formattedUrl': 'https://jobs.lever.co/creditkarma?location=Venice%2C%20CA',
    'htmlFormattedUrl': 'https://jobs.lever.co/creditkarma?location=Venice%2C%20CA',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma',
          'twitter:description': 'Job openings at Credit Karma',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma jobs',
          'og:description': 'Job openings at Credit Karma',
          'og:url': 'https://jobs.lever.co/creditkarma',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - Machine Learning Engineer',
    'htmlTitle': 'Credit Karma - Machine Learning <b>Engineer</b>',
    'link': 'https://jobs.lever.co/creditkarma/cf0ea7df-9a19-4c14-bf4a-6a627e36bd70',
    'displayLink': 'jobs.lever.co',
    'snippet': "Engineering. Full-time. Apply for this job. As a Machine Learning Engineer, you'll \nbe a member of a team of Machine ... 5+ years of exp in software development.",
    'htmlSnippet': '<b>Engineering</b>. Full-time. Apply for this job. As a Machine Learning <b>Engineer</b>, you&#39;ll <br>\nbe a member of a team of Machine ... 5+ years of exp in <b>software</b> development.',
    'cacheId': '7qkqJKaZIB8J',
    'formattedUrl': 'https://jobs.lever.co/.../cf0ea7df-9a19-4c14-bf4a-6a627e36bd70',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../cf0ea7df-9a19-4c14-bf4a-6a627e36bd70',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - Machine Learning Engineer',
          'twitter:description': "As a Machine Learning Engineer, you▒ll be a member of a team of Machine Learning Engineers working closely with data scientists. You▒ll be working on the machine learning infrastructure to help data scientists develop models which will be used to improve user experience through better personalization. You▒ll be working with cutting edge technologies such Spark and Scala. We are a growing Engineering team, yet we offer a great deal of autonomy and flexibility. If you're a person who enjoys working with a lot of freedom, but knows how to take full ownership of a project and meet deadlines with quality, then this is the role for you.",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - Machine Learning Engineer',
          'og:description': "As a Machine Learning Engineer, you▒ll be a member of a team of Machine Learning Engineers working closely with data scientists. You▒ll be working on the machine learning infrastructure to help data scientists develop models which will be used to improve user experience through better personalization. You▒ll be working with cutting edge technologies such Spark and Scala. We are a growing Engineering team, yet we offer a great deal of autonomy and flexibility. If you're a person who enjoys working with a lot of freedom, but knows how to take full ownership of a project and meet deadlines with quality, then this is the role for you.",
          'og:url': 'https://jobs.lever.co/creditkarma/cf0ea7df-9a19-4c14-bf4a-6a627e36bd70',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Credit Karma - IT Client Engineering Manager',
    'htmlTitle': 'Credit Karma - IT Client <b>Engineering</b> Manager',
    'link': 'https://jobs.lever.co/creditkarma/0bfde12c-d5d7-496f-b7ad-2410aeaf433a',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Credit Karma is looking for an engineering lead / manager to be a part of our ... \nsoftware packaging and distribution, patching and configuration, scripting, remote\n\xa0...',
    'htmlSnippet': 'Credit Karma is looking for an <b>engineering</b> lead / manager to be a part of our ... <br>\n<b>software</b> packaging and distribution, patching and configuration, scripting, remote<br>\n&nbsp;...',
    'cacheId': '5ihuqaAQT3MJ',
    'formattedUrl': 'https://jobs.lever.co/.../0bfde12c-d5d7-496f-b7ad-2410aeaf433a',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../0bfde12c-d5d7-496f-b7ad-2410aeaf433a',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '318',
          'height': '159',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT88y7qk0cnmtKfS0kK3W_4rR7RjbshGWIpByfVHgxu3wdY4UomV4dQosE'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Credit Karma - IT Client Engineering Manager',
          'twitter:description': 'Credit Karma is looking for an engineering lead / manager to be a part of our leadership team. If you have a technical background and are interested in all the challenges of people leadership, you might make a great fit for engineering management at CK. Our ideal candidate is passionate about providing the end user experience possible, driving client config best practices within the team and constantly finding ways to improve end-user experience and IT efficiency through automation.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1481750115546.png',
          'og:title': 'Credit Karma - IT Client Engineering Manager',
          'og:description': 'Credit Karma is looking for an engineering lead / manager to be a part of our leadership team. If you have a technical background and are interested in all the challenges of people leadership, you might make a great fit for engineering management at CK. Our ideal candidate is passionate about providing the end user experience possible, driving client config best practices within the team and constantly finding ways to improve end-user experience and IT efficiency through automation.',
          'og:url': 'https://jobs.lever.co/creditkarma/0bfde12c-d5d7-496f-b7ad-2410aeaf433a',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/f286c1a5-decd-48c4-9385-976a7dbaf7fa-1491338386889.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Abacus - Software Engineer: Full Stack',
    'htmlTitle': 'Abacus - <b>Software Engineer</b>: Full Stack',
    'link': 'https://jobs.lever.co/abacus/e35c834e-1be7-4920-83b6-05dfed512afd',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Abacus is seeking an experienced full stack software engineer to join our small, \ncollaborative team building the next generation of expense tools. We are a fast\xa0...',
    'htmlSnippet': 'Abacus is seeking an experienced full stack <b>software engineer</b> to join our small, <br>\ncollaborative team building the next generation of expense tools. We are a fast&nbsp;...',
    'cacheId': 'HGArtKGWsYgJ',
    'formattedUrl': 'https://jobs.lever.co/.../e35c834e-1be7-4920-83b6-05dfed512afd',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../e35c834e-1be7-4920-83b6-05dfed512afd',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '310',
          'height': '163',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRC9kjGXU7qw76ZC2cWO3NF2PGgrvKrv36mafktn6SGZUZIlWQ87YiT5zkN'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Abacus - Software Engineer: Full Stack',
          'twitter:description': "Abacus is seeking an experienced full stack software engineer to join our small, collaborative team building the next generation of expense tools. We are a fast moving team that ships daily and constantly iterates to produce the best tools for our customers. About You: You should have experience working with modern web frameworks, knowledge of Node and Express is welcome but not a prerequisite. About Abacus: At Abacus, we're reimagining the way businesses move money, starting with the first real-time employee expense system. We▒re excited about building tools that are not only effective but enjoyable for everyone to use. Creating the best customer experience drives us - we love hearing everyday how what we're working on is saving our customers time and headaches. Making expense reports obsolete is only the beginning - join a team that is leading the charge in how businesses manage their cash flow.",
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/1a10c230-94a1-461a-8af0-4f3c1e419d91-1504892895451.png',
          'og:title': 'Abacus - Software Engineer: Full Stack',
          'og:description': "Abacus is seeking an experienced full stack software engineer to join our small, collaborative team building the next generation of expense tools. We are a fast moving team that ships daily and constantly iterates to produce the best tools for our customers. About You: You should have experience working with modern web frameworks, knowledge of Node and Express is welcome but not a prerequisite. About Abacus: At Abacus, we're reimagining the way businesses move money, starting with the first real-time employee expense system. We▒re excited about building tools that are not only effective but enjoyable for everyone to use. Creating the best customer experience drives us - we love hearing everyday how what we're working on is saving our customers time and headaches. Making expense reports obsolete is only the beginning - join a team that is leading the charge in how businesses manage their cash flow.",
          'og:url': 'https://jobs.lever.co/abacus/e35c834e-1be7-4920-83b6-05dfed512afd',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/1a10c230-94a1-461a-8af0-4f3c1e419d91-1504893306435.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/1a10c230-94a1-461a-8af0-4f3c1e419d91-1504893306435.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Abacus - Software Engineer: Full Stack',
    'htmlTitle': 'Abacus - <b>Software Engineer</b>: Full Stack',
    'link': 'https://jobs.lever.co/abacus/e35c834e-1be7-4920-83b6-05dfed512afd/',
    'displayLink': 'jobs.lever.co',
    'snippet': "Software Engineer: Full Stack. New York City. Engineering. Full-time. Submit your \napplication. Resume/CV. ATTACH RESUME/CV. Couldn't auto-read resume.",
    'htmlSnippet': '<b>Software Engineer</b>: Full Stack. New York City. Engineering. Full-time. Submit your <br>\napplication. Resume/CV. ATTACH RESUME/CV. Couldn&#39;t auto-read resume.',
    'cacheId': '7nY7giWGLv8J',
    'formattedUrl': 'https://jobs.lever.co/abacus/e35c834e-1be7-4920-83b6.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/abacus/e35c834e-1be7-4920-83b6.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '395',
          'height': '84',
          'src': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpsBpOfnuHiLZaozmevAi2K5CElXkq6crtVggJvfXanorFxctcaBcFmg'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Abacus - Software Engineer: Full Stack',
          'twitter:description': "Abacus is seeking an experienced full stack software engineer to join our small, collaborative team building the next generation of expense tools. We are a fast moving team that ships daily and constantly iterates to produce the best tools for our customers. About You: You should have experience working with modern web frameworks, knowledge of Node and Express is welcome but not a prerequisite. About Abacus: At Abacus, we're reimagining the way businesses move money, starting with the first real-time employee expense system. We▒re excited about building tools that are not only effective but enjoyable for everyone to use. Creating the best customer experience drives us - we love hearing everyday how what we're working on is saving our customers time and headaches. Making expense reports obsolete is only the beginning - join a team that is leading the charge in how businesses manage their cash flow.",
          'og:title': 'Abacus - Software Engineer: Full Stack',
          'og:description': "Abacus is seeking an experienced full stack software engineer to join our small, collaborative team building the next generation of expense tools. We are a fast moving team that ships daily and constantly iterates to produce the best tools for our customers. About You: You should have experience working with modern web frameworks, knowledge of Node and Express is welcome but not a prerequisite. About Abacus: At Abacus, we're reimagining the way businesses move money, starting with the first real-time employee expense system. We▒re excited about building tools that are not only effective but enjoyable for everyone to use. Creating the best customer experience drives us - we love hearing everyday how what we're working on is saving our customers time and headaches. Making expense reports obsolete is only the beginning - join a team that is leading the charge in how businesses manage their cash flow.",
          'og:url': 'https://jobs.lever.co/abacus/e35c834e-1be7-4920-83b6-05dfed512afd/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/abacus-logo.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/abacus-logo.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Abacus',
    'htmlTitle': 'Abacus',
    'link': 'https://jobs.lever.co/abacus?by=location',
    'displayLink': 'jobs.lever.co',
    'snippet': 'New York CitySalesFull-time ▒ Apply ▒ Software Engineer: Full Stack. New York \nCityEngineeringFull-time ▒ Abacus Home Page ▒ Jobs powered by.',
    'htmlSnippet': 'New York CitySalesFull-time &middot; Apply &middot; <b>Software Engineer</b>: Full Stack. New York <br>\nCityEngineeringFull-time &middot; Abacus Home Page &middot; Jobs powered by.',
    'cacheId': 'BBvOSm_YAPwJ',
    'formattedUrl': 'https://jobs.lever.co/abacus?by=location',
    'htmlFormattedUrl': 'https://jobs.lever.co/abacus?by=location',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '316',
          'height': '67',
          'src': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTncIEtbWSMEVLfi4-wZ1MepfpK-kXh_pPFXmFu678oireSjtEeGXWMlg'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Abacus',
          'twitter:description': 'Job openings at Abacus',
          'og:title': 'Abacus jobs',
          'og:description': 'Job openings at Abacus',
          'og:url': 'https://jobs.lever.co/abacus',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/abacus-logo.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/abacus-logo.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'Abacus',
    'htmlTitle': 'Abacus',
    'link': 'https://jobs.lever.co/abacus',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Product Specialist. New York CityCustomerFull-time. Engineering. Apply ▒ \nSoftware Engineer: Full Stack. New York CityEngineeringFull-time. Sales. Apply\xa0...',
    'htmlSnippet': 'Product Specialist. New York CityCustomerFull-time. Engineering. Apply &middot; <br>\n<b>Software Engineer</b>: Full Stack. New York CityEngineeringFull-time. Sales. Apply&nbsp;...',
    'cacheId': 'DoIUbNd7sNoJ',
    'formattedUrl': 'https://jobs.lever.co/abacus',
    'htmlFormattedUrl': 'https://jobs.lever.co/abacus',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '316',
          'height': '67',
          'src': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTncIEtbWSMEVLfi4-wZ1MepfpK-kXh_pPFXmFu678oireSjtEeGXWMlg'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'Abacus',
          'twitter:description': 'Job openings at Abacus',
          'og:title': 'Abacus jobs',
          'og:description': 'Job openings at Abacus',
          'og:url': 'https://jobs.lever.co/abacus',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/abacus-logo.png',
          'og:image:height': '200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/abacus-logo.png'
        }
      ]
    }
  }
]

# local manual per listing test
def get_job_listings_from_google():
    data_get_job_listings_from_google = results_from_GSE_query
    return data_get_job_listings_from_google

def get_job_listings_from_google(cse_search_term, number_of_listings_to_get = 100):
    return_value = []
    try:
        for search_result_number_from_which_api_query_results_start in range(1, number_of_listings_to_get + 1, MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY):
            return_value.extend(do_google_search(
                # https://i.codefor.cash/job_alerts/generate_subscriber_keywords
                # 'site:jobs.lever.co "c++" +engineer'
                search_term=cse_search_term,
                api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN, num=MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY,
                # start=1))
                start=search_result_number_from_which_api_query_results_start))
    except:
        pass
    print(return_value[:number_of_listings_to_get])
    return return_value[:number_of_listings_to_get]

# def save_gse_call_results(listings):
#     with open('finalResults.txt','a+') as f:
#         f.write(json.dumps(get_job_listings_from_google()), sort_keys = True,
#                 indent = 4)

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
            print(web_data)

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
    send_job_listings_to_codeforcash(get_job_listings_from_google())
    # send_job_listings_to_codeforcash(pass_different_clients())
    
    # get_job_listings_from_google(pass_different_clients())
    
    # save_gse_call_results(send_job_listings_to_codeforcash(get_job_listings_from_google(pass_different_clients())))

    # save_gse_call_results(send_job_listings_to_codeforcash(remove_non_ascii(get_job_listings_from_google())))

    # send_job_listings_to_codeforcash(return_value)
    # save_gse_call_results(return_value)

    # save_result_of_sending_job_listings_to_codeforcash(send_job_listings_to_codeforcash(return_value))

    # save_gse_call_results(get_job_listings_from_google())

    # save_result_of_sending_job_listings_to_codeforcash(
    #     get_job_listings_from_google())
        
