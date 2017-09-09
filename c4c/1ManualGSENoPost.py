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

CSE_SEARCH_TERM_PREFIX = 'engineer software site:jobs.lever.co/'

# clients = ['brightedge']
# clients = ['brightedge', 'voleon']
# clients = ['brightedge', 'blendlabs', 'voleon']

# def pass_different_clients():
#     for client in clients:
#         cse_search_term = CSE_SEARCH_TERM_PREFIX + client
#         print(cse_search_term)
#         get_job_listings_from_google(cse_search_term)


# def do_google_search(search_term, api_key, cse_id, **kwargs):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
#     # print(res['items'])
#     print(res['queries']['request'][0]['totalResults'])
#     return res['items']

results_from_GSE_query = [
  {
    'kind': 'customsearch#result',
    'title': 'BrightEdge - Software Engineer',
    'htmlTitle': 'BrightEdge - <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/brightedge/3d8d1fcb-994b-4a45-b1b6-a76910c364d2',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Are you a software engineer looking to join a fast-paced team with ample room \nfor growth? Do you enjoy working with the latest technologies and do you want to\n\xa0...',
    'htmlSnippet': 'Are you a <b>software engineer</b> looking to join a fast-paced team with ample room <br>\nfor growth? Do you enjoy working with the latest technologies and do you want to<br>\n&nbsp;...',
    'cacheId': 'Kw4Btfzu7REJ',
    'formattedUrl': 'https://jobs.lever.co/.../3d8d1fcb-994b-4a45-b1b6-a76910c364d2',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../3d8d1fcb-994b-4a45-b1b6-a76910c364d2',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '306',
          'height': '165',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRQNabfPIIk51v8AsADS3rDUnaCFVMm6jfTuFxtS67-SSRulUU6F-C5V-RT'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'BrightEdge - Software Engineer',
          'twitter:description': 'Are you a software engineer looking to join a fast-paced team with ample room for growth? Do you enjoy working with the latest technologies and do you want to work on an innovative, industry-leading product? If so, we need to talk! As the industry pioneer behind Content Performance Marketing, BrightEdge has thoroughly redefined the concept of search engine optimization (SEO) by developing an award-winning platform that precisely measures and optimizes marketing content across online channels. Our cloud-based platform is powered by big data analysis that allows our customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge has emerged as the leading international provider of cloud-based SEO Enterprise solutions due to its dynamic and results oriented entrepreneurial culture. BrightEdge is looking for a Software Engineer to join our team. In this position, you will develop key backend and frontend components used by some of the largest compan',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495228998728.png',
          'og:title': 'BrightEdge - Software Engineer',
          'og:description': 'Are you a software engineer looking to join a fast-paced team with ample room for growth? Do you enjoy working with the latest technologies and do you want to work on an innovative, industry-leading product? If so, we need to talk! As the industry pioneer behind Content Performance Marketing, BrightEdge has thoroughly redefined the concept of search engine optimization (SEO) by developing an award-winning platform that precisely measures and optimizes marketing content across online channels. Our cloud-based platform is powered by big data analysis that allows our customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge has emerged as the leading international provider of cloud-based SEO Enterprise solutions due to its dynamic and results oriented entrepreneurial culture. BrightEdge is looking for a Software Engineer to join our team. In this position, you will develop key backend and frontend components used by some of the largest compan',
          'og:url': 'https://jobs.lever.co/brightedge/3d8d1fcb-994b-4a45-b1b6-a76910c364d2',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'BrightEdge - Software Development Engineer in Test',
    'htmlTitle': 'BrightEdge - <b>Software</b> Development <b>Engineer</b> in Test',
    'link': 'https://jobs.lever.co/brightedge/f861c953-e7ee-42b9-8fd4-ba2912a89f49',
    'displayLink': 'jobs.lever.co',
    'snippet': 'BrightEdge is looking for a Software Development Engineer in Test to join our \nteam. In this position, you will perform various kinds of testing and automation\xa0...',
    'htmlSnippet': 'BrightEdge is looking for a <b>Software</b> Development <b>Engineer</b> in Test to join our <br>\nteam. In this position, you will perform various kinds of testing and automation&nbsp;...',
    'cacheId': 'mC627DTyTBsJ',
    'formattedUrl': 'https://jobs.lever.co/.../f861c953-e7ee-42b9-8fd4-ba2912a89f49',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../f861c953-e7ee-42b9-8fd4-ba2912a89f49',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '306',
          'height': '165',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRQNabfPIIk51v8AsADS3rDUnaCFVMm6jfTuFxtS67-SSRulUU6F-C5V-RT'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'BrightEdge - Software Development Engineer in Test',
          'twitter:description': 'Are you an engineer with passion and experience in Software Quality Assurance and Test Automation? Are you looking to join a fast-paced team with ample room for growth and innovation? BrightEdge is looking for a Software Development Engineer in Test to join our team. In this position, you will perform various kinds of testing and automation activities to enforce the highest level of product quality for the BrightEdge Platform. BrightEdge is growing quickly, and this is a great opportunity to work with some of the brightest minds in Silicon Valley on innovative solutions used by many Fortune 100, Fortune 500 and Fortune 1000 organizations and brands.',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495228998728.png',
          'og:title': 'BrightEdge - Software Development Engineer in Test',
          'og:description': 'Are you an engineer with passion and experience in Software Quality Assurance and Test Automation? Are you looking to join a fast-paced team with ample room for growth and innovation? BrightEdge is looking for a Software Development Engineer in Test to join our team. In this position, you will perform various kinds of testing and automation activities to enforce the highest level of product quality for the BrightEdge Platform. BrightEdge is growing quickly, and this is a great opportunity to work with some of the brightest minds in Silicon Valley on innovative solutions used by many Fortune 100, Fortune 500 and Fortune 1000 organizations and brands.',
          'og:url': 'https://jobs.lever.co/brightedge/f861c953-e7ee-42b9-8fd4-ba2912a89f49',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'BrightEdge - Front End Software Engineer',
    'htmlTitle': 'BrightEdge - Front End <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/brightedge/f89f332e-6530-4455-b74a-5eeee89ea2a5',
    'displayLink': 'jobs.lever.co',
    'snippet': 'BrightEdge is looking for a Front End Software Engineer who loves working with \nReact.js, Redux and Javascript. If you like helping others, seeing things grow\xa0...',
    'htmlSnippet': 'BrightEdge is looking for a Front End <b>Software Engineer</b> who loves working with <br>\nReact.js, Redux and Javascript. If you like helping others, seeing things grow&nbsp;...',
    'cacheId': 'DVlEHBmyfe0J',
    'formattedUrl': 'https://jobs.lever.co/.../f89f332e-6530-4455-b74a-5eeee89ea2a5',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../f89f332e-6530-4455-b74a-5eeee89ea2a5',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '306',
          'height': '165',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRQNabfPIIk51v8AsADS3rDUnaCFVMm6jfTuFxtS67-SSRulUU6F-C5V-RT'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'BrightEdge - Front End Software Engineer',
          'twitter:description': 'Join the international industry pioneer behind Content Performance Marketing! BrightEdge’s award-winning platform precisely measures and optimizes marketing content across online channels. We’ve thoroughly redefined the concept of search engine optimization (SEO), and our cloud-based platform is powered by big data analysis that allows customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge is looking for a Front End Software Engineer who loves working with React.js, Redux and Javascript. If you like helping others, seeing things grow and watching a market quickly adopt your creations…this is your place!',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495228998728.png',
          'og:title': 'BrightEdge - Front End Software Engineer',
          'og:description': 'Join the international industry pioneer behind Content Performance Marketing! BrightEdge’s award-winning platform precisely measures and optimizes marketing content across online channels. We’ve thoroughly redefined the concept of search engine optimization (SEO), and our cloud-based platform is powered by big data analysis that allows customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge is looking for a Front End Software Engineer who loves working with React.js, Redux and Javascript. If you like helping others, seeing things grow and watching a market quickly adopt your creations…this is your place!',
          'og:url': 'https://jobs.lever.co/brightedge/f89f332e-6530-4455-b74a-5eeee89ea2a5',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'BrightEdge - Software Engineer',
    'htmlTitle': 'BrightEdge - <b>Software Engineer</b>',
    'link': 'https://jobs.lever.co/brightedge/3d8d1fcb-994b-4a45-b1b6-a76910c364d2/',
    'displayLink': 'jobs.lever.co',
    'snippet': 'U.S. Equal Employment Opportunity information (Completion is voluntary and will \nnot subject you to adverse treatment). BrightEdge provides equal employment\xa0...',
    'htmlSnippet': 'U.S. Equal Employment Opportunity information (Completion is voluntary and will <br>\nnot subject you to adverse treatment). BrightEdge provides equal employment&nbsp;...',
    'cacheId': 'BDVwmTv_vS8J',
    'formattedUrl': 'https://jobs.lever.co/brightedge/3d8d1fcb-994b-4a45-b1b6.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/brightedge/3d8d1fcb-994b-4a45-b1b6.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '306',
          'height': '165',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRQNabfPIIk51v8AsADS3rDUnaCFVMm6jfTuFxtS67-SSRulUU6F-C5V-RT'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'BrightEdge - Software Engineer',
          'twitter:description': 'Are you a software engineer looking to join a fast-paced team with ample room for growth? Do you enjoy working with the latest technologies and do you want to work on an innovative, industry-leading product? If so, we need to talk! As the industry pioneer behind Content Performance Marketing, BrightEdge has thoroughly redefined the concept of search engine optimization (SEO) by developing an award-winning platform that precisely measures and optimizes marketing content across online channels. Our cloud-based platform is powered by big data analysis that allows our customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge has emerged as the leading international provider of cloud-based SEO Enterprise solutions due to its dynamic and results oriented entrepreneurial culture. BrightEdge is looking for a Software Engineer to join our team. In this position, you will develop key backend and frontend components used by some of the largest compani',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495228998728.png',
          'og:title': 'BrightEdge - Software Engineer',
          'og:description': 'Are you a software engineer looking to join a fast-paced team with ample room for growth? Do you enjoy working with the latest technologies and do you want to work on an innovative, industry-leading product? If so, we need to talk! As the industry pioneer behind Content Performance Marketing, BrightEdge has thoroughly redefined the concept of search engine optimization (SEO) by developing an award-winning platform that precisely measures and optimizes marketing content across online channels. Our cloud-based platform is powered by big data analysis that allows our customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge has emerged as the leading international provider of cloud-based SEO Enterprise solutions due to its dynamic and results oriented entrepreneurial culture. BrightEdge is looking for a Software Engineer to join our team. In this position, you will develop key backend and frontend components used by some of the largest compani',
          'og:url': 'https://jobs.lever.co/brightedge/3d8d1fcb-994b-4a45-b1b6-a76910c364d2/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'BrightEdge - Software Engineer, Full Stack',
    'htmlTitle': 'BrightEdge - <b>Software Engineer</b>, Full Stack',
    'link': 'https://jobs.lever.co/brightedge/662fe728-6345-40ea-bed2-ba403d405d13/',
    'displayLink': 'jobs.lever.co',
    'snippet': 'U.S. Equal Employment Opportunity information (Completion is voluntary and will \nnot subject you to adverse treatment). BrightEdge provides equal employment\xa0...',
    'htmlSnippet': 'U.S. Equal Employment Opportunity information (Completion is voluntary and will <br>\nnot subject you to adverse treatment). BrightEdge provides equal employment&nbsp;...',
    'cacheId': '5NYp9QRdzacJ',
    'formattedUrl': 'https://jobs.lever.co/brightedge/662fe728-6345-40ea-bed2.../apply',
    'htmlFormattedUrl': 'https://jobs.lever.co/brightedge/662fe728-6345-40ea-bed2.../apply',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '306',
          'height': '165',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRQNabfPIIk51v8AsADS3rDUnaCFVMm6jfTuFxtS67-SSRulUU6F-C5V-RT'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'BrightEdge - Software Engineer, Full Stack',
          'twitter:description': 'As the industry pioneer behind Content Performance Marketing, BrightEdge has thoroughly redefined the concept of search engine optimization (SEO) by developing an award-winning platform that precisely measures and optimizes marketing content across online channels. Our cloud-based platform is powered by big data analysis that allows our customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge has emerged as the leading international provider of cloud-based SEO Enterprise solutions due to its dynamic and results oriented entrepreneurial culture. Are you a software engineer looking to join a fast-paced team with ample room for growth? Do you enjoy working with the latest technologies and do you want to work on an innovative, industry-leading product? If so, we need to talk! BrightEdge is looking for a Software Engineer to join our team. In this position, you will develop key backend and frontend components used by some of the largest compan',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495228998728.png',
          'og:title': 'BrightEdge - Software Engineer, Full Stack',
          'og:description': 'As the industry pioneer behind Content Performance Marketing, BrightEdge has thoroughly redefined the concept of search engine optimization (SEO) by developing an award-winning platform that precisely measures and optimizes marketing content across online channels. Our cloud-based platform is powered by big data analysis that allows our customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge has emerged as the leading international provider of cloud-based SEO Enterprise solutions due to its dynamic and results oriented entrepreneurial culture. Are you a software engineer looking to join a fast-paced team with ample room for growth? Do you enjoy working with the latest technologies and do you want to work on an innovative, industry-leading product? If so, we need to talk! BrightEdge is looking for a Software Engineer to join our team. In this position, you will develop key backend and frontend components used by some of the largest compan',
          'og:url': 'https://jobs.lever.co/brightedge/662fe728-6345-40ea-bed2-ba403d405d13/apply',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'BrightEdge - Sales Engineer',
    'htmlTitle': 'BrightEdge - Sales <b>Engineer</b>',
    'link': 'https://jobs.lever.co/brightedge/d0579004-b2df-42da-ae47-7f2346da5c2e',
    'displayLink': 'jobs.lever.co',
    'snippet': 'BrightEdge is looking for a Sales Engineer to take our pre-sales process to the ... \nManagement Software, Salesforce and other third-party integrations is a plus\xa0...',
    'htmlSnippet': 'BrightEdge is looking for a Sales <b>Engineer</b> to take our pre-sales process to the ... <br>\nManagement <b>Software</b>, Salesforce and other third-party integrations is a plus&nbsp;...',
    'cacheId': 'O0XRv9oqEioJ',
    'formattedUrl': 'https://jobs.lever.co/.../d0579004-b2df-42da-ae47-7f2346da5c2e',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../d0579004-b2df-42da-ae47-7f2346da5c2e',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '306',
          'height': '165',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRQNabfPIIk51v8AsADS3rDUnaCFVMm6jfTuFxtS67-SSRulUU6F-C5V-RT'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'BrightEdge - Sales Engineer',
          'twitter:description': 'As the industry pioneer behind Content Performance Marketing, BrightEdge has thoroughly redefined the concept of Search Engine Optimization (SEO) by developing an award-winning platform that precisely measures and optimizes marketing content across online channels. Our cloud-based platform is powered by big data analysis that allows our customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge has emerged as the leading international provider of cloud-based SEO Enterprise solutions due to its dynamic and results oriented entrepreneurial culture. Are you a technology enthusiast looking to join a fast-paced team with ample room for growth? Do you love building relationships with clients and want to manage and own the technical side of sales for an industry leader? If so, we need to talk! BrightEdge is looking for a Sales Engineer to take our pre-sales process to the next level. You will be an invaluable addition to the Sales team as someone',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495228998728.png',
          'og:title': 'BrightEdge - Sales Engineer',
          'og:description': 'As the industry pioneer behind Content Performance Marketing, BrightEdge has thoroughly redefined the concept of Search Engine Optimization (SEO) by developing an award-winning platform that precisely measures and optimizes marketing content across online channels. Our cloud-based platform is powered by big data analysis that allows our customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge has emerged as the leading international provider of cloud-based SEO Enterprise solutions due to its dynamic and results oriented entrepreneurial culture. Are you a technology enthusiast looking to join a fast-paced team with ample room for growth? Do you love building relationships with clients and want to manage and own the technical side of sales for an industry leader? If so, we need to talk! BrightEdge is looking for a Sales Engineer to take our pre-sales process to the next level. You will be an invaluable addition to the Sales team as someone',
          'og:url': 'https://jobs.lever.co/brightedge/d0579004-b2df-42da-ae47-7f2346da5c2e',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'BrightEdge - Web Developer',
    'htmlTitle': 'BrightEdge - Web Developer',
    'link': 'https://jobs.lever.co/brightedge/d4b7745f-e15a-44e6-9558-9dd7eb5bdc26',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Are you a software engineer looking to join a fast-paced team with ample room \nfor growth? Do you love front-end / web development and want to manage and\xa0...',
    'htmlSnippet': 'Are you a <b>software engineer</b> looking to join a fast-paced team with ample room <br>\nfor growth? Do you love front-end / web development and want to manage and&nbsp;...',
    'cacheId': 'oKJaCYi2lB4J',
    'formattedUrl': 'https://jobs.lever.co/.../d4b7745f-e15a-44e6-9558-9dd7eb5bdc26',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../d4b7745f-e15a-44e6-9558-9dd7eb5bdc26',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '306',
          'height': '165',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRQNabfPIIk51v8AsADS3rDUnaCFVMm6jfTuFxtS67-SSRulUU6F-C5V-RT'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'BrightEdge - Web Developer',
          'twitter:description': 'As the industry pioneer behind Content Performance Marketing, BrightEdge has thoroughly redefined the concept of search engine optimization (SEO) by developing an award-winning platform that precisely measures and optimizes marketing content across online channels. Our cloud-based platform is powered by big data analysis that allows our customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge has emerged as the leading international provider of cloud-based SEO Enterprise solutions due to its dynamic and results oriented entrepreneurial culture. Are you a software engineer looking to join a fast-paced team with ample room for growth? Do you love front-end / web development and want to manage and own the website of an industry leader? If so, we need to talk! BrightEdge is looking for a Web Developer to take responsibility of our web properties, which are visited by tens of thousands of viewers each month and growing quickly. You will collab',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495228998728.png',
          'og:title': 'BrightEdge - Web Developer',
          'og:description': 'As the industry pioneer behind Content Performance Marketing, BrightEdge has thoroughly redefined the concept of search engine optimization (SEO) by developing an award-winning platform that precisely measures and optimizes marketing content across online channels. Our cloud-based platform is powered by big data analysis that allows our customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge has emerged as the leading international provider of cloud-based SEO Enterprise solutions due to its dynamic and results oriented entrepreneurial culture. Are you a software engineer looking to join a fast-paced team with ample room for growth? Do you love front-end / web development and want to manage and own the website of an industry leader? If so, we need to talk! BrightEdge is looking for a Web Developer to take responsibility of our web properties, which are visited by tens of thousands of viewers each month and growing quickly. You will collab',
          'og:url': 'https://jobs.lever.co/brightedge/d4b7745f-e15a-44e6-9558-9dd7eb5bdc26',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'BrightEdge',
    'htmlTitle': 'BrightEdge',
    'displayLink': 'jobs.lever.co',
    'snippet': 'Foster City HQR&D – Software DevelopmentFull-time · Apply ... Software \nDevelopment Engineer in Test. Foster City ... Software Engineer, Data & \nInfrastructure.',
    'htmlSnippet': 'Foster City HQR&amp;D – <b>Software</b> DevelopmentFull-time &middot; Apply ... <b>Software</b> <br>\nDevelopment <b>Engineer</b> in Test. Foster City ... <b>Software Engineer</b>, Data &amp; <br>\nInfrastructure.',
    'cacheId': '0XA8gIqU7gkJ',
    'formattedUrl': 'https://jobs.lever.co/brightedge/',
    'htmlFormattedUrl': 'https://jobs.lever.co/brightedge/',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '306',
          'height': '165',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRQNabfPIIk51v8AsADS3rDUnaCFVMm6jfTuFxtS67-SSRulUU6F-C5V-RT'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'BrightEdge',
          'twitter:description': 'Job openings at BrightEdge',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495228998728.png',
          'og:title': 'BrightEdge jobs',
          'og:description': 'Job openings at BrightEdge',
          'og:url': 'https://jobs.lever.co/brightedge',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png'
        }
      ]
    }
  },
  {
    'kind': 'customsearch#result',
    'title': 'BrightEdge - Back End Developer, Intelligent Experiences',
    'htmlTitle': 'BrightEdge - Back End Developer, Intelligent Experiences',
    'link': 'https://jobs.lever.co/brightedge/8f64062b-c557-4a6a-be40-70c057c8a2e2',
    'displayLink': 'jobs.lever.co',
    'snippet': 'R&D – Software Development ... A BA/BS degree is required; 2 years of Back-\nEnd Software Engineer experience; A working understanding SaaS and Cloud\xa0...',
    'htmlSnippet': 'R&amp;D – <b>Software</b> Development ... A BA/BS degree is required; 2 years of Back-<br>\nEnd <b>Software Engineer</b> experience; A working understanding SaaS and Cloud&nbsp;...',
    'cacheId': 'XBKupLSlJR8J',
    'formattedUrl': 'https://jobs.lever.co/.../8f64062b-c557-4a6a-be40-70c057c8a2e2',
    'htmlFormattedUrl': 'https://jobs.lever.co/.../8f64062b-c557-4a6a-be40-70c057c8a2e2',
    'pagemap': {
      'cse_thumbnail': [
        {
          'width': '306',
          'height': '165',
          'src': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRQNabfPIIk51v8AsADS3rDUnaCFVMm6jfTuFxtS67-SSRulUU6F-C5V-RT'
        }
      ],
      'metatags': [
        {
          'viewport': 'width=device-width, initial-scale=1, maximum-scale=1',
          'twitter:title': 'BrightEdge - Back End Developer, Intelligent Experiences',
          'twitter:description': 'Does the idea of developing cutting edge technology make you code for joy? Are you looking for a fast-paced team with ample room for growth? Do you want to make an impact on over 50% of Fortune 500 companies? If so, we need to talk! As the industry pioneer behind Content Performance Marketing, BrightEdge has thoroughly redefined the concept of Search Engine Optimization (SEO) by developing an award-winning platform that precisely measures and optimizes marketing content across online channels. Our cloud-based platform is powered by big data analysis that allows our customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge has emerged as the leading international provider of cloud-based SEO Enterprise solutions due to its dynamic and results oriented entrepreneurial culture. BrightEdge is looking for a Back End Developer to join our Intelligent Experiences product team. Intelligent Experiences manipulates vast amounts of content performanc',
          'twitter:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495228998728.png',
          'og:title': 'BrightEdge - Back End Developer, Intelligent Experiences',
          'og:description': 'Does the idea of developing cutting edge technology make you code for joy? Are you looking for a fast-paced team with ample room for growth? Do you want to make an impact on over 50% of Fortune 500 companies? If so, we need to talk! As the industry pioneer behind Content Performance Marketing, BrightEdge has thoroughly redefined the concept of Search Engine Optimization (SEO) by developing an award-winning platform that precisely measures and optimizes marketing content across online channels. Our cloud-based platform is powered by big data analysis that allows our customers to plan, optimize, and measure campaigns based on real-time content performance. BrightEdge has emerged as the leading international provider of cloud-based SEO Enterprise solutions due to its dynamic and results oriented entrepreneurial culture. BrightEdge is looking for a Back End Developer to join our Intelligent Experiences product team. Intelligent Experiences manipulates vast amounts of content performanc',
          'og:url': 'https://jobs.lever.co/brightedge/8f64062b-c557-4a6a-be40-70c057c8a2e2',
          'og:image': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png',
          'og:image:height': '630',
          'og:image:width': '1200'
        }
      ],
      'cse_image': [
        {
          'src': 'https://lever-client-logos.s3.amazonaws.com/4dd69699-da37-436b-8b6c-826a9752d240-1495229034630.png'
        }
      ]
    }
  }
]

# #local manual per listing test
def get_job_listings_from_google():
    data_get_job_listings_from_google = results_from_GSE_query
    return data_get_job_listings_from_google

# def get_job_listings_from_google(cse_search_term, number_of_listings_to_get = 100):
#     return_value = []
#     try:
#         for search_result_number_from_which_api_query_results_start in range(1, number_of_listings_to_get + 1, MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY):
#             return_value.extend(do_google_search(
#                 # https://i.codefor.cash/job_alerts/generate_subscriber_keywords
#                 # 'site:jobs.lever.co "c++" +engineer'
#                 search_term=cse_search_term,
#                 api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN, num=MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY,
#                 # start=1))
#                 start=search_result_number_from_which_api_query_results_start))
#     except:
#         pass
#     print(return_value[:number_of_listings_to_get])
#     return return_value[:number_of_listings_to_get]

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
    
        # response_per_post = requests.post(
        #     url=CODEFORCASH_BASE_URL+'/api/metum/create',
        #     data=data_to_send_in_request_body)
        
        # with open('responseFromCodeforcash','ab+') as f:
        #     pickle.dump(response_per_post, f)

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
        
