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
from pygeocoder import Geocoder
from pygeolib import GeocoderError
import time
import sys


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

BAD_WORDS_LIST = ["personal trainer", "executive assistant", "low cost","ultimate software", "app tester", "1-2 hours a day","secretary", "front desk", "office manager", "use referr", "commission", "motivated individuals" , "sales specialist","no experience required", "amazing opportunity", "court researcher","technical support", "tech support", "mystery shopper","customer service", "field engineer", "administrative", "book keeping", "extra money", "extra cash", "extra income", "data entry", "have a car", "debit card", "earn extra income", "step by step training", "dollars a week", "supplemental income", "sales rep","closed lead", "do you want to make", "facebook page", "facebook fan page", "theater installation", "game tester", "% stake","printing and mailing", "laserjet", "credit score","real estate investment", "marketing", "research study","in person", "focus group", "survey", "you must live", "local", "must be local", "tutor", "instructor", "partner ", "equity", "cofounder", "co founder", "co-founder", "unpaid", "volunteer", "get paid", "get pay", "weekly", "webcam", "money making", "fast money", "workfromhome", "fast cash", "scam", "make money", "selling cell phones", "wireless sales", "it's legit", "telemarketer", "fb account", "Cell Phone Repair", "earn money by just", "only applicants residing in", "from his location", "virtual assistant", "by working less", "earn extra money", "experienced seller", "looking for a job", "earn over", "motorclub",  "office assistant", "event planner", "____________________________________________________________", "Filter by:"]

# # def do_google_search(search_term, api_key, cse_id, **kwargs):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
#     print('<<<< CSE Query Loop >>>>')
#     print(res['queries']['request'][0]['startIndex'], 'CSE Start Index')
#     print(res['queries']['request'][0]['totalResults'], 'CSE Query Results')

#     if res['queries']['request'][0]['totalResults'] == '0':
#         # # # prints when reach the gse page where totalResults == '0'
#         print('@@@@ NO CSE QUERY RESULTS @@@@')
#         # print(res)
#         return res['items']
#     else:
#         return res['items']


# test boards
results_from_GSE_query_51 = [
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b>",
    "link": "https://jobs.lever.co/twitch/c795ef2d-2621-4383-8aa1-c85c8750bfa2",
    "displayLink": "jobs.lever.co",
    "snippet": "We are rapidly expanding the engineering team at Twitch to deal with \nchallenging scale problem of being the 4th biggest consumer of bandwidth and \none of the\u00a0...",
    "htmlSnippet": "We are rapidly expanding the <b>engineering</b> team at Twitch to deal with <br>\nchallenging scale problem of being the 4th biggest consumer of bandwidth and <br>\none of the&nbsp;...",
    "cacheId": "IfDwOzBaIzwJ",
    "formattedUrl": "https://jobs.lever.co/twitch/c795ef2d-2621-4383-8aa1-c85c8750bfa2",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/c795ef2d-2621-4383-8aa1-c85c8750bfa2",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer",
          "twitter:description": "We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Here\u2019s a short list of current scale: -Serve more than 150 million unique visitors per month -More than 2 million peak concurrent users -16 billion minutes of video watched each month and growing -10 billion messages sent on chat per day and growing -Serving 5 million+ requests per second on the edge and growing -Anticipated scale year-over-year = 2.5x -Current Engineering Team Size: ~100 People Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. We are looking for the next set of engineering te",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer",
          "og:description": "We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Here\u2019s a short list of current scale: -Serve more than 150 million unique visitors per month -More than 2 million peak concurrent users -16 billion minutes of video watched each month and growing -10 billion messages sent on chat per day and growing -Serving 5 million+ requests per second on the edge and growing -Anticipated scale year-over-year = 2.5x -Current Engineering Team Size: ~100 People Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. We are looking for the next set of engineering te",
          "og:url": "https://jobs.lever.co/twitch/c795ef2d-2621-4383-8aa1-c85c8750bfa2",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Internationalization",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Internationalization",
    "link": "https://jobs.lever.co/twitch/061a5dd7-bd54-4a06-8f62-6b44f5a19bfc",
    "displayLink": "jobs.lever.co",
    "snippet": "Our team builds the foundations that ensure overall product quality and \nfunctionality for all software development at Twitch, including bringing all our \nproducts to\u00a0...",
    "htmlSnippet": "Our team builds the foundations that ensure overall product quality and <br>\nfunctionality for all <b>software</b> development at Twitch, including bringing all our <br>\nproducts to&nbsp;...",
    "cacheId": "ZePYSCpWJMcJ",
    "formattedUrl": "https://jobs.lever.co/twitch/061a5dd7-bd54-4a06-8f62-6b44f5a19bfc",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/061a5dd7-bd54-4a06-8f62-6b44f5a19bfc",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Internationalization",
          "twitter:description": "Millions of visitors per month watch billions of minutes of video on Twitch around the world in many locales and languages on the web, mobile, and gaming consoles. Our team builds the foundations that ensure overall product quality and functionality for all software development at Twitch, including bringing all our products to world readiness. Agile and effective collaboration with other teams is at the heart of our charter, our challenge, and our passion. You are passionate about software development and delivering a great product to all users around the world. You keep up-to-date with your craft but often dabble beyond; you are intellectually curious, inventive, and eager to grow. You understand how code is written up and down the stack and how to build, integrate, test, and deploy global-ready solutions with the latest tools and best practices. You are equally excited to build a minimum viable product quickly as you are cementing a proven feature in maintainable and tested code. Yo",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Internationalization",
          "og:description": "Millions of visitors per month watch billions of minutes of video on Twitch around the world in many locales and languages on the web, mobile, and gaming consoles. Our team builds the foundations that ensure overall product quality and functionality for all software development at Twitch, including bringing all our products to world readiness. Agile and effective collaboration with other teams is at the heart of our charter, our challenge, and our passion. You are passionate about software development and delivering a great product to all users around the world. You keep up-to-date with your craft but often dabble beyond; you are intellectually curious, inventive, and eager to grow. You understand how code is written up and down the stack and how to build, integrate, test, and deploy global-ready solutions with the latest tools and best practices. You are equally excited to build a minimum viable product quickly as you are cementing a proven feature in maintainable and tested code. Yo",
          "og:url": "https://jobs.lever.co/twitch/061a5dd7-bd54-4a06-8f62-6b44f5a19bfc",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Infrastructure",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Infrastructure",
    "link": "https://jobs.lever.co/twitch/786045c4-5534-4d97-b04a-74771f6856bb",
    "displayLink": "jobs.lever.co",
    "snippet": "Twitch has over 100 million users, and the Video Infra team is responsible for \nbuilding infra services and tools to help scale and manage the infrastructure that\n\u00a0...",
    "htmlSnippet": "Twitch has over 100 million users, and the Video Infra team is responsible for <br>\nbuilding infra services and tools to help scale and manage the infrastructure that<br>\n&nbsp;...",
    "cacheId": "3UywsZWkSyUJ",
    "formattedUrl": "https://jobs.lever.co/.../786045c4-5534-4d97-b04a-74771f6856bb",
    "htmlFormattedUrl": "https://jobs.lever.co/.../786045c4-5534-4d97-b04a-74771f6856bb",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Infrastructure",
          "twitter:description": "Twitch has over 100 million users, and the Video Infra team is responsible for building infra services and tools to help scale and manage the infrastructure that powers Twitch\u2019s video. We\u2019re building a number of features to make Twitch the most compelling destination for video. We\u2019re looking for engineers that love delighting people with incredible products and user experiences. On the infra team, you\u2019ll work closely with our other engineering and product teams to craft engaging systems collect feedback, and iterate quickly. We value expertise in distributed systems, microservices and Devops on AWS. We are working on building an even more robust video system to scale twitch to the next level .",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Infrastructure",
          "og:description": "Twitch has over 100 million users, and the Video Infra team is responsible for building infra services and tools to help scale and manage the infrastructure that powers Twitch\u2019s video. We\u2019re building a number of features to make Twitch the most compelling destination for video. We\u2019re looking for engineers that love delighting people with incredible products and user experiences. On the infra team, you\u2019ll work closely with our other engineering and product teams to craft engaging systems collect feedback, and iterate quickly. We value expertise in distributed systems, microservices and Devops on AWS. We are working on building an even more robust video system to scale twitch to the next level .",
          "og:url": "https://jobs.lever.co/twitch/786045c4-5534-4d97-b04a-74771f6856bb",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Video CDN",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Video CDN",
    "link": "https://jobs.lever.co/twitch/2fae3239-fe4d-4582-bfdf-7d43727853d3",
    "displayLink": "jobs.lever.co",
    "snippet": "Twitch is building the future of interactive entertainment, and our video CDN is at \nthe core of that vision. Ensuring smooth, low-latency video across the world\u00a0...",
    "htmlSnippet": "Twitch is building the future of interactive entertainment, and our video CDN is at <br>\nthe core of that vision. Ensuring smooth, low-latency video across the world&nbsp;...",
    "cacheId": "aee-uZY0VS0J",
    "formattedUrl": "https://jobs.lever.co/twitch/2fae3239-fe4d-4582-bfdf-7d43727853d3",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/2fae3239-fe4d-4582-bfdf-7d43727853d3",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Video CDN",
          "twitter:description": "Twitch is building the future of interactive entertainment, and our video CDN is at the core of that vision. Ensuring smooth, low-latency video across the world requires large-scale, fault-tolerant systems that can keep up with millions of simultaneous viewers and thousands of broadcasters. We are looking for engineers who are excited by the thought of working across the entire CDN stack, from service load-balancing, to performance optimization, to backbone traffic management. You will help architect, develop, test, deploy, operate, and maintain our video software software. As part of the team, we will work together to enable our broadcasters and viewers to create and interact in new, innovative ways.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Video CDN",
          "og:description": "Twitch is building the future of interactive entertainment, and our video CDN is at the core of that vision. Ensuring smooth, low-latency video across the world requires large-scale, fault-tolerant systems that can keep up with millions of simultaneous viewers and thousands of broadcasters. We are looking for engineers who are excited by the thought of working across the entire CDN stack, from service load-balancing, to performance optimization, to backbone traffic management. You will help architect, develop, test, deploy, operate, and maintain our video software software. As part of the team, we will work together to enable our broadcasters and viewers to create and interact in new, innovative ways.",
          "og:url": "https://jobs.lever.co/twitch/2fae3239-fe4d-4582-bfdf-7d43727853d3",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - VOD",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - VOD",
    "link": "https://jobs.lever.co/twitch/58d343d0-4aa6-4516-84c2-c542f68b649a",
    "displayLink": "jobs.lever.co",
    "snippet": "Twitch has over 100 million users, and the VOD team is responsible for building a \nnew experience that helps Twitch users watch recorded video. We're building\u00a0...",
    "htmlSnippet": "Twitch has over 100 million users, and the VOD team is responsible for building a <br>\nnew experience that helps Twitch users watch recorded video. We&#39;re building&nbsp;...",
    "cacheId": "sEnt9yZhqrgJ",
    "formattedUrl": "https://jobs.lever.co/.../58d343d0-4aa6-4516-84c2-c542f68b649a",
    "htmlFormattedUrl": "https://jobs.lever.co/.../58d343d0-4aa6-4516-84c2-c542f68b649a",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - VOD",
          "twitter:description": "Twitch has over 100 million users, and the VOD team is responsible for building a new experience that helps Twitch users watch recorded video. We\u2019re building a number of features to make Twitch the most compelling destination for gaming recorded video this year. Recently, we launched VOD upload, Clips and our HTML5 Video Player, and we\u2019re just getting started. We\u2019re looking for product engineers that love delighting people with incredible products and user experiences. On the VOD team, you\u2019ll work closely with our other engineering and product teams to craft engaging consumer products, collect feedback, and iterate quickly. We value expertise in programming for the Web, microservices and Devops on AWS. If you are also comfortable with JS and crafting beautiful interfaces, even better! We are working on building unique VOD watching experiences that are uniquely Twitch. We aspire to change the way people consume and interact with video.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - VOD",
          "og:description": "Twitch has over 100 million users, and the VOD team is responsible for building a new experience that helps Twitch users watch recorded video. We\u2019re building a number of features to make Twitch the most compelling destination for gaming recorded video this year. Recently, we launched VOD upload, Clips and our HTML5 Video Player, and we\u2019re just getting started. We\u2019re looking for product engineers that love delighting people with incredible products and user experiences. On the VOD team, you\u2019ll work closely with our other engineering and product teams to craft engaging consumer products, collect feedback, and iterate quickly. We value expertise in programming for the Web, microservices and Devops on AWS. If you are also comfortable with JS and crafting beautiful interfaces, even better! We are working on building unique VOD watching experiences that are uniquely Twitch. We aspire to change the way people consume and interact with video.",
          "og:url": "https://jobs.lever.co/twitch/58d343d0-4aa6-4516-84c2-c542f68b649a",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Global Infrastructure",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Global Infrastructure",
    "link": "https://jobs.lever.co/twitch/7204c413-9e6b-449f-9536-39aaa75c0c78",
    "displayLink": "jobs.lever.co",
    "snippet": "We are rapidly expanding the engineering team at Twitch to deal with \nchallenging scale problem of being the 4th biggest consumer of bandwidth and \none of the\u00a0...",
    "htmlSnippet": "We are rapidly expanding the <b>engineering</b> team at Twitch to deal with <br>\nchallenging scale problem of being the 4th biggest consumer of bandwidth and <br>\none of the&nbsp;...",
    "cacheId": "ra9NS2Ro7YgJ",
    "formattedUrl": "https://jobs.lever.co/twitch/7204c413-9e6b-449f-9536-39aaa75c0c78",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/7204c413-9e6b-449f-9536-39aaa75c0c78",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Global Infrastructure",
          "twitter:description": "We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. We are looking for the next set of engineering tech leaders to help grow Twitch to the next level. We need strong senior tech leaders that are comfortable working cross-functionally and not be afraid to touch many portions of our code-base to ensure that Twitch services can scale and be robust. We are moving to an SOA world and we need people comfortable with balancing product innovation with building out robust systems.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Global Infrastructure",
          "og:description": "We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. We are looking for the next set of engineering tech leaders to help grow Twitch to the next level. We need strong senior tech leaders that are comfortable working cross-functionally and not be afraid to touch many portions of our code-base to ensure that Twitch services can scale and be robust. We are moving to an SOA world and we need people comfortable with balancing product innovation with building out robust systems.",
          "og:url": "https://jobs.lever.co/twitch/7204c413-9e6b-449f-9536-39aaa75c0c78",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Software Engineer - Tools & Automation",
    "htmlTitle": "Twitch - <b>Software Engineer</b> - Tools &amp; Automation",
    "link": "https://jobs.lever.co/twitch/fb787bb2-c616-4d63-94ef-a96ac7f86b79",
    "displayLink": "jobs.lever.co",
    "snippet": "Twitch is seeking an experienced Software Engineer for our Quality Engineering \nteam, who will be responsible for our test infrastructure and will be the quality\u00a0...",
    "htmlSnippet": "Twitch is seeking an experienced <b>Software Engineer</b> for our Quality Engineering <br>\nteam, who will be responsible for our test infrastructure and will be the quality&nbsp;...",
    "cacheId": "4h_N4PalkYgJ",
    "formattedUrl": "https://jobs.lever.co/twitch/fb787bb2-c616-4d63-94ef-a96ac7f86b79",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/fb787bb2-c616-4d63-94ef-a96ac7f86b79",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Software Engineer - Tools & Automation",
          "twitter:description": "Twitch is seeking an experienced Software Engineer for our Quality Engineering team, who will be responsible for our test infrastructure and will be the quality champion of Twitch. As a Software Engineer,Tools , you will be responsible for establishing a consistent testing methodology for all products we release and promoting best practices across our many product development teams.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Software Engineer - Tools & Automation",
          "og:description": "Twitch is seeking an experienced Software Engineer for our Quality Engineering team, who will be responsible for our test infrastructure and will be the quality champion of Twitch. As a Software Engineer,Tools , you will be responsible for establishing a consistent testing methodology for all products we release and promoting best practices across our many product development teams.",
          "og:url": "https://jobs.lever.co/twitch/fb787bb2-c616-4d63-94ef-a96ac7f86b79",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Network Software Engineer",
    "htmlTitle": "Twitch - Senior Network <b>Software Engineer</b>",
    "link": "https://jobs.lever.co/twitch/e8915dbe-817e-4aec-af61-01088eb4867f",
    "displayLink": "jobs.lever.co",
    "snippet": "By joining the Network Development team, as a Sr. Network Software Engineer, \nyou can help shape the future of network automation at Twitch.The Network\u00a0...",
    "htmlSnippet": "By joining the Network Development team, as a Sr. Network <b>Software Engineer</b>, <br>\nyou can help shape the future of network automation at Twitch.The Network&nbsp;...",
    "cacheId": "Z9iJllvaCKwJ",
    "formattedUrl": "https://jobs.lever.co/twitch/e8915dbe-817e-4aec-af61-01088eb4867f",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/e8915dbe-817e-4aec-af61-01088eb4867f",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Network Software Engineer",
          "twitter:description": "We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. By joining the Network Development team, as a Sr. Network Software Engineer, you can help shape the future of network automation at Twitch.The Network Development team is responsible for building the framework and tooling for network: automation, orchestration, visualization, and alerting. This framework enables other teams to: increase efficiency, leverage network telemetry in their algorithms, and allows the Twitch network to dynamically react to c",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Network Software Engineer",
          "og:description": "We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Our technical stack is vast and our hardware deployments are far reaching to all corners of the globe. We leverage Go and Ruby throughout our stack. We utilize PostgreSQL and many NoSQL variants such as DynamoDB, Cassandra, Redis and ElasticSearch. Our scale and speed of our growth forces us to experiment with techniques and technologies. By joining the Network Development team, as a Sr. Network Software Engineer, you can help shape the future of network automation at Twitch.The Network Development team is responsible for building the framework and tooling for network: automation, orchestration, visualization, and alerting. This framework enables other teams to: increase efficiency, leverage network telemetry in their algorithms, and allows the Twitch network to dynamically react to c",
          "og:url": "https://jobs.lever.co/twitch/e8915dbe-817e-4aec-af61-01088eb4867f",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Identity",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Identity",
    "link": "https://jobs.lever.co/twitch/9ef94e2c-40db-4cff-aa5a-5b7c5e9bf230",
    "displayLink": "jobs.lever.co",
    "snippet": "We are looking for a Full Stack software developer to join the Identity Team at \nTwitch. We're building OAuth solutions for our community to make a Twitch \nIdentity\u00a0...",
    "htmlSnippet": "We are looking for a Full Stack <b>software</b> developer to join the Identity Team at <br>\nTwitch. We&#39;re building OAuth solutions for our community to make a Twitch <br>\nIdentity&nbsp;...",
    "cacheId": "hEfrPswIQrgJ",
    "formattedUrl": "https://jobs.lever.co/twitch/9ef94e2c-40db-4cff-aa5a-5b7c5e9bf230",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/9ef94e2c-40db-4cff-aa5a-5b7c5e9bf230",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Identity",
          "twitter:description": "We are looking for a Full Stack software developer to join the Identity Team at Twitch. We\u2019re building OAuth solutions for our community to make a Twitch Identity the last identity you\u2019ll ever need. This is a technical role that builds heavily on internet standards for authorization and authentication on the Twitch site and our OAuth enabled partners. Our products are highly scalable and highly available world wide. As we level up our architecture and features, you\u2019ll have the opportunity to influence design decisions, tooling choices, and every last detail that makes us the best product we can be.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Identity",
          "og:description": "We are looking for a Full Stack software developer to join the Identity Team at Twitch. We\u2019re building OAuth solutions for our community to make a Twitch Identity the last identity you\u2019ll ever need. This is a technical role that builds heavily on internet standards for authorization and authentication on the Twitch site and our OAuth enabled partners. Our products are highly scalable and highly available world wide. As we level up our architecture and features, you\u2019ll have the opportunity to influence design decisions, tooling choices, and every last detail that makes us the best product we can be.",
          "og:url": "https://jobs.lever.co/twitch/9ef94e2c-40db-4cff-aa5a-5b7c5e9bf230",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Commerce",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Commerce",
    "link": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf",
    "displayLink": "jobs.lever.co",
    "snippet": "We're looking for engineers that love solving hard technical problems related to \ngaming on PCs and Twitch. This project will require innovation and the ability to\u00a0...",
    "htmlSnippet": "We&#39;re looking for <b>engineers</b> that love solving hard technical problems related to <br>\ngaming on PCs and Twitch. This project will require innovation and the ability to&nbsp;...",
    "cacheId": "FWP11B-32uQJ",
    "formattedUrl": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Commerce",
          "twitter:description": "Twitch is building the future of interactive entertainment, and our windows client engineering team is growing in order to execute on a brand new, secret project. We\u2019re looking for engineers that love solving hard technical problems related to gaming on PCs and Twitch. This project will require innovation and the ability to come up with technical solutions in new spaces. You will also need to work with and be able to think like a game developer. We\u2019re working with top developers to help bring new experiences to customers. We\u2019re using a variety of tools and languages, but much of our work will be in C++, so you\u2019ll have to be willing to roll up your sleeves and get your hands dirty. You\u2019ll have to write a lot of code, but should also be able to mentor engineers around you and do whatever needs to be done for the team and product initiative to succeed.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Commerce",
          "og:description": "Twitch is building the future of interactive entertainment, and our windows client engineering team is growing in order to execute on a brand new, secret project. We\u2019re looking for engineers that love solving hard technical problems related to gaming on PCs and Twitch. This project will require innovation and the ability to come up with technical solutions in new spaces. You will also need to work with and be able to think like a game developer. We\u2019re working with top developers to help bring new experiences to customers. We\u2019re using a variety of tools and languages, but much of our work will be in C++, so you\u2019ll have to be willing to roll up your sleeves and get your hands dirty. You\u2019ll have to write a lot of code, but should also be able to mentor engineers around you and do whatever needs to be done for the team and product initiative to succeed.",
          "og:url": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Payments",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Payments",
    "link": "https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7",
    "displayLink": "jobs.lever.co",
    "snippet": "We're looking for a software engineer who gets why the story, \"I bought a sub \nusing my favorite streamer's sub button so I can talk in sub-only chat\" starts off\u00a0...",
    "htmlSnippet": "We&#39;re looking for a <b>software engineer</b> who gets why the story, &quot;I bought a sub <br>\nusing my favorite streamer&#39;s sub button so I can talk in sub-only chat&quot; starts off&nbsp;...",
    "cacheId": "hvR82k33zE0J",
    "formattedUrl": "https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Payments",
          "twitter:description": "Twitch is building the future of interactive entertainment. The services we create for our users have deep, lasting effects on their lives. For many of our partnered broadcasters, streaming on Twitch is a career, and our payments system is central to making that possible. We're looking for a software engineer who gets why the story, \"I bought a sub using my favorite streamer's sub button so I can talk in sub-only chat\" starts off looking simple, but isn't. You like wrangling existing technologies together to solve business problems. Maybe you've built an e-commerce site or two. On our team, you'll specialize in payments and related products like emotes and Turbo. Together, we're transforming the gaming world, $4.99 at a time.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Payments",
          "og:description": "Twitch is building the future of interactive entertainment. The services we create for our users have deep, lasting effects on their lives. For many of our partnered broadcasters, streaming on Twitch is a career, and our payments system is central to making that possible. We're looking for a software engineer who gets why the story, \"I bought a sub using my favorite streamer's sub button so I can talk in sub-only chat\" starts off looking simple, but isn't. You like wrangling existing technologies together to solve business problems. Maybe you've built an e-commerce site or two. On our team, you'll specialize in payments and related products like emotes and Turbo. Together, we're transforming the gaming world, $4.99 at a time.",
          "og:url": "https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Video Client",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Video Client",
    "link": "https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc",
    "displayLink": "jobs.lever.co",
    "snippet": "Twitch's Video Client Engineering team is looking for experienced video \nengineers to help build a cross-platform video playback solution that will support \nweb,\u00a0...",
    "htmlSnippet": "Twitch&#39;s Video Client <b>Engineering</b> team is looking for experienced video <br>\n<b>engineers</b> to help build a cross-platform video playback solution that will support <br>\nweb,&nbsp;...",
    "cacheId": "KKk1mIgltLMJ",
    "formattedUrl": "https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Video Client",
          "twitter:description": "Twitch is building the future of interactive entertainment and video is at the very core of that vision. Twitch\u2019s Video Client Engineering team is looking for experienced video engineers to help build a cross-platform video playback solution that will support web, mobile, and other platforms. As a core video engineer, you will be helping shape the future of the Twitch playback experience used by millions of users across various web browsers, mobile devices, gaming consoles, and more. If you are passionate about media, streaming, or obsessed about performance and want to participate in creating the best video playback system out there then this position is for you. You will work with an extremely talented and accomplished team in the video space and will be building a major component of the Video on Demand video playback pipeline that will scale to millions of users. You will gain an in-depth knowledge on a highly scalable, end to end video streaming platform.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Video Client",
          "og:description": "Twitch is building the future of interactive entertainment and video is at the very core of that vision. Twitch\u2019s Video Client Engineering team is looking for experienced video engineers to help build a cross-platform video playback solution that will support web, mobile, and other platforms. As a core video engineer, you will be helping shape the future of the Twitch playback experience used by millions of users across various web browsers, mobile devices, gaming consoles, and more. If you are passionate about media, streaming, or obsessed about performance and want to participate in creating the best video playback system out there then this position is for you. You will work with an extremely talented and accomplished team in the video space and will be building a major component of the Video on Demand video playback pipeline that will scale to millions of users. You will gain an in-depth knowledge on a highly scalable, end to end video streaming platform.",
          "og:url": "https://jobs.lever.co/twitch/9625abc3-a52d-4af0-b482-af57aa4e18fc",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Bits",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Bits",
    "link": "https://jobs.lever.co/twitch/ebad0f08-c9b4-4b52-bfa1-78edd6aa136b",
    "displayLink": "jobs.lever.co",
    "snippet": "Twitch is building the future of interactive entertainment, and our web client \nengineering team is preparing to scale to execute on critical product initiatives \nlike\u00a0...",
    "htmlSnippet": "Twitch is building the future of interactive entertainment, and our web client <br>\n<b>engineering</b> team is preparing to scale to execute on critical product initiatives <br>\nlike&nbsp;...",
    "cacheId": "tkktVlD-AkcJ",
    "formattedUrl": "https://jobs.lever.co/twitch/ebad0f08-c9b4-4b52-bfa1-78edd6aa136b",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/ebad0f08-c9b4-4b52-bfa1-78edd6aa136b",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Bits",
          "twitter:description": "Twitch is building the future of interactive entertainment, and our web client engineering team is preparing to scale to execute on critical product initiatives like Cheering with Bits, Subscriptions, Affiliates, Twitch Prime, and many great social interaction features. Our Seattle office is focused on exciting new e-commerce initiatives in 2017! We\u2019re looking for engineers that love delighting people with incredible products and user experiences. On the Commerce team, you\u2019ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in programming for the Web (including an understanding of modern JS tooling and cross-browser compatibility issues) and sensibilities for design and UX. The web client is written with Ember.js, builds using Ember CLI, uses ES6 features via Babel, and manifests backend systems like chat and video as user-facing products. We also are building some new featu",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Bits",
          "og:description": "Twitch is building the future of interactive entertainment, and our web client engineering team is preparing to scale to execute on critical product initiatives like Cheering with Bits, Subscriptions, Affiliates, Twitch Prime, and many great social interaction features. Our Seattle office is focused on exciting new e-commerce initiatives in 2017! We\u2019re looking for engineers that love delighting people with incredible products and user experiences. On the Commerce team, you\u2019ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in programming for the Web (including an understanding of modern JS tooling and cross-browser compatibility issues) and sensibilities for design and UX. The web client is written with Ember.js, builds using Ember CLI, uses ES6 features via Babel, and manifests backend systems like chat and video as user-facing products. We also are building some new featu",
          "og:url": "https://jobs.lever.co/twitch/ebad0f08-c9b4-4b52-bfa1-78edd6aa136b",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Frontend Software Engineer - Store",
    "htmlTitle": "Twitch - Frontend <b>Software Engineer</b> - Store",
    "link": "https://jobs.lever.co/twitch/0ee71b6e-bb91-47b9-8d28-4d3df21c09a9",
    "displayLink": "jobs.lever.co",
    "snippet": "Twitch is launching a merchandise line featuring our own community inspired \nlogos and designs and are in need of a creative mind to help bring the right\u00a0...",
    "htmlSnippet": "Twitch is launching a merchandise line featuring our own community inspired <br>\nlogos and designs and are in need of a creative mind to help bring the right&nbsp;...",
    "cacheId": "3fE41pyF6nAJ",
    "formattedUrl": "https://jobs.lever.co/.../0ee71b6e-bb91-47b9-8d28-4d3df21c09a9",
    "htmlFormattedUrl": "https://jobs.lever.co/.../0ee71b6e-bb91-47b9-8d28-4d3df21c09a9",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Frontend Software Engineer - Store",
          "twitter:description": "Twitch is launching a merchandise line featuring our own community inspired logos and designs and are in need of a creative mind to help bring the right customer experience onto Twitch. As an early joiner of the team you will gain the opportunity to influence an international launch, provide creative input into brand direction and drive high visibility projects across a number of commerce teams. We are looking for an experienced Front End Developer who has successfully demonstrated taking business goals and turning them into inspiring designs. The ideal candidate has strong organizational skills, web expertise, and acute attention to detail. They will have developed a deep technical understanding of the strengths and weaknesses of delivery platforms, and are able to identify opportunities and to work creatively within the constraints they impose. In this role, you will be expected to work closely with a team of designers, researchers, developers, and project managers. Using your ski",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Frontend Software Engineer - Store",
          "og:description": "Twitch is launching a merchandise line featuring our own community inspired logos and designs and are in need of a creative mind to help bring the right customer experience onto Twitch. As an early joiner of the team you will gain the opportunity to influence an international launch, provide creative input into brand direction and drive high visibility projects across a number of commerce teams. We are looking for an experienced Front End Developer who has successfully demonstrated taking business goals and turning them into inspiring designs. The ideal candidate has strong organizational skills, web expertise, and acute attention to detail. They will have developed a deep technical understanding of the strengths and weaknesses of delivery platforms, and are able to identify opportunities and to work creatively within the constraints they impose. In this role, you will be expected to work closely with a team of designers, researchers, developers, and project managers. Using your ski",
          "og:url": "https://jobs.lever.co/twitch/0ee71b6e-bb91-47b9-8d28-4d3df21c09a9",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Twitch Crates",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Twitch Crates",
    "link": "https://jobs.lever.co/twitch/4a17fcc9-b8da-4716-9e34-78663265b4f9",
    "displayLink": "jobs.lever.co",
    "snippet": "Twitch is building the future of interactive entertainment and our Commerce \nengineering team builds key services which allow thousands of creative\u00a0...",
    "htmlSnippet": "Twitch is building the future of interactive entertainment and our Commerce <br>\n<b>engineering</b> team builds key services which allow thousands of creative&nbsp;...",
    "cacheId": "mKIjAzgFIaAJ",
    "formattedUrl": "https://jobs.lever.co/twitch/4a17fcc9-b8da-4716-9e34-78663265b4f9",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/4a17fcc9-b8da-4716-9e34-78663265b4f9",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Twitch Crates",
          "twitter:description": "Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing \u201cgig economy\u201d which allows these creators to earn part or all of their income by producing high quality content on Twitch. Twitch Crates was introduced earlier this year as part of our Game Commerce strategy and we are looking for engineers who want to take it to the next level and scale it across other dimensions on Twitch. Crates provides additional value to viewers engaging on Twitch, as well as more interesting and unique ways for Broadcasters, Game Developers and other influencers to reach their audience and monetize their content. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible Web application software. You are a full stack developer who is comfortable with Javascript",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Twitch Crates",
          "og:description": "Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing \u201cgig economy\u201d which allows these creators to earn part or all of their income by producing high quality content on Twitch. Twitch Crates was introduced earlier this year as part of our Game Commerce strategy and we are looking for engineers who want to take it to the next level and scale it across other dimensions on Twitch. Crates provides additional value to viewers engaging on Twitch, as well as more interesting and unique ways for Broadcasters, Game Developers and other influencers to reach their audience and monetize their content. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible Web application software. You are a full stack developer who is comfortable with Javascript",
          "og:url": "https://jobs.lever.co/twitch/4a17fcc9-b8da-4716-9e34-78663265b4f9",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Identity",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Identity",
    "link": "https://jobs.lever.co/twitch/9ef94e2c-40db-4cff-aa5a-5b7c5e9bf230/apply",
    "displayLink": "jobs.lever.co",
    "snippet": "7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\u00a0...",
    "htmlSnippet": "7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...",
    "cacheId": "rFNbmPXcN4UJ",
    "formattedUrl": "https://jobs.lever.co/twitch/9ef94e2c-40db-4cff-aa5a.../apply",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/9ef94e2c-40db-4cff-aa5a.../apply",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Identity",
          "twitter:description": "We are looking for a Full Stack software developer to join the Identity Team at Twitch. We\u2019re building OAuth solutions for our community to make a Twitch Identity the last identity you\u2019ll ever need. This is a technical role that builds heavily on internet standards for authorization and authentication on the Twitch site and our OAuth enabled partners. Our products are highly scalable and highly available world wide. As we level up our architecture and features, you\u2019ll have the opportunity to influence design decisions, tooling choices, and every last detail that makes us the best product we can be.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Identity",
          "og:description": "We are looking for a Full Stack software developer to join the Identity Team at Twitch. We\u2019re building OAuth solutions for our community to make a Twitch Identity the last identity you\u2019ll ever need. This is a technical role that builds heavily on internet standards for authorization and authentication on the Twitch site and our OAuth enabled partners. Our products are highly scalable and highly available world wide. As we level up our architecture and features, you\u2019ll have the opportunity to influence design decisions, tooling choices, and every last detail that makes us the best product we can be.",
          "og:url": "https://jobs.lever.co/twitch/9ef94e2c-40db-4cff-aa5a-5b7c5e9bf230/apply",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Software Engineer, Mac",
    "htmlTitle": "Twitch - <b>Software Engineer</b>, Mac",
    "link": "https://jobs.lever.co/twitch/4bf8046f-aab3-4151-a6e0-d21ec251f38e",
    "displayLink": "jobs.lever.co",
    "snippet": "Mac is an important piece of our desktop application strategy. As a software \nengineer, you'll be working on the Twitch Desktop Application for the Mac \nplatform.",
    "htmlSnippet": "Mac is an important piece of our desktop application strategy. As a <b>software</b> <br>\n<b>engineer</b>, you&#39;ll be working on the Twitch Desktop Application for the Mac <br>\nplatform.",
    "cacheId": "r9cbDeiOJ5wJ",
    "formattedUrl": "https://jobs.lever.co/twitch/4bf8046f-aab3-4151-a6e0-d21ec251f38e",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/4bf8046f-aab3-4151-a6e0-d21ec251f38e",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Software Engineer, Mac",
          "twitter:description": "We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Mac is an important piece of our desktop application strategy. As a software engineer, you\u2019ll be working on the Twitch Desktop Application for the Mac platform.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Software Engineer, Mac",
          "og:description": "We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Mac is an important piece of our desktop application strategy. As a software engineer, you\u2019ll be working on the Twitch Desktop Application for the Mac platform.",
          "og:url": "https://jobs.lever.co/twitch/4bf8046f-aab3-4151-a6e0-d21ec251f38e",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "512",
          "og:image:width": "1024"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Subscriptions",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Subscriptions",
    "link": "https://jobs.lever.co/twitch/4d961614-d40d-4c70-b6cb-246a540901d4",
    "displayLink": "jobs.lever.co",
    "snippet": "Twitch is building the future of interactive entertainment and our Commerce \nengineering team builds key services which allow thousands of creative\u00a0...",
    "htmlSnippet": "Twitch is building the future of interactive entertainment and our Commerce <br>\n<b>engineering</b> team builds key services which allow thousands of creative&nbsp;...",
    "cacheId": "Rjw75Dg2q2YJ",
    "formattedUrl": "https://jobs.lever.co/.../4d961614-d40d-4c70-b6cb-246a540901d4",
    "htmlFormattedUrl": "https://jobs.lever.co/.../4d961614-d40d-4c70-b6cb-246a540901d4",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Subscriptions",
          "twitter:description": "Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing \u201cgig economy\u201d which allows these creators to earn part or all of their income by producing high quality content on Twitch. Our San Francisco office is focused on exciting new e-commerce initiatives in 2017! We\u2019re looking for engineers that love delighting people with incredible products and user experiences such as our Subscriptions for Affiliates feature released on June 28th, 2017 which allows thousands of streamers to receive subscribers to their channels. On the Commerce team, you\u2019ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible W",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Subscriptions",
          "og:description": "Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing \u201cgig economy\u201d which allows these creators to earn part or all of their income by producing high quality content on Twitch. Our San Francisco office is focused on exciting new e-commerce initiatives in 2017! We\u2019re looking for engineers that love delighting people with incredible products and user experiences such as our Subscriptions for Affiliates feature released on June 28th, 2017 which allows thousands of streamers to receive subscribers to their channels. On the Commerce team, you\u2019ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible W",
          "og:url": "https://jobs.lever.co/twitch/4d961614-d40d-4c70-b6cb-246a540901d4",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Discovery",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Discovery",
    "link": "https://jobs.lever.co/twitch/4ca38bac-3695-4504-ac6d-cea7cdbd0a85",
    "displayLink": "jobs.lever.co",
    "snippet": "We are looking for a software engineer to contribute to key product roadmap \nitems, recommendations, search and machine learning infrastructure, internal\u00a0...",
    "htmlSnippet": "We are looking for a <b>software engineer</b> to contribute to key product roadmap <br>\nitems, recommendations, search and machine learning infrastructure, internal&nbsp;...",
    "cacheId": "v8uGvJqnQFkJ",
    "formattedUrl": "https://jobs.lever.co/twitch/4ca38bac-3695-4504-ac6d-cea7cdbd0a85",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/4ca38bac-3695-4504-ac6d-cea7cdbd0a85",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Discovery",
          "twitter:description": "Twitch has over 100 million users, and the Metadata, Recommendations, and Search team is responsible for building products that improve the discovery experience for both viewers and broadcasters. We are looking for a software engineer to contribute to key product roadmap items, recommendations, search and machine learning infrastructure, internal machine learning tools. You will have the opportunity to develop and work on high-profile elements of the Twitch architecture and help create large scale distributed systems. You will be working with other highly motivated team members on building next generation recommendation and search systems at scale, using cutting edge ML/AI algorithms. You will develop services to run on Amazon's cloud computing infrastructure (AWS) and have opportunities to interact with teams inside and outside the organization as well as work on a variety of challenging problems.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Discovery",
          "og:description": "Twitch has over 100 million users, and the Metadata, Recommendations, and Search team is responsible for building products that improve the discovery experience for both viewers and broadcasters. We are looking for a software engineer to contribute to key product roadmap items, recommendations, search and machine learning infrastructure, internal machine learning tools. You will have the opportunity to develop and work on high-profile elements of the Twitch architecture and help create large scale distributed systems. You will be working with other highly motivated team members on building next generation recommendation and search systems at scale, using cutting edge ML/AI algorithms. You will develop services to run on Amazon's cloud computing infrastructure (AWS) and have opportunities to interact with teams inside and outside the organization as well as work on a variety of challenging problems.",
          "og:url": "https://jobs.lever.co/twitch/4ca38bac-3695-4504-ac6d-cea7cdbd0a85",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Store",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Store",
    "link": "https://jobs.lever.co/twitch/6b7d7126-c77f-49c8-8ded-f19dce3c13aa",
    "displayLink": "jobs.lever.co",
    "snippet": "We are looking for mid to senior Software Development Engineer who want to \ntake our Commerce experiences to the next level and scale it across other\u00a0...",
    "htmlSnippet": "We are looking for mid to senior <b>Software</b> Development <b>Engineer</b> who want to <br>\ntake our Commerce experiences to the next level and scale it across other&nbsp;...",
    "cacheId": "16SDrFIXoHAJ",
    "formattedUrl": "https://jobs.lever.co/twitch/6b7d7126-c77f-49c8-8ded-f19dce3c13aa",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/6b7d7126-c77f-49c8-8ded-f19dce3c13aa",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Store",
          "twitter:description": "Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing \u201cgig economy\u201d which allows these creators to earn part or all of their income by producing high quality content on Twitch. As an early joiner of the team you will, provide creative input into brand direction and drive high visibility projects across a number of commerce teams. We are looking for mid to senior Software Development Engineer who want to take our Commerce experiences to the next level and scale it across other dimensions on Twitch. The ideal candidate has strong organizational skills, web expertise, and acute attention to detail. They will have developed a deep technical understanding of the strengths and weaknesses of delivery platforms, and are able to identify opportunities and to work creatively within the cons",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Store",
          "og:description": "Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing \u201cgig economy\u201d which allows these creators to earn part or all of their income by producing high quality content on Twitch. As an early joiner of the team you will, provide creative input into brand direction and drive high visibility projects across a number of commerce teams. We are looking for mid to senior Software Development Engineer who want to take our Commerce experiences to the next level and scale it across other dimensions on Twitch. The ideal candidate has strong organizational skills, web expertise, and acute attention to detail. They will have developed a deep technical understanding of the strengths and weaknesses of delivery platforms, and are able to identify opportunities and to work creatively within the cons",
          "og:url": "https://jobs.lever.co/twitch/6b7d7126-c77f-49c8-8ded-f19dce3c13aa",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Software Engineer - Console Apps",
    "htmlTitle": "Twitch - <b>Software Engineer</b> - Console Apps",
    "link": "https://jobs.lever.co/twitch/a0a99d06-bd2a-4ea1-8df1-f2d3705c7c6b",
    "displayLink": "jobs.lever.co",
    "snippet": "The Client Applications team is responsible for developing Twitch's client \napplications on a wide variety of target platforms, including gaming consoles, \nmobile\u00a0...",
    "htmlSnippet": "The Client Applications team is responsible for developing Twitch&#39;s client <br>\napplications on a wide variety of target platforms, including gaming consoles, <br>\nmobile&nbsp;...",
    "cacheId": "6XSKNYvf33cJ",
    "formattedUrl": "https://jobs.lever.co/twitch/a0a99d06-bd2a-4ea1-8df1-f2d3705c7c6b",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/a0a99d06-bd2a-4ea1-8df1-f2d3705c7c6b",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Software Engineer - Console Apps",
          "twitter:description": "The Client Applications team is responsible for developing Twitch\u2019s client applications on a wide variety of target platforms, including gaming consoles, mobile devices, smart TVs, set-top boxes, and other current and future video platforms (e.g. VR). As an Application Engineer, you will be using a variety of frameworks and languages to bring a great Twitch experience to each platform.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Software Engineer - Console Apps",
          "og:description": "The Client Applications team is responsible for developing Twitch\u2019s client applications on a wide variety of target platforms, including gaming consoles, mobile devices, smart TVs, set-top boxes, and other current and future video platforms (e.g. VR). As an Application Engineer, you will be using a variety of frameworks and languages to bring a great Twitch experience to each platform.",
          "og:url": "https://jobs.lever.co/twitch/a0a99d06-bd2a-4ea1-8df1-f2d3705c7c6b",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Video Player",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Video Player",
    "link": "https://jobs.lever.co/twitch/65b04ed0-7b51-4be5-b81f-17a2d794a381",
    "displayLink": "jobs.lever.co",
    "snippet": "Twitch has over 100 million users, and the Playback Technologies team is \nresponsible for helping them connect with content they love on both live and \nrecorded\u00a0...",
    "htmlSnippet": "Twitch has over 100 million users, and the Playback Technologies team is <br>\nresponsible for helping them connect with content they love on both live and <br>\nrecorded&nbsp;...",
    "cacheId": "yLUp9kTcwxwJ",
    "formattedUrl": "https://jobs.lever.co/.../65b04ed0-7b51-4be5-b81f-17a2d794a381",
    "htmlFormattedUrl": "https://jobs.lever.co/.../65b04ed0-7b51-4be5-b81f-17a2d794a381",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Video Player",
          "twitter:description": "Twitch has over 100 million users, and the Playback Technologies team is responsible for helping them connect with content they love on both live and recorded video. We\u2019re building a number of features to make Twitch the most compelling destination for gaming video this year. Recently, we launched Clips and our HTML5 Video Player, and we\u2019re just getting started. We\u2019re looking for engineers that love delighting people with incredible products and user experiences. You\u2019ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in programming for the Web (including an understanding of modern JS tooling and cross-browser compatibility issues) and sensibilities for design and UX.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Video Player",
          "og:description": "Twitch has over 100 million users, and the Playback Technologies team is responsible for helping them connect with content they love on both live and recorded video. We\u2019re building a number of features to make Twitch the most compelling destination for gaming video this year. Recently, we launched Clips and our HTML5 Video Player, and we\u2019re just getting started. We\u2019re looking for engineers that love delighting people with incredible products and user experiences. You\u2019ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in programming for the Web (including an understanding of modern JS tooling and cross-browser compatibility issues) and sensibilities for design and UX.",
          "og:url": "https://jobs.lever.co/twitch/65b04ed0-7b51-4be5-b81f-17a2d794a381",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Social Products",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Social Products",
    "link": "https://jobs.lever.co/twitch/cc6d80b0-93a4-4e59-bb25-3377e4a90413",
    "displayLink": "jobs.lever.co",
    "snippet": "The Community Success organization is responsible for building the products \nthat allow Twitch users to discover, communicate and keep in touch with over\u00a0...",
    "htmlSnippet": "The Community Success organization is responsible for building the products <br>\nthat allow Twitch users to discover, communicate and keep in touch with over&nbsp;...",
    "cacheId": "vRmmPpP1Hd4J",
    "formattedUrl": "https://jobs.lever.co/.../cc6d80b0-93a4-4e59-bb25-3377e4a90413",
    "htmlFormattedUrl": "https://jobs.lever.co/.../cc6d80b0-93a4-4e59-bb25-3377e4a90413",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Social Products",
          "twitter:description": "The Community Success organization is responsible for building the products that allow Twitch users to discover, communicate and keep in touch with over 100M Twitch users and broadcasters. We're focused on building features that keep users coming back to Twitch such as chat, whispers, feeds, and notifications, as well as game directories, communities, and other features to help Twitch broadcasters get discovered.We're looking for engineers that want to help the Twitch community. In this organization, you'll work alongside product, data science, and design to craft scalable, fault-tolerant backend systems and seamless front-end user experiences. If you want to help build the future of gaming-related discovery and interaction, you should join us!",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Social Products",
          "og:description": "The Community Success organization is responsible for building the products that allow Twitch users to discover, communicate and keep in touch with over 100M Twitch users and broadcasters. We're focused on building features that keep users coming back to Twitch such as chat, whispers, feeds, and notifications, as well as game directories, communities, and other features to help Twitch broadcasters get discovered.We're looking for engineers that want to help the Twitch community. In this organization, you'll work alongside product, data science, and design to craft scalable, fault-tolerant backend systems and seamless front-end user experiences. If you want to help build the future of gaming-related discovery and interaction, you should join us!",
          "og:url": "https://jobs.lever.co/twitch/cc6d80b0-93a4-4e59-bb25-3377e4a90413",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Staff Software Engineer in Test",
    "htmlTitle": "Twitch - Staff <b>Software Engineer</b> in Test",
    "link": "https://jobs.lever.co/twitch/62c5b544-93ec-4c8e-b7ef-6e27dc7a7688/apply",
    "displayLink": "jobs.lever.co",
    "snippet": "7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\u00a0...",
    "htmlSnippet": "7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...",
    "cacheId": "rRWgFfSc_ZAJ",
    "formattedUrl": "https://jobs.lever.co/twitch/62c5b544-93ec-4c8e-b7ef.../apply",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/62c5b544-93ec-4c8e-b7ef.../apply",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Staff Software Engineer in Test",
          "twitter:description": "Twitch is looking for an experienced Software Engineer in Test for the Developer Success Product Team. As a Staff Software Engineer in Test, you will be responsible for driving quality initiatives within the Business Unit. You will work with several teams and help them to write more automated tests and help in improving our product quality levels. The successful candidate will have excellent attention to detail with proven abilities in developing test tools and test frameworks.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Staff Software Engineer in Test",
          "og:description": "Twitch is looking for an experienced Software Engineer in Test for the Developer Success Product Team. As a Staff Software Engineer in Test, you will be responsible for driving quality initiatives within the Business Unit. You will work with several teams and help them to write more automated tests and help in improving our product quality levels. The successful candidate will have excellent attention to detail with proven abilities in developing test tools and test frameworks.",
          "og:url": "https://jobs.lever.co/twitch/62c5b544-93ec-4c8e-b7ef-6e27dc7a7688/apply",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Software Engineer - Social Products",
    "htmlTitle": "Twitch - <b>Software Engineer</b> - Social Products",
    "link": "https://jobs.lever.co/twitch/e7d578a7-bc4d-4a0c-bca7-b75ddf3598fa",
    "displayLink": "jobs.lever.co",
    "snippet": "The Community Success organization is responsible for building the products \nthat allow Twitch users to discover, communicate and keep in touch with over\u00a0...",
    "htmlSnippet": "The Community Success organization is responsible for building the products <br>\nthat allow Twitch users to discover, communicate and keep in touch with over&nbsp;...",
    "cacheId": "el5Y0DE5sxAJ",
    "formattedUrl": "https://jobs.lever.co/twitch/e7d578a7-bc4d-4a0c-bca7-b75ddf3598fa",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/e7d578a7-bc4d-4a0c-bca7-b75ddf3598fa",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Software Engineer - Social Products",
          "twitter:description": "The Community Success organization is responsible for building the products that allow Twitch users to discover, communicate and keep in touch with over 100M Twitch users and broadcasters. We're focused on building features that keep users coming back to Twitch such as chat, whispers, feeds, and notifications, as well as game directories, communities, and other features to help Twitch broadcasters get discovered.We're looking for engineers that want to help the Twitch community. In this organization, you'll work alongside product, data science, and design to craft scalable, fault-tolerant backend systems and seamless front-end user experiences. If you want to help build the future of gaming-related discovery and interaction, you should join us!",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Software Engineer - Social Products",
          "og:description": "The Community Success organization is responsible for building the products that allow Twitch users to discover, communicate and keep in touch with over 100M Twitch users and broadcasters. We're focused on building features that keep users coming back to Twitch such as chat, whispers, feeds, and notifications, as well as game directories, communities, and other features to help Twitch broadcasters get discovered.We're looking for engineers that want to help the Twitch community. In this organization, you'll work alongside product, data science, and design to craft scalable, fault-tolerant backend systems and seamless front-end user experiences. If you want to help build the future of gaming-related discovery and interaction, you should join us!",
          "og:url": "https://jobs.lever.co/twitch/e7d578a7-bc4d-4a0c-bca7-b75ddf3598fa",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Software Engineer - Mobile",
    "htmlTitle": "Twitch - <b>Software Engineer</b> - Mobile",
    "link": "https://jobs.lever.co/twitch/1dc7696f-0fab-4c11-8229-dd15dd7d42c0/apply",
    "displayLink": "jobs.lever.co",
    "snippet": "7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\u00a0...",
    "htmlSnippet": "7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...",
    "cacheId": "JbWsEv73rMsJ",
    "formattedUrl": "https://jobs.lever.co/twitch/1dc7696f-0fab-4c11-8229.../apply",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/1dc7696f-0fab-4c11-8229.../apply",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Software Engineer - Mobile",
          "twitter:description": "Twitch\u2019s Mobile Engineering team is responsible for developing our native applications for the Android and iOS platforms, supporting phone, tablet and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As a Senior Engineer on the Mobile team, you will provide technical leadership and make direct contributions to apps that are the portal to the Twitch community for millions of users.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Software Engineer - Mobile",
          "og:description": "Twitch\u2019s Mobile Engineering team is responsible for developing our native applications for the Android and iOS platforms, supporting phone, tablet and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As a Senior Engineer on the Mobile team, you will provide technical leadership and make direct contributions to apps that are the portal to the Twitch community for millions of users.",
          "og:url": "https://jobs.lever.co/twitch/1dc7696f-0fab-4c11-8229-dd15dd7d42c0/apply",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Software Engineer - Commerce",
    "htmlTitle": "Twitch - Senior <b>Software Engineer</b> - Commerce",
    "link": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf/apply",
    "displayLink": "jobs.lever.co",
    "snippet": "7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\u00a0...",
    "htmlSnippet": "7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...",
    "cacheId": "XPs8wLpaX38J",
    "formattedUrl": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0.../apply",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0.../apply",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Software Engineer - Commerce",
          "twitter:description": "Twitch is building the future of interactive entertainment, and our windows client engineering team is growing in order to execute on a brand new, secret project. We\u2019re looking for engineers that love solving hard technical problems related to gaming on PCs and Twitch. This project will require innovation and the ability to come up with technical solutions in new spaces. You will also need to work with and be able to think like a game developer. We\u2019re working with top developers to help bring new experiences to customers. We\u2019re using a variety of tools and languages, but much of our work will be in C++, so you\u2019ll have to be willing to roll up your sleeves and get your hands dirty. You\u2019ll have to write a lot of code, but should also be able to mentor engineers around you and do whatever needs to be done for the team and product initiative to succeed.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Software Engineer - Commerce",
          "og:description": "Twitch is building the future of interactive entertainment, and our windows client engineering team is growing in order to execute on a brand new, secret project. We\u2019re looking for engineers that love solving hard technical problems related to gaming on PCs and Twitch. This project will require innovation and the ability to come up with technical solutions in new spaces. You will also need to work with and be able to think like a game developer. We\u2019re working with top developers to help bring new experiences to customers. We\u2019re using a variety of tools and languages, but much of our work will be in C++, so you\u2019ll have to be willing to roll up your sleeves and get your hands dirty. You\u2019ll have to write a lot of code, but should also be able to mentor engineers around you and do whatever needs to be done for the team and product initiative to succeed.",
          "og:url": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf/apply",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Software Engineer - Client Platform",
    "htmlTitle": "Twitch - <b>Software Engineer</b> - Client Platform",
    "link": "https://jobs.lever.co/twitch/9df290d0-faa9-4fab-a888-9278d1f7f728/apply",
    "displayLink": "jobs.lever.co",
    "snippet": "7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\u00a0...",
    "htmlSnippet": "7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...",
    "cacheId": "ujUMmBxq8zYJ",
    "formattedUrl": "https://jobs.lever.co/twitch/9df290d0-faa9-4fab-a888.../apply",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/9df290d0-faa9-4fab-a888.../apply",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Software Engineer - Client Platform",
          "twitter:description": "How do we take millions of content creators, connect them with tens of millions of viewers, on a platform that is second to none? It starts with welcoming everyone but choosing only the best. It's the willingness to experiment to decide, and about commitment, not compliance. These are just a few of the driving principles behind the Twitch IT organization. The Client Platform team is a hybrid software/systems group that ensures Twitch\u2019s employees have the systems they need to be highly productive. The team works cross-functionally with every business unit to provide solutions to a wide variety of business needs. To be successful, engineers require a comprehensive understanding of a wide range of operating systems, automation technologies, and coding combined with the capability to leverage them to create unique and innovative solutions. If you are a candidate that has broad skills across multiple operating systems and thrive on the ability to develop leading-edge innovative solution",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Software Engineer - Client Platform",
          "og:description": "How do we take millions of content creators, connect them with tens of millions of viewers, on a platform that is second to none? It starts with welcoming everyone but choosing only the best. It's the willingness to experiment to decide, and about commitment, not compliance. These are just a few of the driving principles behind the Twitch IT organization. The Client Platform team is a hybrid software/systems group that ensures Twitch\u2019s employees have the systems they need to be highly productive. The team works cross-functionally with every business unit to provide solutions to a wide variety of business needs. To be successful, engineers require a comprehensive understanding of a wide range of operating systems, automation technologies, and coding combined with the capability to leverage them to create unique and innovative solutions. If you are a candidate that has broad skills across multiple operating systems and thrive on the ability to develop leading-edge innovative solution",
          "og:url": "https://jobs.lever.co/twitch/9df290d0-faa9-4fab-a888-9278d1f7f728/apply",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Backend Software Engineer- Developer Success",
    "htmlTitle": "Twitch - Backend <b>Software Engineer</b>- Developer Success",
    "link": "https://jobs.lever.co/twitch/1fe36347-5bc9-4620-9273-9f93554717e4?lever-source=stackshare.io/match",
    "displayLink": "jobs.lever.co",
    "snippet": "Twitch seeks a talented back end software engineer to help us create features for \nthousands of game developers building the next generation of games.",
    "htmlSnippet": "Twitch seeks a talented back end <b>software engineer</b> to help us create features for <br>\nthousands of game developers building the next generation of games.",
    "cacheId": "1FjDukRruCAJ",
    "formattedUrl": "https://jobs.lever.co/.../1fe36347-5bc9-4620-9273-9f93554717e4?...",
    "htmlFormattedUrl": "https://jobs.lever.co/.../1fe36347-5bc9-4620-9273-9f93554717e4?...",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Backend Software Engineer- Developer Success",
          "twitter:description": "Twitch seeks a talented back end software engineer to help us create features for thousands of game developers building the next generation of games. Your first project will be experienced by millions.  You will help set the foundation and execute on the construction of back end services and web apps. You have an instinct for code quality and a passion for craftsmanship. You thrive on rapid learning, the opportunity for innovation, and collaborating with top flight team members.  The Developer Success team helps creators, from the world\u2019s top game companies to amazing indie teams, present their products to viewers who may like them, engage with their existing users, and find innovative new ways to generate revenue. With your help we will delight developers and shape the landscape of the gaming industry.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Backend Software Engineer- Developer Success",
          "og:description": "Twitch seeks a talented back end software engineer to help us create features for thousands of game developers building the next generation of games. Your first project will be experienced by millions.  You will help set the foundation and execute on the construction of back end services and web apps. You have an instinct for code quality and a passion for craftsmanship. You thrive on rapid learning, the opportunity for innovation, and collaborating with top flight team members.  The Developer Success team helps creators, from the world\u2019s top game companies to amazing indie teams, present their products to viewers who may like them, engage with their existing users, and find innovative new ways to generate revenue. With your help we will delight developers and shape the landscape of the gaming industry.",
          "og:url": "https://jobs.lever.co/twitch/1fe36347-5bc9-4620-9273-9f93554717e4",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "512",
          "og:image:width": "1024"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Software Engineer - Data",
    "htmlTitle": "Twitch - <b>Software Engineer</b> - Data",
    "link": "https://jobs.lever.co/twitch/889401a7-d917-4947-97d7-8a2d2e2fd430/apply?lever-source=themuse",
    "displayLink": "jobs.lever.co",
    "snippet": "7) If you answered yes to Question 5 above, for the purposes of determining \nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent\u00a0...",
    "htmlSnippet": "7) If you answered yes to Question 5 above, for the purposes of determining <br>\nexport licensing requirements, if you are not a U.S. citizen, a U.S. permanent&nbsp;...",
    "cacheId": "FTyrTOuPX8EJ",
    "formattedUrl": "https://jobs.lever.co/twitch/889401a7-d917-4947-97d7.../apply?...",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/889401a7-d917-4947-97d7.../apply?...",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Software Engineer - Data",
          "twitter:description": "Twitch is building the future of interactive entertainment, and data is critical to every decision we make. The Science Engineering team is looking for a developer to help us meet all the diverse data needs within Twitch and to scale with those needs. Our team develops and operates the real-time behavioral data pipeline, which collects, processes, and distributes data to other teams. We provide data to systems and decision making throughout the company, and we have a constantly growing list of data consumers. The core pipeline is open source -- check out our code at github.com/twitchscience",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Software Engineer - Data",
          "og:description": "Twitch is building the future of interactive entertainment, and data is critical to every decision we make. The Science Engineering team is looking for a developer to help us meet all the diverse data needs within Twitch and to scale with those needs. Our team develops and operates the real-time behavioral data pipeline, which collects, processes, and distributes data to other teams. We provide data to systems and decision making throughout the company, and we have a constantly growing list of data consumers. The core pipeline is open source -- check out our code at github.com/twitchscience",
          "og:url": "https://jobs.lever.co/twitch/889401a7-d917-4947-97d7-8a2d2e2fd430/apply",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Quality Engineer - Core Payments",
    "htmlTitle": "Twitch - Senior Quality <b>Engineer</b> - Core Payments",
    "link": "https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31",
    "displayLink": "jobs.lever.co",
    "snippet": "As a Senior Software Engineer in Test for Core Payments team, you will be \nworking closely with development and various other cross-functional teams to \nensure\u00a0...",
    "htmlSnippet": "As a Senior <b>Software Engineer</b> in Test for Core Payments team, you will be <br>\nworking closely with development and various other cross-functional teams to <br>\nensure&nbsp;...",
    "cacheId": "ujXW9reMdCoJ",
    "formattedUrl": "https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Quality Engineer - Core Payments",
          "twitter:description": "Core Payments team owns product/systems that affect millions of users and broadcasters. Our platforms enable automated onboarding as well as payments processing so its role is essential for the company. The teams are directly responsible in ensuring high quality world class payments experiences for our users. As a Senior Software Engineer in Test for Core Payments team, you will be working closely with development and various other cross-functional teams to ensure the highest quality for our projects.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Quality Engineer - Core Payments",
          "og:description": "Core Payments team owns product/systems that affect millions of users and broadcasters. Our platforms enable automated onboarding as well as payments processing so its role is essential for the company. The teams are directly responsible in ensuring high quality world class payments experiences for our users. As a Senior Software Engineer in Test for Core Payments team, you will be working closely with development and various other cross-functional teams to ensure the highest quality for our projects.",
          "og:url": "https://jobs.lever.co/twitch/8da109ec-2bdb-4f62-802d-f5c1914f3f31",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - iOS Engineer",
    "htmlTitle": "Twitch - iOS <b>Engineer</b>",
    "link": "https://jobs.lever.co/twitch/5777f110-4e1f-4dbd-85dc-219187e9caae",
    "displayLink": "jobs.lever.co",
    "snippet": "As an iOS Software Engineer, you will make major contributions to a rapidly-\nevolving, native app that is a portal to the Twitch community for millions of users.",
    "htmlSnippet": "As an iOS <b>Software Engineer</b>, you will make major contributions to a rapidly-<br>\nevolving, native app that is a portal to the Twitch community for millions of users.",
    "cacheId": "D-LQ1zCdz1QJ",
    "formattedUrl": "https://jobs.lever.co/twitch/5777f110-4e1f-4dbd-85dc-219187e9caae",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/5777f110-4e1f-4dbd-85dc-219187e9caae",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - iOS Engineer",
          "twitter:description": "Twitch\u2019s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As an iOS Software Engineer, you will make major contributions to a rapidly-evolving, native app that is a portal to the Twitch community for millions of users.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - iOS Engineer",
          "og:description": "Twitch\u2019s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As an iOS Software Engineer, you will make major contributions to a rapidly-evolving, native app that is a portal to the Twitch community for millions of users.",
          "og:url": "https://jobs.lever.co/twitch/5777f110-4e1f-4dbd-85dc-219187e9caae",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch",
    "htmlTitle": "Twitch",
    "link": "https://jobs.lever.co/twitch",
    "displayLink": "jobs.lever.co",
    "snippet": "Senior Software Engineer - VOD. San Francisco, CABroadcaster Success \u2013 \nVideo on DemandFull-time. Business & Corporate Development. Strategic \nPartner\u00a0...",
    "htmlSnippet": "Senior <b>Software Engineer</b> - VOD. San Francisco, CABroadcaster Success \u2013 <br>\nVideo on DemandFull-time. Business &amp; Corporate Development. Strategic <br>\nPartner&nbsp;...",
    "cacheId": "JODhjGiGRxAJ",
    "formattedUrl": "https://jobs.lever.co/twitch",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch",
          "twitter:description": "Job openings at Twitch",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch jobs",
          "og:description": "Job openings at Twitch",
          "og:url": "https://jobs.lever.co/twitch",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior iOS Engineer",
    "htmlTitle": "Twitch - Senior iOS <b>Engineer</b>",
    "link": "https://jobs.lever.co/twitch/1a5a24ed-4bed-43f4-8774-195bf28f0cbd",
    "displayLink": "jobs.lever.co",
    "snippet": "As a Senior iOS Software Engineer, you will provide technical leadership and \nmake direct contributions to an app that is the portal to the Twitch community for\u00a0...",
    "htmlSnippet": "As a Senior iOS <b>Software Engineer</b>, you will provide technical leadership and <br>\nmake direct contributions to an app that is the portal to the Twitch community for&nbsp;...",
    "cacheId": "xiBSutZWP9IJ",
    "formattedUrl": "https://jobs.lever.co/twitch/1a5a24ed-4bed-43f4-8774-195bf28f0cbd",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/1a5a24ed-4bed-43f4-8774-195bf28f0cbd",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior iOS Engineer",
          "twitter:description": "Twitch\u2019s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet, and set-top devices. These platforms represent an ever-growing share of Twitch viewership, and providing functional and delightful experiences on them is essential to user engagement. As a Senior iOS Software Engineer, you will provide technical leadership and make direct contributions to an app that is the portal to the Twitch community for millions of users.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior iOS Engineer",
          "og:description": "Twitch\u2019s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet, and set-top devices. These platforms represent an ever-growing share of Twitch viewership, and providing functional and delightful experiences on them is essential to user engagement. As a Senior iOS Software Engineer, you will provide technical leadership and make direct contributions to an app that is the portal to the Twitch community for millions of users.",
          "og:url": "https://jobs.lever.co/twitch/1a5a24ed-4bed-43f4-8774-195bf28f0cbd",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Distributed Systems Engineer",
    "htmlTitle": "Twitch - Distributed Systems <b>Engineer</b>",
    "link": "https://jobs.lever.co/twitch/8929e219-138d-473c-8acd-4fcc3e01fc0a",
    "displayLink": "jobs.lever.co",
    "snippet": "We are looking for engineers who are excited by the thought of working across \nthe ... working in a professional software engineering environment (with source\u00a0...",
    "htmlSnippet": "We are looking for engineers who are excited by the thought of working across <br>\nthe ... working in a professional <b>software engineering</b> environment (with source&nbsp;...",
    "cacheId": "2WyXXOrIqOYJ",
    "formattedUrl": "https://jobs.lever.co/twitch/8929e219-138d-473c-8acd-4fcc3e01fc0a",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/8929e219-138d-473c-8acd-4fcc3e01fc0a",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Distributed Systems Engineer",
          "twitter:description": "Twitch is building the future of interactive entertainment. Ensuring smooth, low-latency video across the world requires large-scale, fault-tolerant systems that can keep up with millions of simultaneous viewers and thousands of broadcasters. We are looking for engineers who are excited by the thought of working across the entire stack, from service load-balancing, to performance optimization, to backbone traffic management. You will help architect, develop, test, deploy, operate, and maintain our video software software. As part of the team, we will work together to enable our broadcasters and viewers to create and interact in new, innovative ways.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Distributed Systems Engineer",
          "og:description": "Twitch is building the future of interactive entertainment. Ensuring smooth, low-latency video across the world requires large-scale, fault-tolerant systems that can keep up with millions of simultaneous viewers and thousands of broadcasters. We are looking for engineers who are excited by the thought of working across the entire stack, from service load-balancing, to performance optimization, to backbone traffic management. You will help architect, develop, test, deploy, operate, and maintain our video software software. As part of the team, we will work together to enable our broadcasters and viewers to create and interact in new, innovative ways.",
          "og:url": "https://jobs.lever.co/twitch/8929e219-138d-473c-8acd-4fcc3e01fc0a",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch",
    "htmlTitle": "Twitch",
    "link": "https://jobs.lever.co/twitch?by=location",
    "displayLink": "jobs.lever.co",
    "snippet": "Senior Software Engineer - Internationalization. Irvine, CAClients Platform & \nProduct Development \u2013 Clients EngineeringFull-time \u00b7 Apply\u00a0...",
    "htmlSnippet": "Senior <b>Software Engineer</b> - Internationalization. Irvine, CAClients Platform &amp; <br>\nProduct Development \u2013 Clients EngineeringFull-time &middot; Apply&nbsp;...",
    "cacheId": "1PL04KCv1NgJ",
    "formattedUrl": "https://jobs.lever.co/twitch?by=location",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch?by=location",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch",
          "twitter:description": "Job openings at Twitch",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch jobs",
          "og:description": "Job openings at Twitch",
          "og:url": "https://jobs.lever.co/twitch",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch",
    "htmlTitle": "Twitch",
    "link": "https://jobs.lever.co/twitch?by=location&location=San%20Francisco%2C%20CA",
    "displayLink": "jobs.lever.co",
    "snippet": "San Francisco, CACommerce \u2013 Developer Product EngineeringFull-time \u00b7 Apply \n... Senior Software Engineer - Global Infrastructure. San Francisco\u00a0...",
    "htmlSnippet": "San Francisco, CACommerce \u2013 Developer Product EngineeringFull-time &middot; Apply <br>\n... Senior <b>Software Engineer</b> - Global Infrastructure. San Francisco&nbsp;...",
    "cacheId": "fBjr9tLpOBgJ",
    "formattedUrl": "https://jobs.lever.co/twitch?by=location&location...",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch?by=location&amp;location...",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch",
          "twitter:description": "Job openings at Twitch",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch jobs",
          "og:description": "Job openings at Twitch",
          "og:url": "https://jobs.lever.co/twitch",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Engineering Manager - Mobile",
    "htmlTitle": "Twitch - <b>Engineering</b> Manager - Mobile",
    "link": "https://jobs.lever.co/twitch/0bfcaf1e-0059-4ed6-b9a7-644a205dad55",
    "displayLink": "jobs.lever.co",
    "snippet": "Twitch's Mobile Engineering team is responsible for developing viewing \napplications ... software development experience; 2+ years experience as \nengineering\u00a0...",
    "htmlSnippet": "Twitch&#39;s Mobile <b>Engineering</b> team is responsible for developing viewing <br>\napplications ... <b>software</b> development experience; 2+ years experience as <br>\n<b>engineering</b>&nbsp;...",
    "cacheId": "Sc7-F37rqz4J",
    "formattedUrl": "https://jobs.lever.co/twitch/0bfcaf1e-0059-4ed6-b9a7-644a205dad55",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/0bfcaf1e-0059-4ed6-b9a7-644a205dad55",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Engineering Manager - Mobile",
          "twitter:description": "Twitch\u2019s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet, and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As an Engineering Manager you\u2019ll help grow our Mobile Engineering team to deliver on our expanding mobile product scope, while maintaining a very high quality and stability bar for the applications.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Engineering Manager - Mobile",
          "og:description": "Twitch\u2019s Mobile Engineering team is responsible for developing viewing applications for the Android and iOS platforms, supporting phone, tablet, and set-top devices. These platforms represent an ever-growing share of Twitch viewership and providing functional and delightful experiences on them is essential to user engagement. As an Engineering Manager you\u2019ll help grow our Mobile Engineering team to deliver on our expanding mobile product scope, while maintaining a very high quality and stability bar for the applications.",
          "og:url": "https://jobs.lever.co/twitch/0bfcaf1e-0059-4ed6-b9a7-644a205dad55",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - IT Support Engineer",
    "htmlTitle": "Twitch - IT Support <b>Engineer</b>",
    "link": "https://jobs.lever.co/twitch/3c9d03da-50b2-452e-9b85-b81760987f81",
    "displayLink": "jobs.lever.co",
    "snippet": "The IT Support engineer will provide hands-on support for client hardware and \nsoftware on Windows, Mac, and Linux systems. They also support networking\u00a0...",
    "htmlSnippet": "The IT Support <b>engineer</b> will provide hands-on support for client hardware and <br>\n<b>software</b> on Windows, Mac, and Linux systems. They also support networking&nbsp;...",
    "cacheId": "riEjFLvBkBwJ",
    "formattedUrl": "https://jobs.lever.co/.../3c9d03da-50b2-452e-9b85-b81760987f81",
    "htmlFormattedUrl": "https://jobs.lever.co/.../3c9d03da-50b2-452e-9b85-b81760987f81",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - IT Support Engineer",
          "twitter:description": "How do we take millions of content creators, connect them with tens of millions of viewers, on a platform that is second to none? It starts with welcoming everyone but choosing only the best. It's the willingness to experiment to decide, and about commitment, not compliance. These are just a few of the driving principles behind the Twitch IT organization. Twitch has an immediate opening for an IT Support Engineer in our San Francisco office. The IT Support Engineer serves as IT Support for Twitch business units and corporate offices within the San Francisco area. The IT Support engineer will provide hands-on support for client hardware and software on Windows, Mac, and Linux systems. They also support networking and local server resources for their site. Regular activities include PC imaging and repair, network troubleshooting, project management, mentor-ship of junior technicians, systems administration in a variety of software and hardware environments, telecom administration, a",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - IT Support Engineer",
          "og:description": "How do we take millions of content creators, connect them with tens of millions of viewers, on a platform that is second to none? It starts with welcoming everyone but choosing only the best. It's the willingness to experiment to decide, and about commitment, not compliance. These are just a few of the driving principles behind the Twitch IT organization. Twitch has an immediate opening for an IT Support Engineer in our San Francisco office. The IT Support Engineer serves as IT Support for Twitch business units and corporate offices within the San Francisco area. The IT Support engineer will provide hands-on support for client hardware and software on Windows, Mac, and Linux systems. They also support networking and local server resources for their site. Regular activities include PC imaging and repair, network troubleshooting, project management, mentor-ship of junior technicians, systems administration in a variety of software and hardware environments, telecom administration, a",
          "og:url": "https://jobs.lever.co/twitch/3c9d03da-50b2-452e-9b85-b81760987f81",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Director of Engineering - Payments Platform",
    "htmlTitle": "Twitch - Senior Director of <b>Engineering</b> - Payments Platform",
    "link": "https://jobs.lever.co/twitch/beef5266-833a-4570-8a7c-79101ad558b3",
    "displayLink": "jobs.lever.co",
    "snippet": "BS in Computer Science or Engineering (or equivalent); Strong technical \ncredentials, with at least 10 years experience managing software development \nteams,\u00a0...",
    "htmlSnippet": "BS in Computer Science or <b>Engineering</b> (or equivalent); Strong technical <br>\ncredentials, with at least 10 years experience managing <b>software</b> development <br>\nteams,&nbsp;...",
    "cacheId": "x9hYjn88feMJ",
    "formattedUrl": "https://jobs.lever.co/.../beef5266-833a-4570-8a7c-79101ad558b3",
    "htmlFormattedUrl": "https://jobs.lever.co/.../beef5266-833a-4570-8a7c-79101ad558b3",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Director of Engineering - Payments Platform",
          "twitter:description": "Twitch is building the future of interactive entertainment and Commerce is ensuring our content creators can make a living doing what they love. The Payments team in Commerce is focused on ensuring our global audience is able to pay in a localized experienced with payment methods that are familiar and accessible and ensuring our tens of thousands of creators are paid accurately, timely, and conveniently. These experiences are the foundation of Twitch\u2019s explosive growth and we are hiring a senior technical leader to lead multiple engineering teams enhancing these capabilities. You will play a leading role in defining the vision for our service and in building a world-class engineering organization to execute to that vision. You will work closely with the individual contributors and managers on your teams, as well as cross-team with engineering, product, operations and business leadership to deliver high visible results. The ideal candidate must have demonstrated ability to build a",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Director of Engineering - Payments Platform",
          "og:description": "Twitch is building the future of interactive entertainment and Commerce is ensuring our content creators can make a living doing what they love. The Payments team in Commerce is focused on ensuring our global audience is able to pay in a localized experienced with payment methods that are familiar and accessible and ensuring our tens of thousands of creators are paid accurately, timely, and conveniently. These experiences are the foundation of Twitch\u2019s explosive growth and we are hiring a senior technical leader to lead multiple engineering teams enhancing these capabilities. You will play a leading role in defining the vision for our service and in building a world-class engineering organization to execute to that vision. You will work closely with the individual contributors and managers on your teams, as well as cross-team with engineering, product, operations and business leadership to deliver high visible results. The ideal candidate must have demonstrated ability to build a",
          "og:url": "https://jobs.lever.co/twitch/beef5266-833a-4570-8a7c-79101ad558b3",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch",
    "htmlTitle": "Twitch",
    "link": "https://jobs.lever.co/twitch?location=Irvine%2C%20CA",
    "displayLink": "jobs.lever.co",
    "snippet": "Frontend Engineer - Browser Clients. Irvine, CAClients Platform & Product ... \nSenior Software Engineer - Internationalization. Irvine, CAClients Platform\u00a0...",
    "htmlSnippet": "Frontend Engineer - Browser Clients. Irvine, CAClients Platform &amp; Product ... <br>\nSenior <b>Software Engineer</b> - Internationalization. Irvine, CAClients Platform&nbsp;...",
    "cacheId": "YwweuHgiZF8J",
    "formattedUrl": "https://jobs.lever.co/twitch?location=Irvine%2C%20CA",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch?location=Irvine%2C%20CA",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch",
          "twitter:description": "Job openings at Twitch",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch jobs",
          "og:description": "Job openings at Twitch",
          "og:url": "https://jobs.lever.co/twitch",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch",
    "htmlTitle": "Twitch",
    "link": "https://jobs.lever.co/twitch?by=location&location=Irvine%2C%20CA",
    "displayLink": "jobs.lever.co",
    "snippet": "... Infrastructure (C#). Irvine, CAClients Platform & Product Development \u2013 Clients \nEngineeringFull-time ... Senior Software Engineer - Internationalization. Irvine\u00a0...",
    "htmlSnippet": "... Infrastructure (C#). Irvine, CAClients Platform &amp; Product Development \u2013 Clients <br>\nEngineeringFull-time ... Senior <b>Software Engineer</b> - Internationalization. Irvine&nbsp;...",
    "cacheId": "__X4k5eEjgEJ",
    "formattedUrl": "https://jobs.lever.co/twitch?by=location&location...",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch?by=location&amp;location...",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch",
          "twitter:description": "Job openings at Twitch",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch jobs",
          "og:description": "Job openings at Twitch",
          "og:url": "https://jobs.lever.co/twitch",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Frontend Engineer - Twitch Crates",
    "htmlTitle": "Twitch - Frontend <b>Engineer</b> - Twitch Crates",
    "link": "https://jobs.lever.co/twitch/7f6218d3-ca90-4daf-abfe-cd693a5ad76b",
    "displayLink": "jobs.lever.co",
    "snippet": "This role is perfect for an engineer who has a passion for building high quality, \nreliable, extensible Web application software. You are passionate about best\u00a0...",
    "htmlSnippet": "This role is perfect for an <b>engineer</b> who has a passion for building high quality, <br>\nreliable, extensible Web application <b>software</b>. You are passionate about best&nbsp;...",
    "cacheId": "YgRjcZC4EQwJ",
    "formattedUrl": "https://jobs.lever.co/twitch/7f6218d3-ca90-4daf-abfe-cd693a5ad76b",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/7f6218d3-ca90-4daf-abfe-cd693a5ad76b",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Frontend Engineer - Twitch Crates",
          "twitter:description": "Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing \u201cgig economy\u201d which allows these creators to earn part or all of their income by producing high quality content on Twitch. Twitch Crates was introduced earlier this year as part of our Game Commerce strategy and we are looking for engineers who want to take it to the next level and scale it across other dimensions on Twitch. Crates provides additional value to viewers engaging on Twitch, as well as more interesting and unique ways for Broadcasters, Game Developers and other influencers to reach their audience and monetize their content. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible Web application software. You are passionate about best practices and comfortable with Jav",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Frontend Engineer - Twitch Crates",
          "og:description": "Twitch is building the future of interactive entertainment and our Commerce engineering team builds key services which allow thousands of creative broadcasters to monetize among the millions of Twitch viewers. Our work is at the center of the rapidly growing \u201cgig economy\u201d which allows these creators to earn part or all of their income by producing high quality content on Twitch. Twitch Crates was introduced earlier this year as part of our Game Commerce strategy and we are looking for engineers who want to take it to the next level and scale it across other dimensions on Twitch. Crates provides additional value to viewers engaging on Twitch, as well as more interesting and unique ways for Broadcasters, Game Developers and other influencers to reach their audience and monetize their content. This role is perfect for an engineer who has a passion for building high quality, reliable, extensible Web application software. You are passionate about best practices and comfortable with Jav",
          "og:url": "https://jobs.lever.co/twitch/7f6218d3-ca90-4daf-abfe-cd693a5ad76b",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior DevOps Engineer - Extensions",
    "htmlTitle": "Twitch - Senior DevOps <b>Engineer</b> - Extensions",
    "link": "https://jobs.lever.co/twitch/aad8df8f-9b94-4141-8805-0e9eeae5c08c",
    "displayLink": "jobs.lever.co",
    "snippet": "This team needs a senior DevOps engineer, who is able to channel their ... \nautomated CI/CD pipelines, managing the lifecycle of software infrastructure, and\n\u00a0...",
    "htmlSnippet": "This team needs a senior DevOps <b>engineer</b>, who is able to channel their ... <br>\nautomated CI/CD pipelines, managing the lifecycle of <b>software</b> infrastructure, and<br>\n&nbsp;...",
    "cacheId": "UNG3yr518MUJ",
    "formattedUrl": "https://jobs.lever.co/twitch/aad8df8f-9b94-4141-8805-0e9eeae5c08c",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/aad8df8f-9b94-4141-8805-0e9eeae5c08c",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior DevOps Engineer - Extensions",
          "twitter:description": "Twitch developer products power the connections between millions of broadcasters and users. This position will be part of the team responsible for providing new interactive ways to connect on Twitch. This team needs a senior DevOps engineer, who is able to channel their years of experience in building automated CI/CD pipelines, managing the lifecycle of software infrastructure, and driving a shared vision for such work forward with the team.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior DevOps Engineer - Extensions",
          "og:description": "Twitch developer products power the connections between millions of broadcasters and users. This position will be part of the team responsible for providing new interactive ways to connect on Twitch. This team needs a senior DevOps engineer, who is able to channel their years of experience in building automated CI/CD pipelines, managing the lifecycle of software infrastructure, and driving a shared vision for such work forward with the team.",
          "og:url": "https://jobs.lever.co/twitch/aad8df8f-9b94-4141-8805-0e9eeae5c08c",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior Backend Engineer - Live Video Product",
    "htmlTitle": "Twitch - Senior Backend <b>Engineer</b> - Live Video Product",
    "link": "https://jobs.lever.co/twitch/507f1c1d-aa19-4148-86cd-edf72a3a15ea",
    "displayLink": "jobs.lever.co",
    "snippet": "On this team, you'll work closely with our other engineering and product teams to \n... Start-up experience; Notable contributions to open source software projects-\u00a0...",
    "htmlSnippet": "On this team, you&#39;ll work closely with our other <b>engineering</b> and product teams to <br>\n... Start-up experience; Notable contributions to open source <b>software</b> projects-&nbsp;...",
    "cacheId": "ZRJ5FvGpMVEJ",
    "formattedUrl": "https://jobs.lever.co/twitch/507f1c1d-aa19-4148-86cd-edf72a3a15ea",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/507f1c1d-aa19-4148-86cd-edf72a3a15ea",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior Backend Engineer - Live Video Product",
          "twitter:description": "Twitch has over 100 million users, and the Live Video Product team is responsible for building products that improve the experience of watching live video. We\u2019re building a number of features to make Twitch the most compelling destination for gaming video this year. Recently, we launched Clips and our HTML5 Video Player, and we\u2019re just getting started. We\u2019re looking for engineers that love delighting people with incredible products and user experiences. On this team, you\u2019ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in building applications for the Web, comfort working throughout the stack, and an understanding of product concerns. Currently, we\u2019re focused on driving real-time interaction between broadcasters and viewers and building a live video watching experience that is uniquely Twitch.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior Backend Engineer - Live Video Product",
          "og:description": "Twitch has over 100 million users, and the Live Video Product team is responsible for building products that improve the experience of watching live video. We\u2019re building a number of features to make Twitch the most compelling destination for gaming video this year. Recently, we launched Clips and our HTML5 Video Player, and we\u2019re just getting started. We\u2019re looking for engineers that love delighting people with incredible products and user experiences. On this team, you\u2019ll work closely with our other engineering and product teams to craft a beautiful and engaging product, collect feedback, and iterate quickly. We value expertise in building applications for the Web, comfort working throughout the stack, and an understanding of product concerns. Currently, we\u2019re focused on driving real-time interaction between broadcasters and viewers and building a live video watching experience that is uniquely Twitch.",
          "og:url": "https://jobs.lever.co/twitch/507f1c1d-aa19-4148-86cd-edf72a3a15ea",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Software Development Manager - Game Commerce",
    "htmlTitle": "Twitch - <b>Software</b> Development Manager - Game Commerce",
    "link": "https://jobs.lever.co/twitch/d253d6be-f921-4b2c-8059-e0ad45090a62",
    "displayLink": "jobs.lever.co",
    "snippet": "Responsibilities include direct management of 5+ engineers, process and quality \nof service improvements, strategic planning, project management for software\u00a0...",
    "htmlSnippet": "Responsibilities include direct management of 5+ <b>engineers</b>, process and quality <br>\nof service improvements, strategic planning, project management for <b>software</b>&nbsp;...",
    "cacheId": "ccNyH9ZgP_MJ",
    "formattedUrl": "https://jobs.lever.co/.../d253d6be-f921-4b2c-8059-e0ad45090a62",
    "htmlFormattedUrl": "https://jobs.lever.co/.../d253d6be-f921-4b2c-8059-e0ad45090a62",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Software Development Manager - Game Commerce",
          "twitter:description": "The Game Commerce team at Twitch is looking for a passionate, results-oriented, inventive software manager to continue our rapid feature development for Twitch Game Commerce. The candidate thrives in a fast-paced environment, understands the gaming and streaming space, and will help us bring new and innovative solutions to our viewers and broadcasters. As the development manager, you will have technical ownership of the customer experience for Game Commerce. You'll lead a talented and nimble team of engineers to create innovative ways to maintain a high velocity delivery of features from our product roadmap. Responsibilities include direct management of 5+ engineers, process and quality of service improvements, strategic planning, project management for software within the team, and management of resources across teams. Successful candidates will be strong leaders who can prioritize well, communicate clearly, and have a consistent track record of delivery. The Game Commerce business r",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Software Development Manager - Game Commerce",
          "og:description": "The Game Commerce team at Twitch is looking for a passionate, results-oriented, inventive software manager to continue our rapid feature development for Twitch Game Commerce. The candidate thrives in a fast-paced environment, understands the gaming and streaming space, and will help us bring new and innovative solutions to our viewers and broadcasters. As the development manager, you will have technical ownership of the customer experience for Game Commerce. You'll lead a talented and nimble team of engineers to create innovative ways to maintain a high velocity delivery of features from our product roadmap. Responsibilities include direct management of 5+ engineers, process and quality of service improvements, strategic planning, project management for software within the team, and management of resources across teams. Successful candidates will be strong leaders who can prioritize well, communicate clearly, and have a consistent track record of delivery. The Game Commerce business r",
          "og:url": "https://jobs.lever.co/twitch/d253d6be-f921-4b2c-8059-e0ad45090a62",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Application Security Engineer",
    "htmlTitle": "Twitch - Application Security <b>Engineer</b>",
    "link": "https://jobs.lever.co/twitch/f2537fe4-6c4e-4f22-a002-4455dda80675",
    "displayLink": "jobs.lever.co",
    "snippet": "Twitch is looking for a focused Application Security Engineer with a desire to ... \nDemonstrated software development proficiency (Go, Ruby, Python, Java, C#,\u00a0...",
    "htmlSnippet": "Twitch is looking for a focused Application Security <b>Engineer</b> with a desire to ... <br>\nDemonstrated <b>software</b> development proficiency (Go, Ruby, Python, Java, C#,&nbsp;...",
    "cacheId": "bqpGsYN3G3sJ",
    "formattedUrl": "https://jobs.lever.co/twitch/f2537fe4-6c4e-4f22-a002-4455dda80675",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/f2537fe4-6c4e-4f22-a002-4455dda80675",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Application Security Engineer",
          "twitter:description": "Twitch is looking for a focused Application Security Engineer with a desire to play on the Blue Team. Maybe you\u2019re a pentester who is bored of always winning; maybe you\u2019re the local security champion within your development organization. However you got to where you are, we want one thing from you - help make Twitch\u2019s products as safe as they can be for our partners and viewers. In this role, you will be escorting Twitch\u2019s products and features from ideation to deployment. You will be providing consulting to product teams looking to try new things safely. You will be reviewing critical passages of code for adherence to standards and safe practices. Most importantly, you will be helping to build and automate the tools that do the above for you as a force multiplier. And yes, where warranted, there\u2019s some pentesting in it for you as well. You know, if you\u2019re into that.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Application Security Engineer",
          "og:description": "Twitch is looking for a focused Application Security Engineer with a desire to play on the Blue Team. Maybe you\u2019re a pentester who is bored of always winning; maybe you\u2019re the local security champion within your development organization. However you got to where you are, we want one thing from you - help make Twitch\u2019s products as safe as they can be for our partners and viewers. In this role, you will be escorting Twitch\u2019s products and features from ideation to deployment. You will be providing consulting to product teams looking to try new things safely. You will be reviewing critical passages of code for adherence to standards and safe practices. Most importantly, you will be helping to build and automate the tools that do the above for you as a force multiplier. And yes, where warranted, there\u2019s some pentesting in it for you as well. You know, if you\u2019re into that.",
          "og:url": "https://jobs.lever.co/twitch/f2537fe4-6c4e-4f22-a002-4455dda80675",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Developer Marketing Manager - Events and Community",
    "htmlTitle": "Twitch - Developer Marketing Manager - Events and Community",
    "link": "https://jobs.lever.co/twitch/91938768-cbe6-4b83-aa3c-4dfcd3a30351",
    "displayLink": "jobs.lever.co",
    "snippet": "Success marketing a B2B solution specified or purchased by software engineers; \nideally in gaming; Success in using data to inform your campaign planning and\u00a0...",
    "htmlSnippet": "Success marketing a B2B solution specified or purchased by <b>software engineers</b>; <br>\nideally in gaming; Success in using data to inform your campaign planning and&nbsp;...",
    "cacheId": "sehnhbeyYOoJ",
    "formattedUrl": "https://jobs.lever.co/twitch/91938768-cbe6-4b83-aa3c-4dfcd3a30351",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/91938768-cbe6-4b83-aa3c-4dfcd3a30351",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Developer Marketing Manager - Events and Community",
          "twitter:description": "As creators of the games and apps Twitch broadcasters and viewers revel in, developers are incredibly important partners for Twitch. They are already reaching tens of millions of viewers on Twitch today; we want to help them wrap even more broadcasters, viewers and users into their products. The Developer Success team helps creators make compelling apps that stand out, present their products to viewers who may like them, engage with their existing users, and find innovative new ways to generate revenue. We\u2019d like you to build and scale the channels through which we invite developers to engage with us. You\u2019ll apply your expertise in community growth and event marketing to help developers understand how Twitch can help them succeed, create scalable campaigns inviting them to get in contact and measure outcomes against business goals using data. We win when thousands of companies clamor to partner with us; you win when you\u2019ve created campaigns that inspires developers to meet us",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Developer Marketing Manager - Events and Community",
          "og:description": "As creators of the games and apps Twitch broadcasters and viewers revel in, developers are incredibly important partners for Twitch. They are already reaching tens of millions of viewers on Twitch today; we want to help them wrap even more broadcasters, viewers and users into their products. The Developer Success team helps creators make compelling apps that stand out, present their products to viewers who may like them, engage with their existing users, and find innovative new ways to generate revenue. We\u2019d like you to build and scale the channels through which we invite developers to engage with us. You\u2019ll apply your expertise in community growth and event marketing to help developers understand how Twitch can help them succeed, create scalable campaigns inviting them to get in contact and measure outcomes against business goals using data. We win when thousands of companies clamor to partner with us; you win when you\u2019ve created campaigns that inspires developers to meet us",
          "og:url": "https://jobs.lever.co/twitch/91938768-cbe6-4b83-aa3c-4dfcd3a30351",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Senior UX Designer - Games Commerce",
    "htmlTitle": "Twitch - Senior UX Designer - Games Commerce",
    "link": "https://jobs.lever.co/twitch/0097ec3a-9863-4771-8001-24022b058536",
    "displayLink": "jobs.lever.co",
    "snippet": "Commerce \u2013 Games Store Engineering ... use your passion, ingenuity, \nexperience, and pragmatism to build very cool software that affects millions of \ncustomers.",
    "htmlSnippet": "Commerce \u2013 Games Store <b>Engineering</b> ... use your passion, ingenuity, <br>\nexperience, and pragmatism to build very cool <b>software</b> that affects millions of <br>\ncustomers.",
    "cacheId": "NjJ4nomD3uYJ",
    "formattedUrl": "https://jobs.lever.co/.../0097ec3a-9863-4771-8001-24022b058536",
    "htmlFormattedUrl": "https://jobs.lever.co/.../0097ec3a-9863-4771-8001-24022b058536",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Senior UX Designer - Games Commerce",
          "twitter:description": "The Twitch Seattle team is seeking a gifted Senior UX Designer to drive user experiences for exciting new opportunities and projects. We offer a series of stimulating problems, an environment that's exciting, motivating, fun, and new. You will have colleagues who will challenge you to achieve more than you thought possible, as well as great camaraderie. Joining our team will give you endless opportunities to use your passion, ingenuity, experience, and pragmatism to build very cool software that affects millions of customers. Our ideal Senior UX Designer will exhibit a strong passion for building top-notch gamer-oriented web and software experiences based on a well-rounded set of design skills that range from wireframes to full fidelity design comps.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Senior UX Designer - Games Commerce",
          "og:description": "The Twitch Seattle team is seeking a gifted Senior UX Designer to drive user experiences for exciting new opportunities and projects. We offer a series of stimulating problems, an environment that's exciting, motivating, fun, and new. You will have colleagues who will challenge you to achieve more than you thought possible, as well as great camaraderie. Joining our team will give you endless opportunities to use your passion, ingenuity, experience, and pragmatism to build very cool software that affects millions of customers. Our ideal Senior UX Designer will exhibit a strong passion for building top-notch gamer-oriented web and software experiences based on a well-rounded set of design skills that range from wireframes to full fidelity design comps.",
          "og:url": "https://jobs.lever.co/twitch/0097ec3a-9863-4771-8001-24022b058536",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Technical Program Manager - Associates",
    "htmlTitle": "Twitch - Technical Program Manager - Associates",
    "link": "https://jobs.lever.co/twitch/effc0e76-15be-423c-a836-7fc50dba2913",
    "displayLink": "jobs.lever.co",
    "snippet": "Share your program management knowledge with engineering leadership teams\n. ... a technical program manager in software/web development organizations.",
    "htmlSnippet": "Share your program management knowledge with <b>engineering</b> leadership teams<br>\n. ... a technical program manager in <b>software</b>/web development organizations.",
    "cacheId": "66w9a6EQ6qoJ",
    "formattedUrl": "https://jobs.lever.co/twitch/effc0e76-15be-423c-a836-7fc50dba2913",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/effc0e76-15be-423c-a836-7fc50dba2913",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Technical Program Manager - Associates",
          "twitter:description": "The Technical Program Management team at Twitch is leading execution of high priority and impactful product initiatives while Twitch is going through hyper growth. TPMs find the right balance between being strategic and tactical to lead cross-functional teams to successfully deliver strategic and complex programs that move the needles for Twitch. We are the glue for the company, and we are playing a key role in scaling the organization.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Technical Program Manager - Associates",
          "og:description": "The Technical Program Management team at Twitch is leading execution of high priority and impactful product initiatives while Twitch is going through hyper growth. TPMs find the right balance between being strategic and tactical to lead cross-functional teams to successfully deliver strategic and complex programs that move the needles for Twitch. We are the glue for the company, and we are playing a key role in scaling the organization.",
          "og:url": "https://jobs.lever.co/twitch/effc0e76-15be-423c-a836-7fc50dba2913",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "630",
          "og:image:width": "1200"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  },
  {
    "kind": "customsearch#result",
    "title": "Twitch - Technical Writer",
    "htmlTitle": "Twitch - Technical Writer",
    "link": "https://jobs.lever.co/twitch/f6d721a0-f549-443d-bcbc-51006f911079",
    "displayLink": "jobs.lever.co",
    "snippet": "You will collaborate closely with engineers, product managers, and usability \nexperts ... Good foundation in programming, API design, and software \narchitecture\u00a0...",
    "htmlSnippet": "You will collaborate closely with <b>engineers</b>, product managers, and usability <br>\nexperts ... Good foundation in programming, API design, and <b>software</b> <br>\narchitecture&nbsp;...",
    "cacheId": "H8EfHaxW2XUJ",
    "formattedUrl": "https://jobs.lever.co/twitch/f6d721a0-f549-443d-bcbc-51006f911079",
    "htmlFormattedUrl": "https://jobs.lever.co/twitch/f6d721a0-f549-443d-bcbc-51006f911079",
    "pagemap": {
      "cse_thumbnail": [
        {
          "width": "258",
          "height": "86",
          "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug"
        }
      ],
      "metatags": [
        {
          "viewport": "width=device-width, initial-scale=1, maximum-scale=1",
          "twitter:title": "Twitch - Technical Writer",
          "twitter:description": "Twitch is looking for an experienced Technical Writer to produce high-quality documentation which will contribute to the overall success of our products. Most importantly, you should specialize in API documentation and other highly technical deliverables. You will collaborate closely with engineers, product managers, and usability experts in order to enhance our product. \u00a0The ideal candidate has excellent communications skills and has a passion for extracting complex systems and concepts into user documentation.",
          "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
          "og:title": "Twitch - Technical Writer",
          "og:description": "Twitch is looking for an experienced Technical Writer to produce high-quality documentation which will contribute to the overall success of our products. Most importantly, you should specialize in API documentation and other highly technical deliverables. You will collaborate closely with engineers, product managers, and usability experts in order to enhance our product. \u00a0The ideal candidate has excellent communications skills and has a passion for extracting complex systems and concepts into user documentation.",
          "og:url": "https://jobs.lever.co/twitch/f6d721a0-f549-443d-bcbc-51006f911079",
          "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
          "og:image:height": "512",
          "og:image:width": "1024"
        }
      ],
      "cse_image": [
        {
          "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
        }
      ]
    }
  }
]

# local manual per listing test
def get_job_listings_from_google():
    data_get_job_listings_from_google = results_from_GSE_query_51
    return data_get_job_listings_from_google

# # set gse query parameters to iterate through results
# def get_job_listings_from_google(cse_search_term, number_of_listings_to_get):
#     return_value = []
#     for search_result_number_from_which_api_query_results_start in range(1, number_of_listings_to_get + 1, MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY):
#         try:
#             return_value.extend(do_google_search(
#                 # online version of keywords > https://i.codefor.cash/job_alerts/generate_subscriber_keywords
#                 search_term=cse_search_term,
#                 api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN,
#                 num=MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY, start=search_result_number_from_which_api_query_results_start))
#         except:
#             print(len(return_value), 'Listings + Empty Index')
#             return return_value[:number_of_listings_to_get]
#     return return_value[:number_of_listings_to_get]

# def save_gse_call_results(listings):
#     with open('saved_gse_results.txt','a+') as f:
#         f.write(json.dump(listings), sort_keys = True,
#                 indent = 4)

def save_gse_call_results(listings):
    print('@@@@', len(listings), 'Listings Saved @@@@')
    with open('./saved_files/saved_gse_results.txt','a+') as f:
        f.write(json.dumps(listings))
    # relevant??????????
    # with open('saved_gse_results.txt','a+') as f:
    #     f.write(json.dumps(get_job_listings_from_google("'software engineer' remote site:jobs.lever.co/" + client, 10), sort_keys = True,
    #             indent = 4))

def save_print_log(data):
    saveout = sys.stdout
    fsock = open('./saved_files/saved_post_metrics.log', 'a+')
    sys.stdout = fsock
    print(data)
    sys.stdout = saveout
    fsock.close()

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
            save_print_log(e)
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

            # soupstrain time_commitment & employment_type
            time_commitment_tag_class = SoupStrainer("div", {"class" : "sort-by-commitment posting-category medium-category-label"})
            time_commitment_soup_html = BeautifulSoup(html, "html.parser", parse_only=time_commitment_tag_class)
            time_commitment = time_commitment_soup_html.text
            data_to_send_in_request_body["time_commitment"] = time_commitment
            if time_commitment == "":
                data_to_send_in_request_body["employment_type"] = "doesnt_say"
            else:
                data_to_send_in_request_body["employment_type"] = time_commitment
            # print listing title
            print(data_of_each_listing["title"])
            save_print_log(data_of_each_listing["title"])
            print('>>>>', data_of_each_listing["website"])
            save_print_log(data_of_each_listing["website"])
            print('TC:', time_commitment, 'ET:', data_to_send_in_request_body["employment_type"])

            # soupstrain location
            location_tag_class = SoupStrainer("div", {"class" : "sort-by-time posting-category medium-category-label"})
            location_soup_html = BeautifulSoup(html, "html.parser", parse_only=location_tag_class)
            location = location_soup_html.text
            print(location)
            save_print_log(location)

            try:
                country = Geocoder.geocode(location).country
                latitude = Geocoder.geocode(location).latitude
                longitude = Geocoder.geocode(location).longitude
            except:
                print('## slept ##')
                save_print_log("## slept ##")
                time.sleep(11)
                try:
                    country = Geocoder.geocode(location).country
                    latitude = Geocoder.geocode(location).latitude
                    longitude = Geocoder.geocode(location).longitude
                except GeocoderError as e:
                    print(e)
                    save_print_log(e)
                    pass
            try:
                print("country:", country, "coords", latitude, longitude)
                data_to_send_in_request_body["country"] = country
                data_to_send_in_request_body["lat"] = latitude
                data_to_send_in_request_body["lng"] = longitude
            except:
                pass

            # set remote or not
            if 'Remote' in location or 'remote' in location or 'Remote' in data_of_each_listing["title"] or 'remote' in data_of_each_listing["title"]:
                data_to_send_in_request_body["remote_ok"] = 'remote_ok'
                # print('remote')
            else:
                # print('no remote')
                data_to_send_in_request_body["remote_ok"] = 'doesnt_say'

            # check for bad words in description
            for bad_word in BAD_WORDS_LIST:
                if bad_word in data_of_each_listing["title"] or bad_word in description_web_data:
                    any_bad_words = True
                    print('** bad word:', bad_word)
                    save_print_log(bad_word)
                    with open('./saved_files/saved_badword_list.txt','a+') as f:
                        f.write(json.dumps(data_to_send_in_request_body))
                else:
                    data_to_send_in_request_body["description"] = description_web_data

                    for data_key in data_to_send_in_request_body:
                        data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key]

            # save listings without bad words
            if any_bad_words == False:
                clean_data_to_post = data_to_send_in_request_body
                count += 1
                # # test: print formatted descriptions
                # print(description_web_data)
            else:
                print("*********************************************")
                save_print_log("*********************************************")
                continue
            # hit geocoder every 1 sec
            # time.sleep(3)
        print("*********************************************")
        save_print_log("*********************************************")
        
        # # test print json formatted complete listing
        # print(data_to_send_in_request_body)

        # send formatted json to code4cash api
        response_per_post = requests.post(
            url=CODEFORCASH_BASE_URL+'/api/metum/create',
            data=clean_data_to_post)
        # save code4cash response
        print(response_per_post)
        with open('./saved_files/saved_C4C_response','ab+') as f:
            pickle.dump(response_per_post, f)

        # save prePostListings before post to c4c
        with open('./saved_files/saved_post_data.txt','a+') as f:
            f.write(json.dumps(clean_data_to_post))

    # print(clean_data_to_post)
    print('XXXX', count, 'Clean Listings Posted XXXX')
    save_print_log(count)
    save_print_log("*********************************************")

if __name__ == '__main__':
    send_job_listings_to_codeforcash(get_job_listings_from_google())
    # for client in clients:
    #     print('**** ROOT:', client, '****')
    #     send_job_listings_to_codeforcash(get_job_listings_from_google("'software engineer' site:jobs.lever.co/" + client, 150))
        # get_job_listings_from_google("'software engineer' site:jobs.lever.co/" + client, 40)
        # save_gse_call_results(send_job_listings_to_codeforcash(get_job_listings_from_google("'software engineer' remote site:jobs.lever.co/" + client, 10)))

