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

results_from_GSE_query = 
[
    {
        "cacheId": "9eBTZxZ1fsIJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/gigya/7dfe08be-62a6-4485-a656-34f859c3f93a",
        "htmlFormattedUrl": "https://jobs.lever.co/gigya/7dfe08be-62a6-4485-a656-34f859c3f93a",
        "htmlSnippet": "Gigya is looking for an experienced software engineer to help develop our next <br>\ngeneration of user management cloud services that reach over 1.5 Billion end&nbsp;...",
        "htmlTitle": "Gigya - Experienced <b>C#</b> Server Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/gigya/7dfe08be-62a6-4485-a656-34f859c3f93a",
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
                    "og:description": "Gigya is looking for an experienced software engineer to help develop our next generation of user management cloud services that reach over 1.5 Billion end users. R&D center is located in Azrieli Towers, in the heart of Tel Aviv. The position is ideally suited to server-side C# engineers looking to challenge themselves in a dynamic, data intensive, highly-distributed computing environment.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1483032404076.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Gigya - Experienced C# Server Developer",
                    "og:url": "https://jobs.lever.co/gigya/7dfe08be-62a6-4485-a656-34f859c3f93a",
                    "twitter:description": "Gigya is looking for an experienced software engineer to help develop our next generation of user management cloud services that reach over 1.5 Billion end users. R&D center is located in Azrieli Towers, in the heart of Tel Aviv. The position is ideally suited to server-side C# engineers looking to challenge themselves in a dynamic, data intensive, highly-distributed computing environment.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1481204313579.png",
                    "twitter:title": "Gigya - Experienced C# Server Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Gigya is looking for an experienced software engineer to help develop our next \ngeneration of user management cloud services that reach over 1.5 Billion end\u00a0...",
        "title": "Gigya - Experienced C# Server Developer"
    },
    {
        "cacheId": "VlCpm9S44JMJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../36d89415-4652-4a6b-bceb-ab40c9adda0b",
        "htmlFormattedUrl": "https://jobs.lever.co/.../36d89415-4652-4a6b-bceb-ab40c9adda0b",
        "htmlSnippet": "Our R&amp;D team works with the latest technologies to create our innovative <br>\nplatform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, <b>C#</b>, Scala, <br>\nInternet&nbsp;...",
        "htmlTitle": "Mendix - <b>C#</b> Data Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/mendix/36d89415-4652-4a6b-bceb-ab40c9adda0b",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "125",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRnynl1eHE8prhfLNU0wZgSen53PbGkIcLcCtJDIaiOQs8dfDzqLHcxsZY",
                    "width": "402"
                }
            ],
            "metatags": [
                {
                    "og:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you. Our team is in control of the backend of our Mendix product, responsible for cre",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Mendix - C# Data Engineer",
                    "og:url": "https://jobs.lever.co/mendix/36d89415-4652-4a6b-bceb-ab40c9adda0b",
                    "twitter:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you. Our team is in control of the backend of our Mendix product, responsible for cre",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644141599.png",
                    "twitter:title": "Mendix - C# Data Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Our R&D team works with the latest technologies to create our innovative \nplatform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, \nInternet\u00a0...",
        "title": "Mendix - C# Data Engineer"
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
    },
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
        "cacheId": "h4Lx4RwiR18J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/cbe7a961-6646-4643-a48f-62d1baab3a6a",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/cbe7a961-6646-4643-a48f-62d1baab3a6a",
        "htmlSnippet": "As a Desktop Clients engineer, you will work with teammates to continuously <br>\ndeliver exciting new features, tune app performance, and evolve the architecture <br>\nof&nbsp;...",
        "htmlTitle": "Twitch - Software Engineer - Desktop Clients (<b>C#</b>)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/cbe7a961-6646-4643-a48f-62d1baab3a6a",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "As a Desktop Clients engineer, you will work with teammates to continuously deliver exciting new features, tune app performance, and evolve the architecture of the Twitch Desktop App. Your work will impact millions gamers on Windows and Mac who use the Twitch Desktop App daily. As gamers ourselves, we share their passion and work continuously to level up the experience in-app. We value engineers with a knack for debugging complex problems, who enjoy learning and working with the latest technologies in client development. In this position you will work with C#, Javascript/Typescript, React, and Electron.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Software Engineer - Desktop Clients (C#)",
                    "og:url": "https://jobs.lever.co/twitch/cbe7a961-6646-4643-a48f-62d1baab3a6a",
                    "twitter:description": "As a Desktop Clients engineer, you will work with teammates to continuously deliver exciting new features, tune app performance, and evolve the architecture of the Twitch Desktop App. Your work will impact millions gamers on Windows and Mac who use the Twitch Desktop App daily. As gamers ourselves, we share their passion and work continuously to level up the experience in-app. We value engineers with a knack for debugging complex problems, who enjoy learning and working with the latest technologies in client development. In this position you will work with C#, Javascript/Typescript, React, and Electron.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Software Engineer - Desktop Clients (C#)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As a Desktop Clients engineer, you will work with teammates to continuously \ndeliver exciting new features, tune app performance, and evolve the architecture \nof\u00a0...",
        "title": "Twitch - Software Engineer - Desktop Clients (C#)"
    },
    {
        "cacheId": "7WaIN7qTVt0J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../b7e93677-6a24-4958-a894-f0a125814d45?...",
        "htmlFormattedUrl": "https://jobs.lever.co/.../b7e93677-6a24-4958-a894-f0a125814d45?...",
        "htmlSnippet": "eFront is a leading software provider of end-to-end solutions dedicated to the <br>\nfinancial industry. eFront&#39;s solutions for cross-asset classes serve more than 800<br>\n&nbsp;...",
        "htmlTitle": "eFront - .Net <b>C#</b> Developer (Test Automation)-Belgrade",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/efront/b7e93677-6a24-4958-a894-f0a125814d45?lever-source=careerwebsite",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5d63bbff-9017-46db-b53a-d22954c68ec4-1470153629563.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "138",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcREJUMYC5P6pS7WpN7q3HjJCaaKUePSj_7UuGAk3qgxSScfO7rewgSn_rY",
                    "width": "365"
                }
            ],
            "metatags": [
                {
                    "og:description": "eFront is a leading software provider of end-to-end solutions dedicated to the financial industry. eFront\u2019s solutions for cross-asset classes serve more than 800 customers in 48 countries, including companies in the private equity, real estate investment, banking and insurance sectors. Founded in 1999, eFront has offices in New York, Montreal, Belgrade, Boston, London, Jersey, Paris (HQ), Dubai, Singapore, Hong Kong and Beijing amongst our 20 global locations. In order to support our constantly growing business, we are looking for a: .Net C# Developer (Test Automation) - Belgrade Department: DevOps Position We are reinforcing our team of seasoned software engineers in charge of the development of Test Frameworks and automated tests for our powerful web based financial software products built over the .NET stack and involving the following technologies and concepts: \u00b7 HTML/Javascript/.NET \u00b7 SQL Server/Oracle \u00b7 Mobility across technologies serving Android",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5d63bbff-9017-46db-b53a-d22954c68ec4-1470153629563.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "eFront - .Net C# Developer (Test Automation)-Belgrade",
                    "og:url": "https://jobs.lever.co/efront/b7e93677-6a24-4958-a894-f0a125814d45",
                    "twitter:description": "eFront is a leading software provider of end-to-end solutions dedicated to the financial industry. eFront\u2019s solutions for cross-asset classes serve more than 800 customers in 48 countries, including companies in the private equity, real estate investment, banking and insurance sectors. Founded in 1999, eFront has offices in New York, Montreal, Belgrade, Boston, London, Jersey, Paris (HQ), Dubai, Singapore, Hong Kong and Beijing amongst our 20 global locations. In order to support our constantly growing business, we are looking for a: .Net C# Developer (Test Automation) - Belgrade Department: DevOps Position We are reinforcing our team of seasoned software engineers in charge of the development of Test Frameworks and automated tests for our powerful web based financial software products built over the .NET stack and involving the following technologies and concepts: \u00b7 HTML/Javascript/.NET \u00b7 SQL Server/Oracle \u00b7 Mobility across technologies serving Android",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/5d63bbff-9017-46db-b53a-d22954c68ec4-1470153616992.png",
                    "twitter:title": "eFront - .Net C# Developer (Test Automation)-Belgrade",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "eFront is a leading software provider of end-to-end solutions dedicated to the \nfinancial industry. eFront's solutions for cross-asset classes serve more than 800\n\u00a0...",
        "title": "eFront - .Net C# Developer (Test Automation)-Belgrade"
    },
    {
        "cacheId": "_szmnVrXtfYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/thredup/c4ff8817-880d-4acc-b62d.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/thredup/c4ff8817-880d-4acc-b62d.../apply",
        "htmlSnippet": "Sr. Software Engineer (<b>C#</b>.net, C++, TCP/IP). San Leandro, CA. Engineering \u2013 <br>\nEngineering - Operations. Full-time. Submit your application. Resume/CV.",
        "htmlTitle": "Sr. Software Engineer (<b>C#</b>.net, C++, TCP/IP)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/thredup/c4ff8817-880d-4acc-b62d-2e2ba1b9ee29/",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/3949d724-5b2b-440d-a2fa-809407ef769f-1494860779713.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "92",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTp4-R7uqwebQIikzMeg3Wxy85I9EkeIEj52r2k1OcJXWwVhTBClzc5GQ",
                    "width": "546"
                }
            ],
            "metatags": [
                {
                    "og:description": "About thredUP thredUP, based in San Francisco, is the leading online marketplace for buying and selling like-new women\u2019s and kids\u2019 clothing. thredUP was founded in 2009 and currently employs nearly 1,000 people across its corporate office and four distribution centers. To date, thredUP has raised $131 million from top-tier investors, most recently closing an $81M equity investment from Goldman Sachs. thredUP\u2019s mission is to inspire a new generation of consumers to think secondhand first. We are achieving this mission being the most convenient solution for busy moms to \u201cclean out\u201d their closets, get organized and do good in the process. thredUP also has the widest and most affordable selection of secondhand clothes in all the name brands customers want to own, in like-new condition. thredUP is growing rapidly, and has built a world-class team that includes investors and executives from Netflix, Virgin, DVF, GAP and Sephora. We are building the leader in the online secondhand apparel m",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/3949d724-5b2b-440d-a2fa-809407ef769f-1494860779713.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "thredUP - Sr. Software Engineer (C#.net, C++, TCP/IP)",
                    "og:url": "https://jobs.lever.co/thredup/c4ff8817-880d-4acc-b62d-2e2ba1b9ee29/apply",
                    "twitter:description": "About thredUP thredUP, based in San Francisco, is the leading online marketplace for buying and selling like-new women\u2019s and kids\u2019 clothing. thredUP was founded in 2009 and currently employs nearly 1,000 people across its corporate office and four distribution centers. To date, thredUP has raised $131 million from top-tier investors, most recently closing an $81M equity investment from Goldman Sachs. thredUP\u2019s mission is to inspire a new generation of consumers to think secondhand first. We are achieving this mission being the most convenient solution for busy moms to \u201cclean out\u201d their closets, get organized and do good in the process. thredUP also has the widest and most affordable selection of secondhand clothes in all the name brands customers want to own, in like-new condition. thredUP is growing rapidly, and has built a world-class team that includes investors and executives from Netflix, Virgin, DVF, GAP and Sephora. We are building the leader in the online secondhand apparel m",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/3949d724-5b2b-440d-a2fa-809407ef769f-1494860086326.png",
                    "twitter:title": "thredUP - Sr. Software Engineer (C#.net, C++, TCP/IP)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Sr. Software Engineer (C#.net, C++, TCP/IP). San Leandro, CA. Engineering \u2013 \nEngineering - Operations. Full-time. Submit your application. Resume/CV.",
        "title": "Sr. Software Engineer (C#.net, C++, TCP/IP)"
    },
    {
        "cacheId": "cU959EbATuAJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/gigya/7dfe08be-62a6-4485-a656.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/gigya/7dfe08be-62a6-4485-a656.../apply",
        "htmlSnippet": "How many years of experience do you have with C#?. 0-2; 3-5; 5+. How many <br>\nyears of experience do you have with server side? 0-2; 3-5; 5+. Do you have <br>\nwork&nbsp;...",
        "htmlTitle": "Gigya - Experienced <b>C#</b> Server Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/gigya/7dfe08be-62a6-4485-a656-34f859c3f93a/",
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
                    "og:description": "Gigya is looking for an experienced software engineer to help develop our next generation of user management cloud services that reach over 1.5 Billion end users. R&D center is located in Azrieli Towers, in the heart of Tel Aviv. The position is ideally suited to server-side C# engineers looking to challenge themselves in a dynamic, data intensive, highly-distributed computing environment.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1483032404076.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Gigya - Experienced C# Server Developer",
                    "og:url": "https://jobs.lever.co/gigya/7dfe08be-62a6-4485-a656-34f859c3f93a/apply",
                    "twitter:description": "Gigya is looking for an experienced software engineer to help develop our next generation of user management cloud services that reach over 1.5 Billion end users. R&D center is located in Azrieli Towers, in the heart of Tel Aviv. The position is ideally suited to server-side C# engineers looking to challenge themselves in a dynamic, data intensive, highly-distributed computing environment.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1481204313579.png",
                    "twitter:title": "Gigya - Experienced C# Server Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "How many years of experience do you have with C#?. 0-2; 3-5; 5+. How many \nyears of experience do you have with server side? 0-2; 3-5; 5+. Do you have \nwork\u00a0...",
        "title": "Gigya - Experienced C# Server Developer"
    },
    {
        "cacheId": "0Rl17urtRr4J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/gigya/efd4f720-56c9-478c-bb30.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/gigya/efd4f720-56c9-478c-bb30.../apply",
        "htmlSnippet": "<b>C#</b> Server Side Team Leader. Tel Aviv, Israel. Engineering. Full-Time. Submit <br>\nyour application. Resume/CV \u2731. ATTACH RESUME/CV. Couldn&#39;t auto-read&nbsp;...",
        "htmlTitle": "Gigya - <b>C#</b> Server Side Team Leader",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/gigya/efd4f720-56c9-478c-bb30-3f6601340c66/",
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
                    "og:url": "https://jobs.lever.co/gigya/efd4f720-56c9-478c-bb30-3f6601340c66/apply",
                    "twitter:description": "Gigya is looking for an experienced, talented team leader ready to take on the challenge of developing our core services. About The Position: Your primary challenge will be to lead a team of experienced programmers developing our SaaS based user management system. The team develops Gigya\u2019s core systems that run at massive scale. You will take an active part on the designing and planning systems with other great team leaders, the head of R&D and our VP architect.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1481204313579.png",
                    "twitter:title": "Gigya - C# Server Side Team Leader",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "C# Server Side Team Leader. Tel Aviv, Israel. Engineering. Full-Time. Submit \nyour application. Resume/CV \u2731. ATTACH RESUME/CV. Couldn't auto-read\u00a0...",
        "title": "Gigya - C# Server Side Team Leader"
    },
    {
        "cacheId": "aST_n9iswjcJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/mendix/ce3d37fb-7a08-4d1e-9c8e.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/mendix/ce3d37fb-7a08-4d1e-9c8e.../apply",
        "htmlSnippet": "<b>C#</b> Developer. Rotterdam. R&amp;D. Full-time. Submit your application. Resume/CV <br>\n\u2731. ATTACH RESUME/CV. Couldn&#39;t auto-read resume. Analyzing resume.",
        "htmlTitle": "Mendix - <b>C#</b> Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/mendix/ce3d37fb-7a08-4d1e-9c8e-770a48602694/",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "125",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRnynl1eHE8prhfLNU0wZgSen53PbGkIcLcCtJDIaiOQs8dfDzqLHcxsZY",
                    "width": "402"
                }
            ],
            "metatags": [
                {
                    "og:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you. The Desktop Modeler team develops our IDE, the Mendix Modeler, creating high-tech",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Mendix - C# Developer",
                    "og:url": "https://jobs.lever.co/mendix/ce3d37fb-7a08-4d1e-9c8e-770a48602694/apply",
                    "twitter:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you. The Desktop Modeler team develops our IDE, the Mendix Modeler, creating high-tech",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644141599.png",
                    "twitter:title": "Mendix - C# Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "C# Developer. Rotterdam. R&D. Full-time. Submit your application. Resume/CV \n\u2731. ATTACH RESUME/CV. Couldn't auto-read resume. Analyzing resume.",
        "title": "Mendix - C# Developer"
    },
    {
        "cacheId": "WrvCYLxrT4EJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/efront/b7e93677-6a24-4958-a894.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/efront/b7e93677-6a24-4958-a894.../apply",
        "htmlSnippet": ".Net <b>C#</b> Developer (Test Automation)-Belgrade. Belgrade. Product &amp; Dev Ops. <br>\nFull-time. Submit your application. Resume/CV \u2731. ATTACH RESUME/CV.",
        "htmlTitle": "eFront - .Net <b>C#</b> Developer (Test Automation)-Belgrade",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/efront/b7e93677-6a24-4958-a894-f0a125814d45/",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5d63bbff-9017-46db-b53a-d22954c68ec4-1470153629563.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "138",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcREJUMYC5P6pS7WpN7q3HjJCaaKUePSj_7UuGAk3qgxSScfO7rewgSn_rY",
                    "width": "365"
                }
            ],
            "metatags": [
                {
                    "og:description": "eFront is a leading software provider of end-to-end solutions dedicated to the financial industry. eFront\u2019s solutions for cross-asset classes serve more than 800 customers in 48 countries, including companies in the private equity, real estate investment, banking and insurance sectors. Founded in 1999, eFront has offices in New York, Montreal, Belgrade, Boston, London, Jersey, Paris (HQ), Dubai, Singapore, Hong Kong and Beijing amongst our 20 global locations. In order to support our constantly growing business, we are looking for a: .Net C# Developer (Test Automation) - Belgrade Department: DevOps Position We are reinforcing our team of seasoned software engineers in charge of the development of Test Frameworks and automated tests for our powerful web based financial software products built over the .NET stack and involving the following technologies and concepts: \u00b7 HTML/Javascript/.NET \u00b7 SQL Server/Oracle \u00b7 Mobility across technologies serving Android",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5d63bbff-9017-46db-b53a-d22954c68ec4-1470153629563.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "eFront - .Net C# Developer (Test Automation)-Belgrade",
                    "og:url": "https://jobs.lever.co/efront/b7e93677-6a24-4958-a894-f0a125814d45/apply",
                    "twitter:description": "eFront is a leading software provider of end-to-end solutions dedicated to the financial industry. eFront\u2019s solutions for cross-asset classes serve more than 800 customers in 48 countries, including companies in the private equity, real estate investment, banking and insurance sectors. Founded in 1999, eFront has offices in New York, Montreal, Belgrade, Boston, London, Jersey, Paris (HQ), Dubai, Singapore, Hong Kong and Beijing amongst our 20 global locations. In order to support our constantly growing business, we are looking for a: .Net C# Developer (Test Automation) - Belgrade Department: DevOps Position We are reinforcing our team of seasoned software engineers in charge of the development of Test Frameworks and automated tests for our powerful web based financial software products built over the .NET stack and involving the following technologies and concepts: \u00b7 HTML/Javascript/.NET \u00b7 SQL Server/Oracle \u00b7 Mobility across technologies serving Android",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/5d63bbff-9017-46db-b53a-d22954c68ec4-1470153616992.png",
                    "twitter:title": "eFront - .Net C# Developer (Test Automation)-Belgrade",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": ".Net C# Developer (Test Automation)-Belgrade. Belgrade. Product & Dev Ops. \nFull-time. Submit your application. Resume/CV \u2731. ATTACH RESUME/CV.",
        "title": "eFront - .Net C# Developer (Test Automation)-Belgrade"
    },
    {
        "cacheId": "WuwQfIv3l9IJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/avecto/57ba7159-2c0c-47d5-b293.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/avecto/57ba7159-2c0c-47d5-b293.../apply",
        "htmlSnippet": "Senior Software Engineer <b>C#</b>. UK, Manchester. Engineering \u2013 Development. Full <br>\nTime. Submit your application. Resume/CV \u2731. ATTACH RESUME/CV. Couldn&#39;t&nbsp;...",
        "htmlTitle": "Avecto - Senior Software Engineer <b>C#</b>",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/avecto/57ba7159-2c0c-47d5-b293-0468e5bb9259/",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/02ec5539-ed42-4a6c-bf0c-b13151b02795-1497528767450.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "109",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSumPri1vDbmLVUzT0XSNVQtHYE7xslAr8f5W71X3LzskONK_oHZEOTfKo",
                    "width": "460"
                }
            ],
            "metatags": [
                {
                    "og:description": "The position (what you\u2019ll do): o Play a key part in the design, architecture and development of our product suite o Research, prototype and on board new technologies if they can bring us a competitive edge. o Use agile tools and techniques to play a full part in all aspects of the software development lifecycle o Cope with pressure of conflicting requirements and adept at context switching o Use advanced debugging techniques to diagnose and fix problems o Demonstrate the ability to drive change, be innovative and mentor more Junior engineers, whilst hitting tight deadlines o Act as a mentor to more junior members of the team What you have to offer: o Experience of working on secure enterprise systems o Knowledge of Agile methodologies o Experience of mentoring, supporting and guiding a team within all technical aspects o Excellent interpersonal skills o OO design o Writing multithreaded software o Designing for performance, security & stability o Unit te",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/02ec5539-ed42-4a6c-bf0c-b13151b02795-1497528767450.png",
                    "og:image:height": "200",
                    "og:title": "Avecto - Senior Software Engineer C#",
                    "og:url": "https://jobs.lever.co/avecto/57ba7159-2c0c-47d5-b293-0468e5bb9259/apply",
                    "twitter:description": "The position (what you\u2019ll do): o Play a key part in the design, architecture and development of our product suite o Research, prototype and on board new technologies if they can bring us a competitive edge. o Use agile tools and techniques to play a full part in all aspects of the software development lifecycle o Cope with pressure of conflicting requirements and adept at context switching o Use advanced debugging techniques to diagnose and fix problems o Demonstrate the ability to drive change, be innovative and mentor more Junior engineers, whilst hitting tight deadlines o Act as a mentor to more junior members of the team What you have to offer: o Experience of working on secure enterprise systems o Knowledge of Agile methodologies o Experience of mentoring, supporting and guiding a team within all technical aspects o Excellent interpersonal skills o OO design o Writing multithreaded software o Designing for performance, security & stability o Unit te",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/02ec5539-ed42-4a6c-bf0c-b13151b02795-1497528998385.png",
                    "twitter:title": "Avecto - Senior Software Engineer C#",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Senior Software Engineer C#. UK, Manchester. Engineering \u2013 Development. Full \nTime. Submit your application. Resume/CV \u2731. ATTACH RESUME/CV. Couldn't\u00a0...",
        "title": "Avecto - Senior Software Engineer C#"
    },
    {
        "cacheId": "80SGMXaDPMsJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../2ee4a8da-caad-44c3-b869-88604289f60a",
        "htmlFormattedUrl": "https://jobs.lever.co/.../2ee4a8da-caad-44c3-b869-88604289f60a",
        "htmlSnippet": "You&#39;ll use <b>C#</b> to implement high performance web services backed by Redis, <br>\nDynamoDB, SQL server, etc. You&#39;ll be a key player in designing and refining&nbsp;...",
        "htmlTitle": "BoomTown - Senior Software Engineer (<b>c#</b>)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/boomtownroi.com/2ee4a8da-caad-44c3-b869-88604289f60a",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/035d99be-98af-422a-aeb3-25d8c844018f-1468443033584.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRriALjfc-FHmorRLrF57SqKQ3DE7rrCgRuPs-6mpHIG6wQNoofhrq3Fcg",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "What we do: As a Software Engineer on the Foundation team, you provide the web services, messaging systems, data stores, and other server-side systems our product teams need to get their job done quickly and easily. You\u2019ll be charged with continuously enhancing and reinventing BoomTown\u2019s server side platform. You\u2019ll use C# to implement high performance web services backed by Redis, DynamoDB, SQL server, etc. You\u2019ll be a key player in designing and refining BoomTown\u2019s server side APIs.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/035d99be-98af-422a-aeb3-25d8c844018f-1468443033584.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "BoomTown - Senior Software Engineer (c#)",
                    "og:url": "https://jobs.lever.co/boomtownroi.com/2ee4a8da-caad-44c3-b869-88604289f60a",
                    "twitter:description": "What we do: As a Software Engineer on the Foundation team, you provide the web services, messaging systems, data stores, and other server-side systems our product teams need to get their job done quickly and easily. You\u2019ll be charged with continuously enhancing and reinventing BoomTown\u2019s server side platform. You\u2019ll use C# to implement high performance web services backed by Redis, DynamoDB, SQL server, etc. You\u2019ll be a key player in designing and refining BoomTown\u2019s server side APIs.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/035d99be-98af-422a-aeb3-25d8c844018f-1468443025221.png",
                    "twitter:title": "BoomTown - Senior Software Engineer (c#)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "You'll use C# to implement high performance web services backed by Redis, \nDynamoDB, SQL server, etc. You'll be a key player in designing and refining\u00a0...",
        "title": "BoomTown - Senior Software Engineer (c#)"
    },
    {
        "cacheId": "e5z_rNZQbXIJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/gigya/4d49a34f-9099-489d-a31b.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/gigya/4d49a34f-9099-489d-a31b.../apply",
        "htmlSnippet": "Senior <b>C#</b> Infrastructure/server developer. Tel Aviv, Israel. Engineering. Full-time. <br>\nSubmit your application. Resume/CV \u2731. ATTACH RESUME/CV. Couldn&#39;t&nbsp;...",
        "htmlTitle": "Gigya - Senior <b>C#</b> Infrastructure/server developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/gigya/4d49a34f-9099-489d-a31b-503ee85c7361/",
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
                    "og:url": "https://jobs.lever.co/gigya/4d49a34f-9099-489d-a31b-503ee85c7361/apply",
                    "twitter:description": "Gigya\u2019s R&D center in Azrieli towers in Tel-Aviv is looking for a senior C# developer with strong software engineering skills, to develop high-quality, advanced infrastructures and micro-services for use by other R&D teams in the company.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1481204313579.png",
                    "twitter:title": "Gigya - Senior C# Infrastructure/server developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Senior C# Infrastructure/server developer. Tel Aviv, Israel. Engineering. Full-time. \nSubmit your application. Resume/CV \u2731. ATTACH RESUME/CV. Couldn't\u00a0...",
        "title": "Gigya - Senior C# Infrastructure/server developer"
    },
    {
        "cacheId": "kPlPSRso7mcJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../450f8f64-52c5-4185-a465-7807e25ff616",
        "htmlFormattedUrl": "https://jobs.lever.co/.../450f8f64-52c5-4185-a465-7807e25ff616",
        "htmlSnippet": "We are building a desktop application in <b>C#</b> (we use the latest version) using <br>\nWPF because we need to support the user which are running on Windows 7.",
        "htmlTitle": "PlanGrid - Windows Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/plangrid/450f8f64-52c5-4185-a465-7807e25ff616",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/c64b81a2-4ba4-48d3-a8b7-53d0a86cc731-1481912401269.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "115",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTV89eyqm3YTp_-k7FD9JmZve1poG8PXwevCltjKaRaeSeLEa56FS1X0Yo",
                    "width": "438"
                }
            ],
            "metatags": [
                {
                    "og:description": "About the Role: PlanGrid is on a mission to build the future faster by creating beautiful software for construction, one of the oldest an largest industries on the planet. We\u2019re changing that by building tools that automate the mundane tasks around collaboration, planning and version control (think version control for blueprints). Our users are building some of the most amazing construction projects in the world, and our platform is their central information point. As a Windows Engineer, you will tackle some very difficult and interesting challenges. Things like: - Building near real-time collaboration and markup for construction drawings - Building slick and responsive UI that can handle millions of user generated data points (like photos and annotations) - Replacing Excel workflows with simple, powerful tools that work great on mobile devices (both phones and tablets) - Build unique user experiences for large scale displays (Surface Hub) - Integrating with existing construction sof",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/c64b81a2-4ba4-48d3-a8b7-53d0a86cc731-1481912401269.png",
                    "og:image:height": "200",
                    "og:title": "PlanGrid - Windows Engineer",
                    "og:url": "https://jobs.lever.co/plangrid/450f8f64-52c5-4185-a465-7807e25ff616",
                    "twitter:description": "About the Role: PlanGrid is on a mission to build the future faster by creating beautiful software for construction, one of the oldest an largest industries on the planet. We\u2019re changing that by building tools that automate the mundane tasks around collaboration, planning and version control (think version control for blueprints). Our users are building some of the most amazing construction projects in the world, and our platform is their central information point. As a Windows Engineer, you will tackle some very difficult and interesting challenges. Things like: - Building near real-time collaboration and markup for construction drawings - Building slick and responsive UI that can handle millions of user generated data points (like photos and annotations) - Replacing Excel workflows with simple, powerful tools that work great on mobile devices (both phones and tablets) - Build unique user experiences for large scale displays (Surface Hub) - Integrating with existing construction sof",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/c64b81a2-4ba4-48d3-a8b7-53d0a86cc731-1481912543966.png",
                    "twitter:title": "PlanGrid - Windows Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We are building a desktop application in C# (we use the latest version) using \nWPF because we need to support the user which are running on Windows 7.",
        "title": "PlanGrid - Windows Engineer"
    },
    {
        "cacheId": "r9cbDeiOJ5wJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/4bf8046f-aab3-4151-a6e0-d21ec251f38e",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/4bf8046f-aab3-4151-a6e0-d21ec251f38e",
        "htmlSnippet": "Working on Mac-specific features; Help maintain and evolve existing <b>C#</b> <br>\ncodebase shared between Windows and Mac; Write maintainable code with <br>\nextensive&nbsp;...",
        "htmlTitle": "Twitch - Software Engineer, Mac",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/4bf8046f-aab3-4151-a6e0-d21ec251f38e",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Mac is an important piece of our desktop application strategy. As a software engineer, you\u2019ll be working on the Twitch Desktop Application for the Mac platform.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "512",
                    "og:image:width": "1024",
                    "og:title": "Twitch - Software Engineer, Mac",
                    "og:url": "https://jobs.lever.co/twitch/4bf8046f-aab3-4151-a6e0-d21ec251f38e",
                    "twitter:description": "We are rapidly expanding the engineering team at Twitch to deal with challenging scale problem of being the 4th biggest consumer of bandwidth and one of the largest social gaming experiences in the world. Mac is an important piece of our desktop application strategy. As a software engineer, you\u2019ll be working on the Twitch Desktop Application for the Mac platform.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Software Engineer, Mac",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Working on Mac-specific features; Help maintain and evolve existing C# \ncodebase shared between Windows and Mac; Write maintainable code with \nextensive\u00a0...",
        "title": "Twitch - Software Engineer, Mac"
    },
    {
        "cacheId": "qfG-TKMYX9IJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../4758cb3d-e575-425d-bbf3-d622d1ab6bef?...",
        "htmlFormattedUrl": "https://jobs.lever.co/.../4758cb3d-e575-425d-bbf3-d622d1ab6bef?...",
        "htmlSnippet": "Strong knowledge of <b>C#</b> and SQL, previous experience will be positively <br>\nconsidered. \u00b7 Able to autonomously dig into an existing codebase and <br>\nunderstand its&nbsp;...",
        "htmlTitle": "eFront - Full Stack Functional Developer-Belgrade",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/efront/4758cb3d-e575-425d-bbf3-d622d1ab6bef?lever-source=careerwebsite",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5d63bbff-9017-46db-b53a-d22954c68ec4-1470153629563.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "138",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcREJUMYC5P6pS7WpN7q3HjJCaaKUePSj_7UuGAk3qgxSScfO7rewgSn_rY",
                    "width": "365"
                }
            ],
            "metatags": [
                {
                    "og:description": "eFront is a leading software provider of end-to-end solutions dedicated to the financial industry. eFront\u2019s solutions for cross-asset classes serve more than 800 customers in 48 countries, including companies in the private equity, real estate investment, banking and insurance sectors. Founded in 1999, eFront has offices in New York, Montreal, Belgrade, Boston, London, Jersey, Paris (HQ), Dubai, Singapore, Hong Kong and Beijing amongst our 20 global locations. In order to support our constantly growing business, we are looking for: Full Stack Functional Developer-Belgrade Department : DevOps Position Fully integrated to our .Net Engineering Team in Belgrade, you will be exposed to both the technical and functional layers of our flagship product, while acquiring a unique skillset on the fast growing Private Equity industry, and Alternative Finance in general. As a member of an international team, you will also learn how to work in a global Agile company. High achievers will be rewar",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5d63bbff-9017-46db-b53a-d22954c68ec4-1470153629563.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "eFront - Full Stack Functional Developer-Belgrade",
                    "og:url": "https://jobs.lever.co/efront/4758cb3d-e575-425d-bbf3-d622d1ab6bef",
                    "twitter:description": "eFront is a leading software provider of end-to-end solutions dedicated to the financial industry. eFront\u2019s solutions for cross-asset classes serve more than 800 customers in 48 countries, including companies in the private equity, real estate investment, banking and insurance sectors. Founded in 1999, eFront has offices in New York, Montreal, Belgrade, Boston, London, Jersey, Paris (HQ), Dubai, Singapore, Hong Kong and Beijing amongst our 20 global locations. In order to support our constantly growing business, we are looking for: Full Stack Functional Developer-Belgrade Department : DevOps Position Fully integrated to our .Net Engineering Team in Belgrade, you will be exposed to both the technical and functional layers of our flagship product, while acquiring a unique skillset on the fast growing Private Equity industry, and Alternative Finance in general. As a member of an international team, you will also learn how to work in a global Agile company. High achievers will be rewar",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/5d63bbff-9017-46db-b53a-d22954c68ec4-1470153616992.png",
                    "twitter:title": "eFront - Full Stack Functional Developer-Belgrade",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Strong knowledge of C# and SQL, previous experience will be positively \nconsidered. \u00b7 Able to autonomously dig into an existing codebase and \nunderstand its\u00a0...",
        "title": "eFront - Full Stack Functional Developer-Belgrade"
    },
    {
        "cacheId": "wrPgpjRiqVgJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../ceca12e0-94aa-4899-adf3-3d8e6d32013e",
        "htmlFormattedUrl": "https://jobs.lever.co/.../ceca12e0-94aa-4899-adf3-3d8e6d32013e",
        "htmlSnippet": "Strong programming skills in at least one of an object oriented {Scala, Java, C++, <br>\n<b>C#</b>, Python, etc}, functional programming {Scala, <b>C#</b>, Haskell, OCaML/SML,&nbsp;...",
        "htmlTitle": "CiBO Technologies - Crop Model Scientist - Cambridge",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/cibotechnologies/ceca12e0-94aa-4899-adf3-3d8e6d32013e",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/dd2e0aa0-4905-44cc-a2a4-d74d85838438-1492695934888.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "121",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSkmNvkyMjhJq32mxdKanJki0nAy_6paCQ_h3P1jKJ5K5DpyaPXOcgPUQ",
                    "width": "415"
                }
            ],
            "metatags": [
                {
                    "og:description": "As a Crop Model Scientist at CiBO you\u2019ll be part of a collaborative team of developers, data scientists, agronomists, and remote sensing experts. You will help build customer facing applications and our core platform to create, improve, and scale agricultural models and optimization. Our culture is built on cross-disciplinary collaboration, learning, and rapid prototyping. As engineers, we believe in types, tests, functional programming, and automation. Our major platform is built on Scala in AWS, with sprinklings of R. CiBO is a science-based company, so prepare to learn and invent with us! Software is a creative process and we welcome non-traditional and diverse candidates to apply. Qualifications Solid foundation in plant physiology with particular emphasis on agriculture and current agronomic best practices Significant experience with modeling crop development phases, growth, stresses, and interactions with biotic and abiotic factors, especially creation of models with different b",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/dd2e0aa0-4905-44cc-a2a4-d74d85838438-1492695934888.png",
                    "og:image:height": "200",
                    "og:title": "CiBO Technologies - Crop Model Scientist - Cambridge",
                    "og:url": "https://jobs.lever.co/cibotechnologies/ceca12e0-94aa-4899-adf3-3d8e6d32013e",
                    "twitter:description": "As a Crop Model Scientist at CiBO you\u2019ll be part of a collaborative team of developers, data scientists, agronomists, and remote sensing experts. You will help build customer facing applications and our core platform to create, improve, and scale agricultural models and optimization. Our culture is built on cross-disciplinary collaboration, learning, and rapid prototyping. As engineers, we believe in types, tests, functional programming, and automation. Our major platform is built on Scala in AWS, with sprinklings of R. CiBO is a science-based company, so prepare to learn and invent with us! Software is a creative process and we welcome non-traditional and diverse candidates to apply. Qualifications Solid foundation in plant physiology with particular emphasis on agriculture and current agronomic best practices Significant experience with modeling crop development phases, growth, stresses, and interactions with biotic and abiotic factors, especially creation of models with different b",
                    "twitter:title": "CiBO Technologies - Crop Model Scientist - Cambridge",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Strong programming skills in at least one of an object oriented {Scala, Java, C++, \nC#, Python, etc}, functional programming {Scala, C#, Haskell, OCaML/SML,\u00a0...",
        "title": "CiBO Technologies - Crop Model Scientist - Cambridge"
    },
    {
        "cacheId": "seuvPOpb3SwJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../af546f4d-8227-4ec2-a0a0-78ebf80f05c1",
        "htmlFormattedUrl": "https://jobs.lever.co/.../af546f4d-8227-4ec2-a0a0-78ebf80f05c1",
        "htmlSnippet": "Expert-level experience with Unity Game Engine; Expert in scripting with <b>C#</b> <br>\nwithin the Unity environment; Experience creating real-time visual effects&nbsp;...",
        "htmlTitle": "Niantic inc. - Unity Technical Artist",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/nianticlabs/af546f4d-8227-4ec2-a0a0-78ebf80f05c1",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/6688674a-c350-45c0-b279-9d840d40e025-1483483457557.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "276",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSyWpN5dU3tO9vFJdnR2mvJDq3mW1VGgpH8Ah8Rd8NyBxeH3qivcVMvk7B0",
                    "width": "182"
                }
            ],
            "metatags": [
                {
                    "og:description": "Niantic Labs, creator of Ingress and Pok\u00e9mon GO, seeks a Unity Technical Artist with creative and technical expertise to develop challenging Unity scenes. Niantic is a fast-moving, multi-disciplinary team of software developers and creative professionals based in San Francisco and Seattle. You will be responsible for working with Unity and other graphics tools to merge the virtual with the real world.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/6688674a-c350-45c0-b279-9d840d40e025-1483483457557.png",
                    "og:image:height": "200",
                    "og:title": "Niantic inc. - Unity Technical Artist",
                    "og:url": "https://jobs.lever.co/nianticlabs/af546f4d-8227-4ec2-a0a0-78ebf80f05c1",
                    "twitter:description": "Niantic Labs, creator of Ingress and Pok\u00e9mon GO, seeks a Unity Technical Artist with creative and technical expertise to develop challenging Unity scenes. Niantic is a fast-moving, multi-disciplinary team of software developers and creative professionals based in San Francisco and Seattle. You will be responsible for working with Unity and other graphics tools to merge the virtual with the real world.",
                    "twitter:title": "Niantic inc. - Unity Technical Artist",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Expert-level experience with Unity Game Engine; Expert in scripting with C# \nwithin the Unity environment; Experience creating real-time visual effects\u00a0...",
        "title": "Niantic inc. - Unity Technical Artist"
    },
    {
        "cacheId": "DL8xqgPDu1cJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/63a55490-942f-4717-ac81-c86c31dad2ae",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/63a55490-942f-4717-ac81-c86c31dad2ae",
        "htmlSnippet": "As a software engineer working on the Client Platforms Engineering (CPE) team <br>\nyou will help develop the systems and services powering the next generation of&nbsp;...",
        "htmlTitle": "Twitch - Backend Engineer, Infrastructure (<b>C#</b>)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/63a55490-942f-4717-ac81-c86c31dad2ae",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "As a software engineer working on the Client Platforms Engineering (CPE) team you will help develop the systems and services powering the next generation of Twitch clients. We in CPE strive to provide Twitch developers the best development platform as well as building robust services for the deployed applications. The tools and services you develop will be used by hundreds of developers and help enhance the Twitch.tv experience for millions.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Backend Engineer, Infrastructure (C#)",
                    "og:url": "https://jobs.lever.co/twitch/63a55490-942f-4717-ac81-c86c31dad2ae",
                    "twitter:description": "As a software engineer working on the Client Platforms Engineering (CPE) team you will help develop the systems and services powering the next generation of Twitch clients. We in CPE strive to provide Twitch developers the best development platform as well as building robust services for the deployed applications. The tools and services you develop will be used by hundreds of developers and help enhance the Twitch.tv experience for millions.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Backend Engineer, Infrastructure (C#)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "As a software engineer working on the Client Platforms Engineering (CPE) team \nyou will help develop the systems and services powering the next generation of\u00a0...",
        "title": "Twitch - Backend Engineer, Infrastructure (C#)"
    },
    {
        "cacheId": "TmvchvsnQQoJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../6828281f-ebfa-4eec-9c05-0e6b2fa4dd00",
        "htmlFormattedUrl": "https://jobs.lever.co/.../6828281f-ebfa-4eec-9c05-0e6b2fa4dd00",
        "htmlSnippet": "3+ years of experience in executing detailed test cases, test plans and test <br>\ndesign documents; Strong programming skills desired (JavaScript, <b>C#</b> or Ruby)&nbsp;...",
        "htmlTitle": "Plethora - QA Automation Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/plethora/6828281f-ebfa-4eec-9c05-0e6b2fa4dd00",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5e325818-48b2-47c3-bce0-2ee0abaa3d92-1483574051428.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "66",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQ8L6cPsHN4Q8TN2em6nj99HiXdkARMvEPzha67AaHYmgDLx_SlURaFVQ",
                    "width": "600"
                }
            ],
            "metatags": [
                {
                    "og:description": "Plethora is building the future of manufacturing - a new kind of automated factory that turns digital designs into physical products in days, not months with our internally developed software and fully-integrated factory system. We are a uniquely ambitious company funded by some of the biggest names, such as Founders Fund, Lux Capital, Google, and Autodesk. Our organization is already impacting the short-run manufacturing space, with a category-leading NPS, in the $21B addressable market that is ripe for disruption. You will be collaborating with a small team of skilled Software Engineers and Product Managers to work on new strategic projects. Together with an agile team develop and translate business goals into high quality, reliable and scalable technology. In order to deliver faster and set a high quality bar we invest the time and commitment to automating tests.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5e325818-48b2-47c3-bce0-2ee0abaa3d92-1483574051428.png",
                    "og:image:height": "200",
                    "og:title": "Plethora - QA Automation Engineer",
                    "og:url": "https://jobs.lever.co/plethora/6828281f-ebfa-4eec-9c05-0e6b2fa4dd00",
                    "twitter:description": "Plethora is building the future of manufacturing - a new kind of automated factory that turns digital designs into physical products in days, not months with our internally developed software and fully-integrated factory system. We are a uniquely ambitious company funded by some of the biggest names, such as Founders Fund, Lux Capital, Google, and Autodesk. Our organization is already impacting the short-run manufacturing space, with a category-leading NPS, in the $21B addressable market that is ripe for disruption. You will be collaborating with a small team of skilled Software Engineers and Product Managers to work on new strategic projects. Together with an agile team develop and translate business goals into high quality, reliable and scalable technology. In order to deliver faster and set a high quality bar we invest the time and commitment to automating tests.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/5e325818-48b2-47c3-bce0-2ee0abaa3d92-1479853206515.png",
                    "twitter:title": "Plethora - QA Automation Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "3+ years of experience in executing detailed test cases, test plans and test \ndesign documents; Strong programming skills desired (JavaScript, C# or Ruby)\u00a0...",
        "title": "Plethora - QA Automation Engineer"
    },
    {
        "cacheId": "WI473bVKHyYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../7ecb407c-c9a1-4451-a307-17fe0d46a55e",
        "htmlFormattedUrl": "https://jobs.lever.co/.../7ecb407c-c9a1-4451-a307-17fe0d46a55e",
        "htmlSnippet": "2+ years experience programming experience in Java, Javascript, C/C++, <b>C#</b>, <br>\nObjective-C, Python, and/or Ruby. At least one of following web framework&nbsp;...",
        "htmlTitle": "Udacity - Senior Full Stack Developer, Marketing",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/udacity/7ecb407c-c9a1-4451-a307-17fe0d46a55e",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1456507702873.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "225",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQimNZAwidOK_Ars6vYyVtRY1_FtGEDoahzlFur2hKcDON4NHx0ftTBR1I",
                    "width": "225"
                }
            ],
            "metatags": [
                {
                    "og:description": "Udacity's mission is to democratize education. We're an online learning platform offering groundbreaking education in fields such as artificial intelligence, machine learning, robotics, virtual reality, and more. Focused on self-empowerment through learning, Udacity is making innovative technologies such as self-driving cars available to a global community of aspiring technologists, while also enabling learners at all levels to skill up with essentials like programming, web and app development. Udacity is looking for people to join our Marketing team. If you love a challenge, and truly want to make a difference in the world, read on! As a key member of the our Growth/Marketing team, you will be helping us bring accessible, affordable, engaging, and highly effective higher education to the world. You will be working on new products to acquire and grow our students base, new platform to leverage user behavior data to increase conversion rate, also new tool to improving SEO result. The u",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1456507702873.png",
                    "og:image:height": "200",
                    "og:title": "Udacity - Senior Full Stack Developer, Marketing",
                    "og:url": "https://jobs.lever.co/udacity/7ecb407c-c9a1-4451-a307-17fe0d46a55e",
                    "twitter:description": "Udacity's mission is to democratize education. We're an online learning platform offering groundbreaking education in fields such as artificial intelligence, machine learning, robotics, virtual reality, and more. Focused on self-empowerment through learning, Udacity is making innovative technologies such as self-driving cars available to a global community of aspiring technologists, while also enabling learners at all levels to skill up with essentials like programming, web and app development. Udacity is looking for people to join our Marketing team. If you love a challenge, and truly want to make a difference in the world, read on! As a key member of the our Growth/Marketing team, you will be helping us bring accessible, affordable, engaging, and highly effective higher education to the world. You will be working on new products to acquire and grow our students base, new platform to leverage user behavior data to increase conversion rate, also new tool to improving SEO result. The u",
                    "twitter:title": "Udacity - Senior Full Stack Developer, Marketing",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "2+ years experience programming experience in Java, Javascript, C/C++, C#, \nObjective-C, Python, and/or Ruby. At least one of following web framework\u00a0...",
        "title": "Udacity - Senior Full Stack Developer, Marketing"
    },
    {
        "cacheId": "Kb4JfjvTLbsJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../56d76fc9-9fc4-4dd1-a352-e554445ccaaa",
        "htmlFormattedUrl": "https://jobs.lever.co/.../56d76fc9-9fc4-4dd1-a352-e554445ccaaa",
        "htmlSnippet": "Actively searching for bright and talented software engineers to support the Drug <br>\nEnforcement Administration&#39;s application development initiatives.",
        "htmlTitle": "Lazerline Solutions - Sr. <b>C#</b>/.NET Software Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/lazerlinesolutions/56d76fc9-9fc4-4dd1-a352-e554445ccaaa",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/4b64606c-d19b-477f-aa6b-bfdf6bb34fa7-1472481053413.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "185",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQA1VBgvH9468HsPe4hNp_4tjnm8FTkjJm-au_4QpMF_Gs6jPRARnsccyo",
                    "width": "272"
                }
            ],
            "metatags": [
                {
                    "og:description": "*** LOCATION: STERLING, VA and ARLINGTON, VA *** General/Overview Actively searching for bright and talented software engineers to support the Drug Enforcement Administration\u2019s application development initiatives. Our engineers develop cutting-edge applications that directly enable DEA to further its mission. Our client and DEA are avid practitioners of agile development methodologies, and most of our work is done in a purely agile environment. We use Scrum, continuous integration, and peer reviews on a daily basis, and we adhere to the \u201cinspect and adapt\u201d principle as we seek new ways to innovate. We are looking for more than a set of programming skills \u2013 we are interested in your experiences, talents, interests, and enthusiasm for the craftsmanship and engineering aspects of software development. Our engineers understand and use design patterns, SOLID principles, mocks and fakes, and unit tests. In addition to being technology enthusiasts, we are also passionate about deliverin",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/4b64606c-d19b-477f-aa6b-bfdf6bb34fa7-1472481053413.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Lazerline Solutions - Sr. C#/.NET Software Developer",
                    "og:url": "https://jobs.lever.co/lazerlinesolutions/56d76fc9-9fc4-4dd1-a352-e554445ccaaa",
                    "twitter:description": "*** LOCATION: STERLING, VA and ARLINGTON, VA *** General/Overview Actively searching for bright and talented software engineers to support the Drug Enforcement Administration\u2019s application development initiatives. Our engineers develop cutting-edge applications that directly enable DEA to further its mission. Our client and DEA are avid practitioners of agile development methodologies, and most of our work is done in a purely agile environment. We use Scrum, continuous integration, and peer reviews on a daily basis, and we adhere to the \u201cinspect and adapt\u201d principle as we seek new ways to innovate. We are looking for more than a set of programming skills \u2013 we are interested in your experiences, talents, interests, and enthusiasm for the craftsmanship and engineering aspects of software development. Our engineers understand and use design patterns, SOLID principles, mocks and fakes, and unit tests. In addition to being technology enthusiasts, we are also passionate about deliverin",
                    "twitter:title": "Lazerline Solutions - Sr. C#/.NET Software Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Actively searching for bright and talented software engineers to support the Drug \nEnforcement Administration's application development initiatives.",
        "title": "Lazerline Solutions - Sr. C#/.NET Software Developer"
    },
    {
        "cacheId": "9Q6LSPwEjLMJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../f6c0bdeb-5fd5-4af7-b248-306e72017c4e",
        "htmlFormattedUrl": "https://jobs.lever.co/.../f6c0bdeb-5fd5-4af7-b248-306e72017c4e",
        "htmlSnippet": "Requirements: Bachelors or Masters degree in Computer Science, Math or <br>\nequivalent experience; 5+ years experience designing and coding in Java, C++, <br>\n<b>C#</b>,&nbsp;...",
        "htmlTitle": "98point6 - Senior Software Back-End Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/98point6/f6c0bdeb-5fd5-4af7-b248-306e72017c4e",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/0b349ccf-4d94-4dbf-bb00-adf96740f692-1468266929348.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNuBTs2L5Fdp7qTbF1iq-GPZ-6bUP6ozjRcffAyJF67vKsA744qW9i3Isi",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "98point6 is building the next generation of primary care by changing the relationship between healthcare and technology. By uniting leading-edge data science with Board Certified Physicians we are working to make primary care more convenient, accessible, and affordable. As we grow, you will have room to grow alongside us and impact the future of healthcare. Your role and impact As a senior software engineer working at 98point6 you will get firsthand experience with technologies such as semantic databases, machine learning, and natural language processing; and you will be surrounded by people who are smart and passionate about both our social and technical missions.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/0b349ccf-4d94-4dbf-bb00-adf96740f692-1468266929348.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "98point6 - Senior Software Back-End Engineer",
                    "og:url": "https://jobs.lever.co/98point6/f6c0bdeb-5fd5-4af7-b248-306e72017c4e",
                    "twitter:description": "98point6 is building the next generation of primary care by changing the relationship between healthcare and technology. By uniting leading-edge data science with Board Certified Physicians we are working to make primary care more convenient, accessible, and affordable. As we grow, you will have room to grow alongside us and impact the future of healthcare. Your role and impact As a senior software engineer working at 98point6 you will get firsthand experience with technologies such as semantic databases, machine learning, and natural language processing; and you will be surrounded by people who are smart and passionate about both our social and technical missions.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/0b349ccf-4d94-4dbf-bb00-adf96740f692-1468266590832.png",
                    "twitter:title": "98point6 - Senior Software Back-End Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Requirements: Bachelors or Masters degree in Computer Science, Math or \nequivalent experience; 5+ years experience designing and coding in Java, C++, \nC#,\u00a0...",
        "title": "98point6 - Senior Software Back-End Engineer"
    },
    {
        "cacheId": "8ByCgRUp2-IJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../1cbf2e81-c302-489d-9006-2609324848d7",
        "htmlFormattedUrl": "https://jobs.lever.co/.../1cbf2e81-c302-489d-9006-2609324848d7",
        "htmlSnippet": "2+ years of experience with Java, <b>C#</b> or Ruby; 2+ years of experience with <br>\nJavascript, HTML5 and CSS; 1+ years of experience with Angular.js (preferable),<br>\n&nbsp;...",
        "htmlTitle": "Updox - Software Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/updox/1cbf2e81-c302-489d-9006-2609324848d7",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/2396e49f-ee96-4444-a6fa-6d81287198de-1490712748236.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "71",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzJ43zviQ7eo_NZPYAPz4MkcDwg3QqP0Nu-Tu9fz6zMi3oMDkAQJaXEw",
                    "width": "225"
                }
            ],
            "metatags": [
                {
                    "og:description": "We believe that high \u00adquality, innovative software is built by craftsmen in a collaborative workshop environment, rather than by workers on an assembly line. Our team values passion and dedication over drudgery and busywork. To us, crafting software is a way of life, not just a job. If you share our passion for breaking new ground every day, while delivering cutting edge software solutions, and are driven to continuously improve your craft while striving for perfection each and every day, then we may have a spot for you in our high growth, startup company. If you are selected to join our team, you will have the opportunity to work with a wide array of languages and technologies, learn and leverage agile practices, work on various layers of the architecture stack, build awesome web and mobile apps, and learn to love the safety of a well \u00adwritten automated test. A Software Engineer is responsible for participating in many aspects of the Updox software development lifecycle for both new",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/2396e49f-ee96-4444-a6fa-6d81287198de-1490712748236.png",
                    "og:image:height": "200",
                    "og:title": "Updox - Software Engineer",
                    "og:url": "https://jobs.lever.co/updox/1cbf2e81-c302-489d-9006-2609324848d7",
                    "twitter:description": "We believe that high \u00adquality, innovative software is built by craftsmen in a collaborative workshop environment, rather than by workers on an assembly line. Our team values passion and dedication over drudgery and busywork. To us, crafting software is a way of life, not just a job. If you share our passion for breaking new ground every day, while delivering cutting edge software solutions, and are driven to continuously improve your craft while striving for perfection each and every day, then we may have a spot for you in our high growth, startup company. If you are selected to join our team, you will have the opportunity to work with a wide array of languages and technologies, learn and leverage agile practices, work on various layers of the architecture stack, build awesome web and mobile apps, and learn to love the safety of a well \u00adwritten automated test. A Software Engineer is responsible for participating in many aspects of the Updox software development lifecycle for both new",
                    "twitter:title": "Updox - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "2+ years of experience with Java, C# or Ruby; 2+ years of experience with \nJavascript, HTML5 and CSS; 1+ years of experience with Angular.js (preferable),\n\u00a0...",
        "title": "Updox - Software Engineer"
    },
    {
        "cacheId": "Kz0FRRWAE6sJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../fd27b4e5-f57e-44c3-94ee-29dda2129673",
        "htmlFormattedUrl": "https://jobs.lever.co/.../fd27b4e5-f57e-44c3-94ee-29dda2129673",
        "htmlSnippet": "Help architect a large software system, written in C++, <b>C#</b>, and Python, to take a <br>\npart from 3D model to manufactured with high reliability and accuracy; Develop&nbsp;...",
        "htmlTitle": "Plethora - Computational Geometry Software Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/plethora/fd27b4e5-f57e-44c3-94ee-29dda2129673",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5e325818-48b2-47c3-bce0-2ee0abaa3d92-1483574051428.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "66",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQ8L6cPsHN4Q8TN2em6nj99HiXdkARMvEPzha67AaHYmgDLx_SlURaFVQ",
                    "width": "600"
                }
            ],
            "metatags": [
                {
                    "og:description": "Plethora is building the future of manufacturing - a new kind of automated factory that turns digital designs into physical products in days, not months with our internally developed software and fully-integrated factory system. We are a uniquely ambitious company funded by some of the biggest names, such as Founders Fund, Lux Capital, Google, and Autodesk. Our organization is already impacting the short-run manufacturing space, with a category-leading NPS, in the $21B addressable market that is ripe for disruption. We\u2019re looking for a Computational Geometry Software Developer to help build the automated software pipeline that generates manufacturing instructions. This system determines the precise strategy necessary to build a customer part, from the toolpaths to the custom workholdings. As you can imagine, building a software-powered factory is a tricky process. To ensure our success, we employ a variety of engineering methodologies to ensure the correctness and safety of our sys",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5e325818-48b2-47c3-bce0-2ee0abaa3d92-1483574051428.png",
                    "og:image:height": "200",
                    "og:title": "Plethora - Computational Geometry Software Engineer",
                    "og:url": "https://jobs.lever.co/plethora/fd27b4e5-f57e-44c3-94ee-29dda2129673",
                    "twitter:description": "Plethora is building the future of manufacturing - a new kind of automated factory that turns digital designs into physical products in days, not months with our internally developed software and fully-integrated factory system. We are a uniquely ambitious company funded by some of the biggest names, such as Founders Fund, Lux Capital, Google, and Autodesk. Our organization is already impacting the short-run manufacturing space, with a category-leading NPS, in the $21B addressable market that is ripe for disruption. We\u2019re looking for a Computational Geometry Software Developer to help build the automated software pipeline that generates manufacturing instructions. This system determines the precise strategy necessary to build a customer part, from the toolpaths to the custom workholdings. As you can imagine, building a software-powered factory is a tricky process. To ensure our success, we employ a variety of engineering methodologies to ensure the correctness and safety of our sys",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/5e325818-48b2-47c3-bce0-2ee0abaa3d92-1479853206515.png",
                    "twitter:title": "Plethora - Computational Geometry Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Help architect a large software system, written in C++, C#, and Python, to take a \npart from 3D model to manufactured with high reliability and accuracy; Develop\u00a0...",
        "title": "Plethora - Computational Geometry Software Engineer"
    },
    {
        "cacheId": "QZ3yUqxSmKoJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/gigya/a3197c46-c592-4f8d-a21b-e9d5f407bfe7",
        "htmlFormattedUrl": "https://jobs.lever.co/gigya/a3197c46-c592-4f8d-a21b-e9d5f407bfe7",
        "htmlSnippet": "Design, develop and execute automation tests using <b>C#</b> and JavaScript. Identify, <br>\nrecord, document and track bugs. Perform thorough regression testing when&nbsp;...",
        "htmlTitle": "Gigya - Experienced Automation Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/gigya/a3197c46-c592-4f8d-a21b-e9d5f407bfe7",
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
                    "og:description": "Gigya is looking for an experienced QA Manual & Automation developer for our team. The position is located at Gigya\u2019s R&D center, Azrieli Towers, Tel Aviv. About The Position: The QA Engineer verifies the company\u2019s SDKs products across a wide range of platforms (e.g., Android, iOS, Web, client- server-side). You will be responsible for the product from beginning to end - influence feature design, create test plans, write and execute automated and manual tests, and troubleshoot customer issues. The \u202aQA Engineer as part of the development team. At Gigya, QA plays a key role in the development process, so the position requires an independent fast learner with general technical skills, the ability to understand customer needs and an out-of-the-box mindset.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1483032404076.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Gigya - Experienced Automation Developer",
                    "og:url": "https://jobs.lever.co/gigya/a3197c46-c592-4f8d-a21b-e9d5f407bfe7",
                    "twitter:description": "Gigya is looking for an experienced QA Manual & Automation developer for our team. The position is located at Gigya\u2019s R&D center, Azrieli Towers, Tel Aviv. About The Position: The QA Engineer verifies the company\u2019s SDKs products across a wide range of platforms (e.g., Android, iOS, Web, client- server-side). You will be responsible for the product from beginning to end - influence feature design, create test plans, write and execute automated and manual tests, and troubleshoot customer issues. The \u202aQA Engineer as part of the development team. At Gigya, QA plays a key role in the development process, so the position requires an independent fast learner with general technical skills, the ability to understand customer needs and an out-of-the-box mindset.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1481204313579.png",
                    "twitter:title": "Gigya - Experienced Automation Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Design, develop and execute automation tests using C# and JavaScript. Identify, \nrecord, document and track bugs. Perform thorough regression testing when\u00a0...",
        "title": "Gigya - Experienced Automation Developer"
    },
    {
        "cacheId": "bv9mrsmogX4J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../5cb76721-b10a-4d19-9f38-7be7a9ddc70f",
        "htmlFormattedUrl": "https://jobs.lever.co/.../5cb76721-b10a-4d19-9f38-7be7a9ddc70f",
        "htmlSnippet": "Responsibilities. Current openings are for people with top-notch experience in <br>\nMicrosoft .NET languages (primarily ASP.NET, <b>C#</b>, and LINQ), technologies (<br>\nMVC&nbsp;...",
        "htmlTitle": "Lazerline Solutions - CX/.NET Software Developer, Intermediate",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/lazerlinesolutions/5cb76721-b10a-4d19-9f38-7be7a9ddc70f",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/4b64606c-d19b-477f-aa6b-bfdf6bb34fa7-1472481053413.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "185",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQA1VBgvH9468HsPe4hNp_4tjnm8FTkjJm-au_4QpMF_Gs6jPRARnsccyo",
                    "width": "272"
                }
            ],
            "metatags": [
                {
                    "og:description": "*** LOCATION: STERLING, VA and ARLINGTON, VA *** General/Overview Actively searching bright and talented software engineers to support the Drug Enforcement administration's application development initiatives. Our engineers develop cutting-edge applications that directly enable DEA to further its mission. Our client and DEA are avid practitioners of agile development methodologies, and most of our work is done in a purely agile environment. We use Scrum, continuous integration, and peer reviews on a daily basis, and we adhere to the \u201cinspect and adapt\u201d principle as we seek new ways to innovate. We are looking for more than a set of programming skills \u2013 we are interested in your experiences, talents, interests, and enthusiasm for the craftsmanship and engineering aspects of software development. Our engineers understand and use design patterns, SOLID principles, mocks and fakes, and unit tests. In addition to being technology enthusiasts, we are also passionate about delivering v",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/4b64606c-d19b-477f-aa6b-bfdf6bb34fa7-1472481053413.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Lazerline Solutions - CX/.NET Software Developer, Intermediate",
                    "og:url": "https://jobs.lever.co/lazerlinesolutions/5cb76721-b10a-4d19-9f38-7be7a9ddc70f",
                    "twitter:description": "*** LOCATION: STERLING, VA and ARLINGTON, VA *** General/Overview Actively searching bright and talented software engineers to support the Drug Enforcement administration's application development initiatives. Our engineers develop cutting-edge applications that directly enable DEA to further its mission. Our client and DEA are avid practitioners of agile development methodologies, and most of our work is done in a purely agile environment. We use Scrum, continuous integration, and peer reviews on a daily basis, and we adhere to the \u201cinspect and adapt\u201d principle as we seek new ways to innovate. We are looking for more than a set of programming skills \u2013 we are interested in your experiences, talents, interests, and enthusiasm for the craftsmanship and engineering aspects of software development. Our engineers understand and use design patterns, SOLID principles, mocks and fakes, and unit tests. In addition to being technology enthusiasts, we are also passionate about delivering v",
                    "twitter:title": "Lazerline Solutions - CX/.NET Software Developer, Intermediate",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Responsibilities. Current openings are for people with top-notch experience in \nMicrosoft .NET languages (primarily ASP.NET, C#, and LINQ), technologies (\nMVC\u00a0...",
        "title": "Lazerline Solutions - CX/.NET Software Developer, Intermediate"
    },
    {
        "cacheId": "FWP11B-32uQJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf",
        "htmlSnippet": "You&#39;ll brainstorm with designers, product managers and game developers to <br>\ndesign new features; You&#39;ll work both on the front end in C++/<b>C#</b> and the back <br>\nend&nbsp;...",
        "htmlTitle": "Twitch - Senior Software Engineer - Commerce",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Twitch is building the future of interactive entertainment, and our windows client engineering team is growing in order to execute on a brand new, secret project. We\u2019re looking for engineers that love solving hard technical problems related to gaming on PCs and Twitch. This project will require innovation and the ability to come up with technical solutions in new spaces. You will also need to work with and be able to think like a game developer. We\u2019re working with top developers to help bring new experiences to customers. We\u2019re using a variety of tools and languages, but much of our work will be in C++, so you\u2019ll have to be willing to roll up your sleeves and get your hands dirty. You\u2019ll have to write a lot of code, but should also be able to mentor engineers around you and do whatever needs to be done for the team and product initiative to succeed.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Senior Software Engineer - Commerce",
                    "og:url": "https://jobs.lever.co/twitch/4a42f57e-12a0-4707-b4c0-c5f1938e68cf",
                    "twitter:description": "Twitch is building the future of interactive entertainment, and our windows client engineering team is growing in order to execute on a brand new, secret project. We\u2019re looking for engineers that love solving hard technical problems related to gaming on PCs and Twitch. This project will require innovation and the ability to come up with technical solutions in new spaces. You will also need to work with and be able to think like a game developer. We\u2019re working with top developers to help bring new experiences to customers. We\u2019re using a variety of tools and languages, but much of our work will be in C++, so you\u2019ll have to be willing to roll up your sleeves and get your hands dirty. You\u2019ll have to write a lot of code, but should also be able to mentor engineers around you and do whatever needs to be done for the team and product initiative to succeed.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Senior Software Engineer - Commerce",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "You'll brainstorm with designers, product managers and game developers to \ndesign new features; You'll work both on the front end in C++/C# and the back \nend\u00a0...",
        "title": "Twitch - Senior Software Engineer - Commerce"
    },
    {
        "cacheId": "sdHOTrLpDRoJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../fa5864b5-f094-4a60-94c3-6bce174eb0c3",
        "htmlFormattedUrl": "https://jobs.lever.co/.../fa5864b5-f094-4a60-94c3-6bce174eb0c3",
        "htmlSnippet": "For this role, we are looking for an experienced <b>C#</b> engineer, ideally with <br>\nexposure &amp; experience within a mobile client environment (iOS or Android) and <br>\nto&nbsp;...",
        "htmlTitle": "Trainline - Backend Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/thetrainline/fa5864b5-f094-4a60-94c3-6bce174eb0c3",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/e7325281-bcf1-44ee-8fbb-cac3cc210349-1491409888732.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "112",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQ0KZwVSoEOnN4-xPVXPIcI5xCTSQ2R1Pte6AGPcbPttjWzL1hfHo56wQ",
                    "width": "450"
                }
            ],
            "metatags": [
                {
                    "og:description": "The Trainline is UK\u2019s leading online provider of rail tickets and journey planning, setting the pace in rail-commerce. Our platforms are a strategic area of focus and investment for our with more than 46 million visits per month (website and mobile apps combined) and \u00a32.3 bn in transactions / year. The team is responsible for our UK eCommerce backend components as well as the trainline public API. The eCommerce components underpin our rail transactions across all our front end and support channels. Our Public API is one of the channels that integrate with our UK eCommerce components and allows our partners to retail UK rail via their bespoke applications. Both products implement high scalable and high availability patterns and process hundreds or thousands of transactions per minute. For this role, we are looking for an experienced C# engineer, ideally with exposure & experience within a mobile client environment (iOS or Android) and to areas like DevOps and Testing. You will join",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/e7325281-bcf1-44ee-8fbb-cac3cc210349-1491409888732.png",
                    "og:image:height": "200",
                    "og:title": "Trainline - Backend Engineer",
                    "og:url": "https://jobs.lever.co/thetrainline/fa5864b5-f094-4a60-94c3-6bce174eb0c3",
                    "twitter:description": "The Trainline is UK\u2019s leading online provider of rail tickets and journey planning, setting the pace in rail-commerce. Our platforms are a strategic area of focus and investment for our with more than 46 million visits per month (website and mobile apps combined) and \u00a32.3 bn in transactions / year. The team is responsible for our UK eCommerce backend components as well as the trainline public API. The eCommerce components underpin our rail transactions across all our front end and support channels. Our Public API is one of the channels that integrate with our UK eCommerce components and allows our partners to retail UK rail via their bespoke applications. Both products implement high scalable and high availability patterns and process hundreds or thousands of transactions per minute. For this role, we are looking for an experienced C# engineer, ideally with exposure & experience within a mobile client environment (iOS or Android) and to areas like DevOps and Testing. You will join",
                    "twitter:title": "Trainline - Backend Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "For this role, we are looking for an experienced C# engineer, ideally with \nexposure & experience within a mobile client environment (iOS or Android) and \nto\u00a0...",
        "title": "Trainline - Backend Engineer"
    },
    {
        "cacheId": "jOdl3seH5CAJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../521ce14b-957b-46e5-a551-1617d75a603f",
        "htmlFormattedUrl": "https://jobs.lever.co/.../521ce14b-957b-46e5-a551-1617d75a603f",
        "htmlSnippet": "Android; Strong <b>C#</b> skills. Experience in hybrid web view applications; <br>\nKnowledgeable about HTTP, web services and local storage; Experience <br>\ndeveloping&nbsp;...",
        "htmlTitle": "K4Connect - Senior Mobile Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/k4connect/521ce14b-957b-46e5-a551-1617d75a603f",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/3586feeb-d1df-4c9e-bcbe-5f46f9986ebc-1468443530152.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "146",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSs3y9KYwFJ6sFJuIZZgalLFBRkMFzqTzM8EzSYyvrZR8pd1lQ5a8-YelWq",
                    "width": "345"
                }
            ],
            "metatags": [
                {
                    "og:description": "We are a high impact, high growth, venture backed company on a mission to leverage technology to empower the 1.5B older adults and individuals living with disabilities to live simpler, healthier and happier lives. We believe that technology is not simply reserved for the next generation, but rather should empower all generations. If you are interested in joining a committed, impassioned, intelligent and creative team that is driven to making global impact, then K4Connect may be the place for you! Our ability to develop the best mobile experience for our clients, while connecting them with friends and family depends on a reliable mobile application on as many platforms as possible. Working with our Angular team, you\u2019ll help define, create and add great new features, port our app to new platforms, and continually strive to improve performance and quality for our clients.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/3586feeb-d1df-4c9e-bcbe-5f46f9986ebc-1468443530152.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "K4Connect - Senior Mobile Engineer",
                    "og:url": "https://jobs.lever.co/k4connect/521ce14b-957b-46e5-a551-1617d75a603f",
                    "twitter:description": "We are a high impact, high growth, venture backed company on a mission to leverage technology to empower the 1.5B older adults and individuals living with disabilities to live simpler, healthier and happier lives. We believe that technology is not simply reserved for the next generation, but rather should empower all generations. If you are interested in joining a committed, impassioned, intelligent and creative team that is driven to making global impact, then K4Connect may be the place for you! Our ability to develop the best mobile experience for our clients, while connecting them with friends and family depends on a reliable mobile application on as many platforms as possible. Working with our Angular team, you\u2019ll help define, create and add great new features, port our app to new platforms, and continually strive to improve performance and quality for our clients.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/3586feeb-d1df-4c9e-bcbe-5f46f9986ebc-1468443514435.png",
                    "twitter:title": "K4Connect - Senior Mobile Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Android; Strong C# skills. Experience in hybrid web view applications; \nKnowledgeable about HTTP, web services and local storage; Experience \ndeveloping\u00a0...",
        "title": "K4Connect - Senior Mobile Engineer"
    },
    {
        "cacheId": "l_GPjQf7EZ8J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../b10d6138-c470-4577-914e-b00b0671c285",
        "htmlFormattedUrl": "https://jobs.lever.co/.../b10d6138-c470-4577-914e-b00b0671c285",
        "htmlSnippet": "On the mobile side we also use Objective-C, Java (both for Android and back-<br>\nend), <b>C#</b>, and client-side JavaScript. Our platform is fully run on top of AWS in a&nbsp;...",
        "htmlTitle": "CloudMine - Senior Platform Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/cloudmineinc/b10d6138-c470-4577-914e-b00b0671c285",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/Cloudmine.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "126",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRqbFLu5PrdVNHIryoKDvaiWc151dAzTFuXbpLq_32Ry_p6VBSbRYG1GAw",
                    "width": "240"
                }
            ],
            "metatags": [
                {
                    "og:description": "About CloudMine CloudMine, through its Connected Health Cloud, solves the technical complexities of healthcare innovation and empowers leaders to bring truly impactful solutions to market significantly faster than ever imagined. By removing challenges such as compliance, security, and interoperability, innovators across Healthcare, Pharmaceuticals, Biotechnology and more are able to truly focus on improving the patient experience, reducing readmissions, and creating better outcomes. CloudMine\u2019s Connected Health Cloud is accelerating healthcare innovation where it\u2019s needed most in data analytics, clinical research, treatment adherence, and chronic disease management. Headquartered in Center City, Philadelphia, we have two additional locations in Chicago, IL and Boston, MA. Our team is made up of fast moving technologists that thrive on customer success. Job Description We are looking for self-motivated, highly experienced engineers to join our team to help take our product to th",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/Cloudmine.png",
                    "og:image:height": "200",
                    "og:title": "CloudMine - Senior Platform Engineer",
                    "og:url": "https://jobs.lever.co/cloudmineinc/b10d6138-c470-4577-914e-b00b0671c285",
                    "twitter:description": "About CloudMine CloudMine, through its Connected Health Cloud, solves the technical complexities of healthcare innovation and empowers leaders to bring truly impactful solutions to market significantly faster than ever imagined. By removing challenges such as compliance, security, and interoperability, innovators across Healthcare, Pharmaceuticals, Biotechnology and more are able to truly focus on improving the patient experience, reducing readmissions, and creating better outcomes. CloudMine\u2019s Connected Health Cloud is accelerating healthcare innovation where it\u2019s needed most in data analytics, clinical research, treatment adherence, and chronic disease management. Headquartered in Center City, Philadelphia, we have two additional locations in Chicago, IL and Boston, MA. Our team is made up of fast moving technologists that thrive on customer success. Job Description We are looking for self-motivated, highly experienced engineers to join our team to help take our product to th",
                    "twitter:title": "CloudMine - Senior Platform Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "On the mobile side we also use Objective-C, Java (both for Android and back-\nend), C#, and client-side JavaScript. Our platform is fully run on top of AWS in a\u00a0...",
        "title": "CloudMine - Senior Platform Engineer"
    },
    {
        "cacheId": "xkNdVCEVBGsJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../31eb48e3-296d-4b21-9896-5f85468cac26",
        "htmlFormattedUrl": "https://jobs.lever.co/.../31eb48e3-296d-4b21-9896-5f85468cac26",
        "htmlSnippet": "-Design and develop software in a hands-on capacity by writing globalization <br>\narchitecture and .NET source code (<b>C#</b> and AJAX), developing databases using<br>\n&nbsp;...",
        "htmlTitle": "Vettanna - Sr Web Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/vettanna/31eb48e3-296d-4b21-9896-5f85468cac26",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/1560ec5a-59fc-4de7-af8f-5cc1d3074eb7-1471043749166.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "65",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRcQA_fpNcx9GM2-6269ArWCCuDWVMwoACLNkRmbIDnxPgd7w8SkZStPA",
                    "width": "210"
                }
            ],
            "metatags": [
                {
                    "og:description": "Sr Web Developer Location: Morgan Hill Long term contract with potential for permanent placement based on performance Rate: $85 - $100/hr DOQ Responsibilities include but are not limited to: -Design and develop software in a hands-on capacity by writing globalization architecture and .NET source code (C# and AJAX), developing databases using Microsoft SQL Server, and integrating solutions with leading Microsoft server software platforms. -Understand the content management system and involve the development by working with remote teams. -Provide architectural recommendations -Assist with the creation of business solutions, specifically taking ownership of design and technical architecture, estimates for software development and system configuration hours, and definition of specific technology platforms and products to be used in the solution with globalization/internationalization perspective. -Document requirements, technical designs, using flow charts, class diagrams, sequence",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/1560ec5a-59fc-4de7-af8f-5cc1d3074eb7-1471043749166.png",
                    "og:image:height": "200",
                    "og:title": "Vettanna - Sr Web Developer",
                    "og:url": "https://jobs.lever.co/vettanna/31eb48e3-296d-4b21-9896-5f85468cac26",
                    "twitter:description": "Sr Web Developer Location: Morgan Hill Long term contract with potential for permanent placement based on performance Rate: $85 - $100/hr DOQ Responsibilities include but are not limited to: -Design and develop software in a hands-on capacity by writing globalization architecture and .NET source code (C# and AJAX), developing databases using Microsoft SQL Server, and integrating solutions with leading Microsoft server software platforms. -Understand the content management system and involve the development by working with remote teams. -Provide architectural recommendations -Assist with the creation of business solutions, specifically taking ownership of design and technical architecture, estimates for software development and system configuration hours, and definition of specific technology platforms and products to be used in the solution with globalization/internationalization perspective. -Document requirements, technical designs, using flow charts, class diagrams, sequence",
                    "twitter:title": "Vettanna - Sr Web Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "-Design and develop software in a hands-on capacity by writing globalization \narchitecture and .NET source code (C# and AJAX), developing databases using\n\u00a0...",
        "title": "Vettanna - Sr Web Developer"
    },
    {
        "cacheId": "C_VBczGx8nYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../412e622d-3118-4cc1-9883-c0cc268e03b6",
        "htmlFormattedUrl": "https://jobs.lever.co/.../412e622d-3118-4cc1-9883-c0cc268e03b6",
        "htmlSnippet": "We are looking for a hands-on software architect with great <b>C#</b> and .NET skills to <br>\njoin several SCRUM teams developing a new, complex, distributed, .NET SPA&nbsp;...",
        "htmlTitle": "Bluewater Consulting Group - .NET Architect",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/bwcgroup/412e622d-3118-4cc1-9883-c0cc268e03b6",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1456168493663.jpg"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "213",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsTkSJpe3kaAhBpVA9ZgEfChJ1MuTn2uE35TMFJUpgRXwY2iYzA5njOug",
                    "width": "236"
                }
            ],
            "metatags": [
                {
                    "og:description": "OVERVIEW We are looking for a hands-on software architect with great C# and .NET skills to join several SCRUM teams developing a new, complex, distributed, .NET SPA to support millions of customers using the latest technologies: ASP.NET Core (ASP.NET 5) / Core MVC (MVC 6) / .NET Core (.Net 4.6), Angular, Azure, Redis. This is a potentially long-term contract opportunity: at least one year, plus likely another year after that. Our client is also known for its willingness and ability to retain contracted talent for many years. ENVIRONMENT We take the software engineering craft to heart: extensive unit testing, peer reviews, formal coding guidelines with the latest code quality tooling, continuous integration/deployment and a supportive, delivery-focused atmosphere are just some of the characteristics of our work environment. Working hours are typically limited to 40/week. Death marches are not in our DNA. The positions are at the client site in the immediate vicinity of Washington,",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/84963f7c-5208-4789-813f-59b515174479-1456168493663.jpg",
                    "og:image:height": "200",
                    "og:title": "Bluewater Consulting Group - .NET Architect",
                    "og:url": "https://jobs.lever.co/bwcgroup/412e622d-3118-4cc1-9883-c0cc268e03b6",
                    "twitter:description": "OVERVIEW We are looking for a hands-on software architect with great C# and .NET skills to join several SCRUM teams developing a new, complex, distributed, .NET SPA to support millions of customers using the latest technologies: ASP.NET Core (ASP.NET 5) / Core MVC (MVC 6) / .NET Core (.Net 4.6), Angular, Azure, Redis. This is a potentially long-term contract opportunity: at least one year, plus likely another year after that. Our client is also known for its willingness and ability to retain contracted talent for many years. ENVIRONMENT We take the software engineering craft to heart: extensive unit testing, peer reviews, formal coding guidelines with the latest code quality tooling, continuous integration/deployment and a supportive, delivery-focused atmosphere are just some of the characteristics of our work environment. Working hours are typically limited to 40/week. Death marches are not in our DNA. The positions are at the client site in the immediate vicinity of Washington,",
                    "twitter:title": "Bluewater Consulting Group - .NET Architect",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "We are looking for a hands-on software architect with great C# and .NET skills to \njoin several SCRUM teams developing a new, complex, distributed, .NET SPA\u00a0...",
        "title": "Bluewater Consulting Group - .NET Architect"
    },
    {
        "cacheId": "d7_vDBoqF8oJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../c3a10185-536b-4837-bc2a-e8c0b59d3315",
        "htmlFormattedUrl": "https://jobs.lever.co/.../c3a10185-536b-4837-bc2a-e8c0b59d3315",
        "htmlSnippet": "NET and <b>C#</b> environment) with an emphasis on both front-end methodologies <br>\nand server-side programing. * Design and develop web services components for<br>\n&nbsp;...",
        "htmlTitle": "Lazerline Solutions - Application Developer Master",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/lazerlinesolutions/c3a10185-536b-4837-bc2a-e8c0b59d3315",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/4b64606c-d19b-477f-aa6b-bfdf6bb34fa7-1472481053413.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "185",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQA1VBgvH9468HsPe4hNp_4tjnm8FTkjJm-au_4QpMF_Gs6jPRARnsccyo",
                    "width": "272"
                }
            ],
            "metatags": [
                {
                    "og:description": "General/Overview Actively seeking a Master Application Developer to join our team and support development efforts for a government client in Fort Collins, CO. Would you like to be part of a dynamic team of dedicated software professionals? Are you concerned about protecting our Nation\u2019s natural resources? We need people who are committed to action. People who want to apply their education and experience to make sure that all of us enjoy the benefits of productive soil, clean water, clean air, and abundant wildlife that come from a healthy environment. Natural resource conservation is an effort of Federal and State agencies, universities, and professional societies to deliver science-based information to land owners. Join us to build the technology to help people understand, preserve and increase the productivity of our natural resources. Responsibilities The successful candidate must be knowledgeable of and experienced with web and desktop application software design and develo",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/4b64606c-d19b-477f-aa6b-bfdf6bb34fa7-1472481053413.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Lazerline Solutions - Application Developer Master",
                    "og:url": "https://jobs.lever.co/lazerlinesolutions/c3a10185-536b-4837-bc2a-e8c0b59d3315",
                    "twitter:description": "General/Overview Actively seeking a Master Application Developer to join our team and support development efforts for a government client in Fort Collins, CO. Would you like to be part of a dynamic team of dedicated software professionals? Are you concerned about protecting our Nation\u2019s natural resources? We need people who are committed to action. People who want to apply their education and experience to make sure that all of us enjoy the benefits of productive soil, clean water, clean air, and abundant wildlife that come from a healthy environment. Natural resource conservation is an effort of Federal and State agencies, universities, and professional societies to deliver science-based information to land owners. Join us to build the technology to help people understand, preserve and increase the productivity of our natural resources. Responsibilities The successful candidate must be knowledgeable of and experienced with web and desktop application software design and develo",
                    "twitter:title": "Lazerline Solutions - Application Developer Master",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "NET and C# environment) with an emphasis on both front-end methodologies \nand server-side programing. * Design and develop web services components for\n\u00a0...",
        "title": "Lazerline Solutions - Application Developer Master"
    },
    {
        "cacheId": "Bsgm0QqHvsMJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../206283ce-82f8-4e61-b129-a2d62ea00347",
        "htmlFormattedUrl": "https://jobs.lever.co/.../206283ce-82f8-4e61-b129-a2d62ea00347",
        "htmlSnippet": "You will be tasked with improving and augmenting our drawing automation web <br>\nservices utilizing RealDWG, <b>C#</b>, WCF, Web API and SQL. You&#39;ll communicate&nbsp;...",
        "htmlTitle": "CaptiveAire Systems - Sr. AutoCAD Automation Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/captiveaire/206283ce-82f8-4e61-b129-a2d62ea00347",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/a07fc712-4e94-4fa7-84e6-345e8cdaebda-1490798859500.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "82",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS8qAWSMyIhfFvuuYH8e5nSvuEhC3obs_JfdlF4LUJe2QKkFUnIA0lzjG0",
                    "width": "600"
                }
            ],
            "metatags": [
                {
                    "og:description": "CaptiveAire values its software developers highly and offers them immense opportunities for freedom and creativity while not having overbearing management. We value very highly our work environment and provide the absolute best in terms of equipment. Our corporate offices are a developer's dream with private offices and modern, recently renovated spaces. We are seeking an experienced AutoCAD automation developer to join our existing product and submittal drawing automation team. You will be tasked with improving and augmenting our drawing automation web services utilizing RealDWG, C#, WCF, Web API and SQL. You\u2019ll communicate with sales engineers, product engineers and other CaptiveAire employees to translate user stories and requirements into concrete software development tasks. Over time you\u2019ll be expected to gain good knowledge of CaptiveAire products and their nuances as it relates to 2D drawings and 3D models. You will gain familiarity with software applications used by our sales",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/a07fc712-4e94-4fa7-84e6-345e8cdaebda-1490798859500.png",
                    "og:image:height": "200",
                    "og:title": "CaptiveAire Systems - Sr. AutoCAD Automation Developer",
                    "og:url": "https://jobs.lever.co/captiveaire/206283ce-82f8-4e61-b129-a2d62ea00347",
                    "twitter:description": "CaptiveAire values its software developers highly and offers them immense opportunities for freedom and creativity while not having overbearing management. We value very highly our work environment and provide the absolute best in terms of equipment. Our corporate offices are a developer's dream with private offices and modern, recently renovated spaces. We are seeking an experienced AutoCAD automation developer to join our existing product and submittal drawing automation team. You will be tasked with improving and augmenting our drawing automation web services utilizing RealDWG, C#, WCF, Web API and SQL. You\u2019ll communicate with sales engineers, product engineers and other CaptiveAire employees to translate user stories and requirements into concrete software development tasks. Over time you\u2019ll be expected to gain good knowledge of CaptiveAire products and their nuances as it relates to 2D drawings and 3D models. You will gain familiarity with software applications used by our sales",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/a07fc712-4e94-4fa7-84e6-345e8cdaebda-1490891507876.png",
                    "twitter:title": "CaptiveAire Systems - Sr. AutoCAD Automation Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "You will be tasked with improving and augmenting our drawing automation web \nservices utilizing RealDWG, C#, WCF, Web API and SQL. You'll communicate\u00a0...",
        "title": "CaptiveAire Systems - Sr. AutoCAD Automation Developer"
    },
    {
        "cacheId": "ZKUAE4hbPF8J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../a01796dc-9c34-4e69-adf1-89eed6972e71",
        "htmlFormattedUrl": "https://jobs.lever.co/.../a01796dc-9c34-4e69-adf1-89eed6972e71",
        "htmlSnippet": "Test execution experience in .NET/<b>C#</b> environment. * Experience testing <br>\nproducts developed within the Pega framework. * Experience with Microsoft SQL <br>\nServer&nbsp;...",
        "htmlTitle": "Lazerline Solutions - Sr. Software Testing Specialist",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/lazerlinesolutions/a01796dc-9c34-4e69-adf1-89eed6972e71",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/4b64606c-d19b-477f-aa6b-bfdf6bb34fa7-1472481053413.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "185",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQA1VBgvH9468HsPe4hNp_4tjnm8FTkjJm-au_4QpMF_Gs6jPRARnsccyo",
                    "width": "272"
                }
            ],
            "metatags": [
                {
                    "og:description": "General/Overview Actively seeking a Senior Software Testing Specialist. The selected candidate must be knowledgeable and experienced as a Quality Assurance/Test Engineer for testing web-based and desktop applications, software engineering practices, quality assurance standards, interpretation of product requirements, test plan development, test case development, and testing of software functionality, performance, load, installation, and usability (508 compliance experience a plus). Responsibilities Principal responsibilities include: * Test plan and test case development * Test environment creation and configuration * Test server maintenance * Manual and automated testing of software functionality, installation, and regression * Load and performance testing * Bug management and error tracking * Test report documentation Coordination and prioritization of testing activities and the ability to work with multiple development teams and software projects are also critic",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/4b64606c-d19b-477f-aa6b-bfdf6bb34fa7-1472481053413.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Lazerline Solutions - Sr. Software Testing Specialist",
                    "og:url": "https://jobs.lever.co/lazerlinesolutions/a01796dc-9c34-4e69-adf1-89eed6972e71",
                    "twitter:description": "General/Overview Actively seeking a Senior Software Testing Specialist. The selected candidate must be knowledgeable and experienced as a Quality Assurance/Test Engineer for testing web-based and desktop applications, software engineering practices, quality assurance standards, interpretation of product requirements, test plan development, test case development, and testing of software functionality, performance, load, installation, and usability (508 compliance experience a plus). Responsibilities Principal responsibilities include: * Test plan and test case development * Test environment creation and configuration * Test server maintenance * Manual and automated testing of software functionality, installation, and regression * Load and performance testing * Bug management and error tracking * Test report documentation Coordination and prioritization of testing activities and the ability to work with multiple development teams and software projects are also critic",
                    "twitter:title": "Lazerline Solutions - Sr. Software Testing Specialist",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Test execution experience in .NET/C# environment. * Experience testing \nproducts developed within the Pega framework. * Experience with Microsoft SQL \nServer\u00a0...",
        "title": "Lazerline Solutions - Sr. Software Testing Specialist"
    },
    {
        "cacheId": "l21Eruk1HiwJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/axon/99aade2a-6609-4c1c-96e8-c602b0560501",
        "htmlFormattedUrl": "https://jobs.lever.co/axon/99aade2a-6609-4c1c-96e8-c602b0560501",
        "htmlSnippet": "To achieve these design implementations, you will implement with object <br>\noriented methodologies using X++, SSRS, .net and / or <b>C#</b> development <br>\nlanguages.",
        "htmlTitle": "Axon - Sr. AX Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/axon/99aade2a-6609-4c1c-96e8-c602b0560501",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/6aa14d12-a323-4bcb-9368-48a4fd3d7aca-1497567326829.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "190",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSv4tWaK_c0_aSAH7VHCIUaK9xIw5lCeCQPyYa_yNBPWqTL6cv1-JKwKWur",
                    "width": "266"
                }
            ],
            "metatags": [
                {
                    "og:description": "Your Impact You bring deep experience with Microsoft Dynamics, the know how to clarify and enable business process with solutions that propel your business partners to new heights. In addition to your Dynamics skill set you bring solution design experience, curiosity and passion to make the team around you better with your infectious can do attitude. Your Day to Day In this role, you will work closely with colleagues in theIT infrastructure, Development and Application Services Teams,along withinternal employees and external consultants on system functionality, gathering requirements, designing and developing application functionality based on defined specifications. To achieve these design implementations, you will implement with object oriented methodologies using X++, SSRS, .net and / or C# development languages. This work requires additional detail including unit, regression and integration testing and driving the completion of user acceptance testing. And system administration",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/6aa14d12-a323-4bcb-9368-48a4fd3d7aca-1497567326829.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Axon - Sr. AX Developer",
                    "og:url": "https://jobs.lever.co/axon/99aade2a-6609-4c1c-96e8-c602b0560501",
                    "twitter:description": "Your Impact You bring deep experience with Microsoft Dynamics, the know how to clarify and enable business process with solutions that propel your business partners to new heights. In addition to your Dynamics skill set you bring solution design experience, curiosity and passion to make the team around you better with your infectious can do attitude. Your Day to Day In this role, you will work closely with colleagues in theIT infrastructure, Development and Application Services Teams,along withinternal employees and external consultants on system functionality, gathering requirements, designing and developing application functionality based on defined specifications. To achieve these design implementations, you will implement with object oriented methodologies using X++, SSRS, .net and / or C# development languages. This work requires additional detail including unit, regression and integration testing and driving the completion of user acceptance testing. And system administration",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/6aa14d12-a323-4bcb-9368-48a4fd3d7aca-1497567377352.png",
                    "twitter:title": "Axon - Sr. AX Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "To achieve these design implementations, you will implement with object \noriented methodologies using X++, SSRS, .net and / or C# development \nlanguages.",
        "title": "Axon - Sr. AX Developer"
    },
    {
        "cacheId": "tGPzYCuy7SwJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../d6c2d430-6fed-4dd7-9057-9e66c528365f",
        "htmlFormattedUrl": "https://jobs.lever.co/.../d6c2d430-6fed-4dd7-9057-9e66c528365f",
        "htmlSnippet": "Must have a strong knowledge of <b>C#</b> and javascript, and experience developing <br>\nweb clients. You thrive on working with results-oriented team members in a fun&nbsp;...",
        "htmlTitle": "Bunker - Angular / .NET Senior Software Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/buildbunker/d6c2d430-6fed-4dd7-9057-9e66c528365f",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/58572ace-f589-438c-8566-ea6a6827ef58-1493913799257.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "133",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTYEprViVfMBJ2Lv-wUIlj_0huVLz-p1QYY-YruX1yqDtERxkUjCjLHtqav",
                    "width": "378"
                }
            ],
            "metatags": [
                {
                    "og:description": "Are you passionate about creating experiences that people love and being a pioneer for change in the $100B small business insurance segment? If yes, we\u2019d like to talk to you. Bunker is delivering an entirely new insurance buying experience to small businesses. The founding team consists of leading design, UX, technology, and insurance talent. Backed by leading venture capitalists and Fortune 1000 insurance companies, we\u2019re in growth mode and expanding our team. Summary: Bunker is seeking a full stack developer in its Madison, WI office with a focus on web UX to help an agile team build out their innovative online insurance purchasing and compliance tool in downtown Madison, WI. Bunker has a casual, fun and fast paced environment that is perfect for self-motivated devs looking to build great user experiences with great tech. Description/Responsibilities: The chosen candidate will be part of an agile team developing features for a rich Angular web client. Work will be front-end",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/58572ace-f589-438c-8566-ea6a6827ef58-1493913799257.png",
                    "og:image:height": "200",
                    "og:title": "Bunker - Angular / .NET Senior Software Engineer",
                    "og:url": "https://jobs.lever.co/buildbunker/d6c2d430-6fed-4dd7-9057-9e66c528365f",
                    "twitter:description": "Are you passionate about creating experiences that people love and being a pioneer for change in the $100B small business insurance segment? If yes, we\u2019d like to talk to you. Bunker is delivering an entirely new insurance buying experience to small businesses. The founding team consists of leading design, UX, technology, and insurance talent. Backed by leading venture capitalists and Fortune 1000 insurance companies, we\u2019re in growth mode and expanding our team. Summary: Bunker is seeking a full stack developer in its Madison, WI office with a focus on web UX to help an agile team build out their innovative online insurance purchasing and compliance tool in downtown Madison, WI. Bunker has a casual, fun and fast paced environment that is perfect for self-motivated devs looking to build great user experiences with great tech. Description/Responsibilities: The chosen candidate will be part of an agile team developing features for a rich Angular web client. Work will be front-end",
                    "twitter:title": "Bunker - Angular / .NET Senior Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Must have a strong knowledge of C# and javascript, and experience developing \nweb clients. You thrive on working with results-oriented team members in a fun\u00a0...",
        "title": "Bunker - Angular / .NET Senior Software Engineer"
    },
    {
        "cacheId": "t9JDTEt9hLIJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../490c5171-c529-450b-a07d-7bd817a61800",
        "htmlFormattedUrl": "https://jobs.lever.co/.../490c5171-c529-450b-a07d-7bd817a61800",
        "htmlSnippet": "The ideal candidate will have a willingness to learn or have experience with PHP<br>\n, Python, or <b>C#</b>. Good knowledge of the Search Engine Optimization business&nbsp;...",
        "htmlTitle": "Bazaarvoice - Senior Back End Software Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/bazaarvoice/490c5171-c529-450b-a07d-7bd817a61800",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/714170d1-1117-4943-89d7-fa08f7e6af25-1499454942524.png"
                }
            ],
            "metatags": [
                {
                    "og:description": "Who we want Do you want to work on something that you, your friends, family and hundreds of millions of others use every day, and actually makes you smarter about how you spend your money? What if you could do that with a bunch of really smart people in an environment that actively encourages learning, growth and individual development? For good measure, we'll even throw in the opportunity to explore technology from the UI to the database, and everything in between, all while working on products that world's biggest brands rely on in order to maintain their place among the world's biggest brands. Every day, the Bazaarvoice engineering team tackles interesting and challenging problems across virtually every major computer science problem domain, and we do it all at a massive scale. So whether you're interested in server-side Java, UI/UX, massive datasets, mobile/social, natural language processing, sentiment analysis, or data visualization, we've got an opportunity for you. As a",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/714170d1-1117-4943-89d7-fa08f7e6af25-1499454942524.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Bazaarvoice - Senior Back End Software Engineer",
                    "og:url": "https://jobs.lever.co/bazaarvoice/490c5171-c529-450b-a07d-7bd817a61800",
                    "twitter:description": "Who we want Do you want to work on something that you, your friends, family and hundreds of millions of others use every day, and actually makes you smarter about how you spend your money? What if you could do that with a bunch of really smart people in an environment that actively encourages learning, growth and individual development? For good measure, we'll even throw in the opportunity to explore technology from the UI to the database, and everything in between, all while working on products that world's biggest brands rely on in order to maintain their place among the world's biggest brands. Every day, the Bazaarvoice engineering team tackles interesting and challenging problems across virtually every major computer science problem domain, and we do it all at a massive scale. So whether you're interested in server-side Java, UI/UX, massive datasets, mobile/social, natural language processing, sentiment analysis, or data visualization, we've got an opportunity for you. As a",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/714170d1-1117-4943-89d7-fa08f7e6af25-1499455042907.png",
                    "twitter:title": "Bazaarvoice - Senior Back End Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "The ideal candidate will have a willingness to learn or have experience with PHP\n, Python, or C#. Good knowledge of the Search Engine Optimization business\u00a0...",
        "title": "Bazaarvoice - Senior Back End Software Engineer"
    },
    {
        "cacheId": "GDEZFFIBJYYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../20035d6e-84ab-4388-ab3c-ffa175997359",
        "htmlFormattedUrl": "https://jobs.lever.co/.../20035d6e-84ab-4388-ab3c-ffa175997359",
        "htmlSnippet": "NET, <b>C#</b>, HTML5, CSS3, XSLT, T-SQL. Hands on development experience with <br>\nFront-End scripting languages/frameworks; i.e. Javascript, Jquery, React JS,&nbsp;...",
        "htmlTitle": "StartupTAP - Web Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/startuptap/20035d6e-84ab-4388-ab3c-ffa175997359",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/9bf26c36-fc18-4358-9555-a47a0f6691fe-1485894379541.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "92",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4erpM1WIEF7tm7sT0Xj7QoLEM7FhSOlzwJ7aXiAwcAmeh5SfzCQGEpQ",
                    "width": "92"
                }
            ],
            "metatags": [
                {
                    "og:description": "THE COMPANY: deltatre (www.deltatre.com) Part of the Bruin Sports Capital group, deltatre is a global leader in $500B+ sports and media landscape. deltatre provides a comprehensive range of digital and broadcast solutions for the world's largest sport events, federations, media partners and brands, bringing fans close to their teams and allowing immersive, monetizable engagement - delivering multi-dimensional and multi-platform sporting coverage focusing on three different experiences: Online, Onstage, Backstage. The services provided by Deltatre range from sport media strategies, creative and design, websites, mobile apps, live streaming and OTT platforms, to the delivery of results, TV graphics and additional on venue services, as well as a comprehensive sport event management system. SNAPSHOT OF PROJECTS WE\u2019LL BE WORKING ON: WEB DEVELOPER We\u2019re building digital projects and web applications for our partners \u2013 some of the largest and most recognizable sports and media bran",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/9bf26c36-fc18-4358-9555-a47a0f6691fe-1485894379541.png",
                    "og:image:height": "200",
                    "og:title": "StartupTAP - Web Developer",
                    "og:url": "https://jobs.lever.co/startuptap/20035d6e-84ab-4388-ab3c-ffa175997359",
                    "twitter:description": "THE COMPANY: deltatre (www.deltatre.com) Part of the Bruin Sports Capital group, deltatre is a global leader in $500B+ sports and media landscape. deltatre provides a comprehensive range of digital and broadcast solutions for the world's largest sport events, federations, media partners and brands, bringing fans close to their teams and allowing immersive, monetizable engagement - delivering multi-dimensional and multi-platform sporting coverage focusing on three different experiences: Online, Onstage, Backstage. The services provided by Deltatre range from sport media strategies, creative and design, websites, mobile apps, live streaming and OTT platforms, to the delivery of results, TV graphics and additional on venue services, as well as a comprehensive sport event management system. SNAPSHOT OF PROJECTS WE\u2019LL BE WORKING ON: WEB DEVELOPER We\u2019re building digital projects and web applications for our partners \u2013 some of the largest and most recognizable sports and media bran",
                    "twitter:title": "StartupTAP - Web Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "NET, C#, HTML5, CSS3, XSLT, T-SQL. Hands on development experience with \nFront-End scripting languages/frameworks; i.e. Javascript, Jquery, React JS,\u00a0...",
        "title": "StartupTAP - Web Developer"
    },
    {
        "cacheId": "_XZh3uftKRgJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../4e68297f-0980-47bb-974d-b1721e12de52?...",
        "htmlFormattedUrl": "https://jobs.lever.co/.../4e68297f-0980-47bb-974d-b1721e12de52?...",
        "htmlSnippet": "Customer needs are our top priority. Our solutions are modular and based on <br>\nSOA. Our technology stack mainly consists of Java, <b>C#</b>, HTML5, AngularJS, <br>\nGuice&nbsp;...",
        "htmlTitle": "ION - Junior Software Developer, Agency Trading and Processing ...",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/ion/4e68297f-0980-47bb-974d-b1721e12de52?lever-origin=agency&lever-source%5B%5D=ChicagoFinancialSearch",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5acaadd7-e4fc-4b74-9201-6997757efe37-1477889263623.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "164",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQCBxIjcuW2QSrWO2m5fx4ee24C3oiNEd0Sr2AGJPre5x2zWNs_URu4Sbk",
                    "width": "307"
                }
            ],
            "metatags": [
                {
                    "og:description": "Role: Software Developer, XTP Development, ATP Division, Chicago What are we trying to do? We are working on a new generation trade processing and reporting solution which has been launched in the market recently, and must be extended to support cleared OTC products. This is a real time trade processing system that handles activities like trade and position management, risk management, collateral and interest, margining, fees and commissions, balances, market processing and reporting. Our systems connect to 50+ exchanges globally to provide real time trades and market data. Our solution is highly scalable and caters for all types of customers - FCMs, global and regional banks, asset management firms etc. We focus on our customer needs and quick time to market. What do we need help with? We are looking for people with can-do attitude who are passionate about solving complex problems. We are interested in people with strong technical skills and background in test automation. C",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5acaadd7-e4fc-4b74-9201-6997757efe37-1477889263623.png",
                    "og:image:height": "200",
                    "og:title": "ION - Junior Software Developer, Agency Trading and Processing, Chicago",
                    "og:url": "https://jobs.lever.co/ion/4e68297f-0980-47bb-974d-b1721e12de52",
                    "twitter:description": "Role: Software Developer, XTP Development, ATP Division, Chicago What are we trying to do? We are working on a new generation trade processing and reporting solution which has been launched in the market recently, and must be extended to support cleared OTC products. This is a real time trade processing system that handles activities like trade and position management, risk management, collateral and interest, margining, fees and commissions, balances, market processing and reporting. Our systems connect to 50+ exchanges globally to provide real time trades and market data. Our solution is highly scalable and caters for all types of customers - FCMs, global and regional banks, asset management firms etc. We focus on our customer needs and quick time to market. What do we need help with? We are looking for people with can-do attitude who are passionate about solving complex problems. We are interested in people with strong technical skills and background in test automation. C",
                    "twitter:title": "ION - Junior Software Developer, Agency Trading and Processing, Chicago",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Customer needs are our top priority. Our solutions are modular and based on \nSOA. Our technology stack mainly consists of Java, C#, HTML5, AngularJS, \nGuice\u00a0...",
        "title": "ION - Junior Software Developer, Agency Trading and Processing ..."
    },
    {
        "cacheId": "CoooC41zeeIJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../f0b383a0-167c-4650-8b57-6a45034c54b5",
        "htmlFormattedUrl": "https://jobs.lever.co/.../f0b383a0-167c-4650-8b57-6a45034c54b5",
        "htmlSnippet": "Designing and building SQL Server Integration Services (SSIS) jobs; Developing <br>\ncustom Microsoft <b>C#</b> or Node JS loaders for solutions that fall outside the scope&nbsp;...",
        "htmlTitle": "Kurtosys - Senior SQL Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/kurtosys/f0b383a0-167c-4650-8b57-6a45034c54b5",
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
                    "og:description": "INTRODUCTION Do you enjoy making sense of large amounts of complex data? We are seeking an experienced Senior SQL Data Specialist to join our Fact Sheets team. The specialist will draw on a variety of problem solving abilities, advanced SQL, ETL and other database skills, to improve and enhance our existing data integration processes.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/3cfa711a-651a-409a-a7d4-5ad27c30a140-1502985410952.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Kurtosys - Senior SQL Developer",
                    "og:url": "https://jobs.lever.co/kurtosys/f0b383a0-167c-4650-8b57-6a45034c54b5",
                    "twitter:description": "INTRODUCTION Do you enjoy making sense of large amounts of complex data? We are seeking an experienced Senior SQL Data Specialist to join our Fact Sheets team. The specialist will draw on a variety of problem solving abilities, advanced SQL, ETL and other database skills, to improve and enhance our existing data integration processes.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/3cfa711a-651a-409a-a7d4-5ad27c30a140-1502985405500.png",
                    "twitter:title": "Kurtosys - Senior SQL Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Designing and building SQL Server Integration Services (SSIS) jobs; Developing \ncustom Microsoft C# or Node JS loaders for solutions that fall outside the scope\u00a0...",
        "title": "Kurtosys - Senior SQL Developer"
    },
    {
        "cacheId": "-SKurvu6eN0J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../dabdf053-b1e6-4add-96da-14c364453a0f",
        "htmlFormattedUrl": "https://jobs.lever.co/.../dabdf053-b1e6-4add-96da-14c364453a0f",
        "htmlSnippet": "Maintaining and building SQL Server Integration Services (SSIS) jobs; <br>\nMaintaining and developing custom Microsoft <b>C#</b> or Node JS loaders for <br>\nsolutions that fall&nbsp;...",
        "htmlTitle": "Kurtosys - SQL Data Specialist",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/kurtosys/dabdf053-b1e6-4add-96da-14c364453a0f",
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
                    "og:description": "INTRODUCTION Do you enjoy making sense of large amounts of complex data? We are seeking an experienced SQL Data Specialist to join our Fact Sheets team. The specialist will draw on a variety of problem solving abilities, advanced SQL, ETL and other database skills, to improve and enhance our existing data integration processes.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/3cfa711a-651a-409a-a7d4-5ad27c30a140-1502985410952.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Kurtosys - SQL Data Specialist",
                    "og:url": "https://jobs.lever.co/kurtosys/dabdf053-b1e6-4add-96da-14c364453a0f",
                    "twitter:description": "INTRODUCTION Do you enjoy making sense of large amounts of complex data? We are seeking an experienced SQL Data Specialist to join our Fact Sheets team. The specialist will draw on a variety of problem solving abilities, advanced SQL, ETL and other database skills, to improve and enhance our existing data integration processes.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/3cfa711a-651a-409a-a7d4-5ad27c30a140-1502985405500.png",
                    "twitter:title": "Kurtosys - SQL Data Specialist",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Maintaining and building SQL Server Integration Services (SSIS) jobs; \nMaintaining and developing custom Microsoft C# or Node JS loaders for \nsolutions that fall\u00a0...",
        "title": "Kurtosys - SQL Data Specialist"
    },
    {
        "cacheId": "Xj-l88xmDp4J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../a0e072b1-73fb-4492-96bb-bbbfb4469132",
        "htmlFormattedUrl": "https://jobs.lever.co/.../a0e072b1-73fb-4492-96bb-bbbfb4469132",
        "htmlSnippet": "Our R&amp;D team works with the latest technologies to create our innovative <br>\nplatform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, <b>C#</b>, Scala, <br>\nInternet&nbsp;...",
        "htmlTitle": "Mendix - Senior Frontend Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/mendix/a0e072b1-73fb-4492-96bb-bbbfb4469132",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "125",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRnynl1eHE8prhfLNU0wZgSen53PbGkIcLcCtJDIaiOQs8dfDzqLHcxsZY",
                    "width": "402"
                }
            ],
            "metatags": [
                {
                    "og:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Mendix - Senior Frontend Developer",
                    "og:url": "https://jobs.lever.co/mendix/a0e072b1-73fb-4492-96bb-bbbfb4469132",
                    "twitter:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644141599.png",
                    "twitter:title": "Mendix - Senior Frontend Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Our R&D team works with the latest technologies to create our innovative \nplatform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, \nInternet\u00a0...",
        "title": "Mendix - Senior Frontend Developer"
    },
    {
        "cacheId": "6fyJoSKgPyUJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/gigya",
        "htmlFormattedUrl": "https://jobs.lever.co/gigya",
        "htmlSnippet": "<b>C#</b> Server Side Team Leader. Tel Aviv ... Experienced <b>C#</b> Server Developer. Tel <br>\nAviv ... Senior <b>C#</b> Infrastructure/server developer. Tel Aviv&nbsp;...",
        "htmlTitle": "Gigya",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/gigya",
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
                    "og:description": "Job openings at Gigya",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1483032404076.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Gigya jobs",
                    "og:url": "https://jobs.lever.co/gigya",
                    "twitter:description": "Job openings at Gigya",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1481204313579.png",
                    "twitter:title": "Gigya",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "C# Server Side Team Leader. Tel Aviv ... Experienced C# Server Developer. Tel \nAviv ... Senior C# Infrastructure/server developer. Tel Aviv\u00a0...",
        "title": "Gigya"
    },
    {
        "cacheId": "wPpykuQK1dAJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../e0f3b094-959b-4759-9a10-5110abb30dd2",
        "htmlFormattedUrl": "https://jobs.lever.co/.../e0f3b094-959b-4759-9a10-5110abb30dd2",
        "htmlSnippet": "On the mobile side we also use Objective-C, Java (both for Android and back-<br>\nend), <b>C#</b>, and client-side JavaScript. Our platform is fully run on top of AWS in a&nbsp;...",
        "htmlTitle": "CloudMine - Platform Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/cloudmineinc/e0f3b094-959b-4759-9a10-5110abb30dd2",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/Cloudmine.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "126",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRqbFLu5PrdVNHIryoKDvaiWc151dAzTFuXbpLq_32Ry_p6VBSbRYG1GAw",
                    "width": "240"
                }
            ],
            "metatags": [
                {
                    "og:description": "About CloudMine CloudMine, through its Connected Health Cloud, solves the technical complexities of healthcare innovation and empowers leaders to bring truly impactful solutions to market significantly faster than ever imagined. By removing challenges such as compliance, security, and interoperability, innovators across Healthcare, Pharmaceuticals, Biotechnology and more are able to truly focus on improving the patient experience, reducing readmissions, and creating better outcomes. CloudMine\u2019s Connected Health Cloud is accelerating healthcare innovation where it\u2019s needed most in data analytics, clinical research, treatment adherence, and chronic disease management. Headquartered in Center City, Philadelphia, we have two additional locations in Chicago, IL and Boston, MA. Our team is made up of fast moving technologists that thrive on customer success. Job Description We are looking for self-motivated engineers to join our team to help take our product to the next level. You will",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/Cloudmine.png",
                    "og:image:height": "200",
                    "og:title": "CloudMine - Platform Engineer",
                    "og:url": "https://jobs.lever.co/cloudmineinc/e0f3b094-959b-4759-9a10-5110abb30dd2",
                    "twitter:description": "About CloudMine CloudMine, through its Connected Health Cloud, solves the technical complexities of healthcare innovation and empowers leaders to bring truly impactful solutions to market significantly faster than ever imagined. By removing challenges such as compliance, security, and interoperability, innovators across Healthcare, Pharmaceuticals, Biotechnology and more are able to truly focus on improving the patient experience, reducing readmissions, and creating better outcomes. CloudMine\u2019s Connected Health Cloud is accelerating healthcare innovation where it\u2019s needed most in data analytics, clinical research, treatment adherence, and chronic disease management. Headquartered in Center City, Philadelphia, we have two additional locations in Chicago, IL and Boston, MA. Our team is made up of fast moving technologists that thrive on customer success. Job Description We are looking for self-motivated engineers to join our team to help take our product to the next level. You will",
                    "twitter:title": "CloudMine - Platform Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "On the mobile side we also use Objective-C, Java (both for Android and back-\nend), C#, and client-side JavaScript. Our platform is fully run on top of AWS in a\u00a0...",
        "title": "CloudMine - Platform Engineer"
    },
    {
        "cacheId": "k5-El-k0xlYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/gigya?by=location",
        "htmlFormattedUrl": "https://jobs.lever.co/gigya?by=location",
        "htmlSnippet": "<b>C#</b> Server Side Team Leader. Tel Aviv, IsraelEngineeringFull-Time &middot; Apply ... <br>\nSenior <b>C#</b> Infrastructure/server developer. Tel Aviv, IsraelEngineeringFull-time.",
        "htmlTitle": "Gigya",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/gigya?by=location",
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
                    "og:description": "Job openings at Gigya",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1483032404076.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Gigya jobs",
                    "og:url": "https://jobs.lever.co/gigya",
                    "twitter:description": "Job openings at Gigya",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/e9edeb96-ca19-437c-b6ae-4ffd8bb878f9-1481204313579.png",
                    "twitter:title": "Gigya",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "C# Server Side Team Leader. Tel Aviv, IsraelEngineeringFull-Time \u00b7 Apply ... \nSenior C# Infrastructure/server developer. Tel Aviv, IsraelEngineeringFull-time.",
        "title": "Gigya"
    },
    {
        "cacheId": "9aUe-tQk61oJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../48ae283f-f8aa-4179-a908-d556b177fed5",
        "htmlFormattedUrl": "https://jobs.lever.co/.../48ae283f-f8aa-4179-a908-d556b177fed5",
        "htmlSnippet": "Our R&amp;D team works with the latest technologies to create our innovative <br>\nplatform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, <b>C#</b>, Scala, <br>\nInternet&nbsp;...",
        "htmlTitle": "Mendix - React / MobX Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/mendix/48ae283f-f8aa-4179-a908-d556b177fed5",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "125",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRnynl1eHE8prhfLNU0wZgSen53PbGkIcLcCtJDIaiOQs8dfDzqLHcxsZY",
                    "width": "402"
                }
            ],
            "metatags": [
                {
                    "og:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you. Our team is responsible for all the core services of the IDE and some of its edi",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Mendix - React / MobX Developer",
                    "og:url": "https://jobs.lever.co/mendix/48ae283f-f8aa-4179-a908-d556b177fed5",
                    "twitter:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you. Our team is responsible for all the core services of the IDE and some of its edi",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644141599.png",
                    "twitter:title": "Mendix - React / MobX Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Our R&D team works with the latest technologies to create our innovative \nplatform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, \nInternet\u00a0...",
        "title": "Mendix - React / MobX Developer"
    },
    {
        "cacheId": "w4onggHg7NQJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/kurtosys/ba28c3d0-afe0-4d3e-a883.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/kurtosys/ba28c3d0-afe0-4d3e-a883.../apply",
        "htmlSnippet": "Web Application Engineer - Secure Portal. Cape Town, Claremont, South Africa. <br>\nEngineering. Full-time. Submit your application. Resume/CV \u2731. ATTACH&nbsp;...",
        "htmlTitle": "Kurtosys - Web Application Engineer - Secure Portal",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/kurtosys/ba28c3d0-afe0-4d3e-a883-53509e7de50d/",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/3cfa711a-651a-409a-a7d4-5ad27c30a140-1493221516647.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "49",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQkBlGbD0BEmIRfGppkJVKABm9cTxsdrXGEA07Jl0aDKJfUMTHVvcJQdA",
                    "width": "332"
                }
            ],
            "metatags": [
                {
                    "og:description": "INTRODUCTION This is a Software Engineering role to work on the Kurtosys Secure Portal application. The role requires technical experience with the development of secure web applications, good organizational and planning skills, and the candidate must be comfortable consuming and creating written technical design documentation. The role involves working closely with API developers, the QA team, Business Analysis and Project Managers both on and offshore.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/3cfa711a-651a-409a-a7d4-5ad27c30a140-1493221516647.png",
                    "og:image:height": "200",
                    "og:title": "Kurtosys - Web Application Engineer - Secure Portal",
                    "og:url": "https://jobs.lever.co/kurtosys/ba28c3d0-afe0-4d3e-a883-53509e7de50d/apply",
                    "twitter:description": "INTRODUCTION This is a Software Engineering role to work on the Kurtosys Secure Portal application. The role requires technical experience with the development of secure web applications, good organizational and planning skills, and the candidate must be comfortable consuming and creating written technical design documentation. The role involves working closely with API developers, the QA team, Business Analysis and Project Managers both on and offshore.",
                    "twitter:title": "Kurtosys - Web Application Engineer - Secure Portal",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Web Application Engineer - Secure Portal. Cape Town, Claremont, South Africa. \nEngineering. Full-time. Submit your application. Resume/CV \u2731. ATTACH\u00a0...",
        "title": "Kurtosys - Web Application Engineer - Secure Portal"
    },
    {
        "cacheId": "SucfbyKoop8J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../87481a21-900a-4a67-95be-778b7286e555",
        "htmlFormattedUrl": "https://jobs.lever.co/.../87481a21-900a-4a67-95be-778b7286e555",
        "htmlSnippet": "2+ years building applications in a mainstream programming language: Python, <br>\nPHP, Ruby, <b>C#</b>, C++, Java, etc. 2+ years of experience using some form of web&nbsp;...",
        "htmlTitle": "Eventbrite - Software Engineer - Financial",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/eventbrite/87481a21-900a-4a67-95be-778b7286e555",
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
                    "og:description": "THE CHALLENGE Financial Engineering is incredibly important for any global marketplace. The success of the business as well as its customers depends on building and maintaining a best-in-class financial ecosystem that produces, monitors, and validates Eventbrite\u2019s data. We're looking for a strong Engineer to join our Financial Foundry team to help us take our financial platform to the next level. THE TEAM The Financial Foundry team is responsible for building infrastructure for, and maintaining the health of, the Eventbrite financial ecosystem. We are tasked with ensuring that Eventbrite's marketplace is as stable, scalable, and as accurate as possible. The team builds tools and processes to manipulate, move, audit, and reconcile financial data. We also consult other teams on best practices when working with high-risk data and code. One thing you should know: we're a people-focused organization. Engineers help each other, work on problems together, mentor each other, fail togeth",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1488492166844.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Eventbrite - Software Engineer - Financial",
                    "og:url": "https://jobs.lever.co/eventbrite/87481a21-900a-4a67-95be-778b7286e555",
                    "twitter:description": "THE CHALLENGE Financial Engineering is incredibly important for any global marketplace. The success of the business as well as its customers depends on building and maintaining a best-in-class financial ecosystem that produces, monitors, and validates Eventbrite\u2019s data. We're looking for a strong Engineer to join our Financial Foundry team to help us take our financial platform to the next level. THE TEAM The Financial Foundry team is responsible for building infrastructure for, and maintaining the health of, the Eventbrite financial ecosystem. We are tasked with ensuring that Eventbrite's marketplace is as stable, scalable, and as accurate as possible. The team builds tools and processes to manipulate, move, audit, and reconcile financial data. We also consult other teams on best practices when working with high-risk data and code. One thing you should know: we're a people-focused organization. Engineers help each other, work on problems together, mentor each other, fail togeth",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1476237511604.png",
                    "twitter:title": "Eventbrite - Software Engineer - Financial",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "2+ years building applications in a mainstream programming language: Python, \nPHP, Ruby, C#, C++, Java, etc. 2+ years of experience using some form of web\u00a0...",
        "title": "Eventbrite - Software Engineer - Financial"
    },
    {
        "cacheId": "vZPaX1dzKIYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../eb5c45a9-c385-427b-b35a-242a72dd1268",
        "htmlFormattedUrl": "https://jobs.lever.co/.../eb5c45a9-c385-427b-b35a-242a72dd1268",
        "htmlSnippet": "3+ years building applications in a mainstream programming language: Python, <br>\nPHP, Ruby, <b>C#</b>, C++, Java, etc. 2+ years of experience using some form of web&nbsp;...",
        "htmlTitle": "Eventbrite - Software Engineer - Back End",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/eventbrite/eb5c45a9-c385-427b-b35a-242a72dd1268",
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
                    "og:description": "THE CHALLENGE Last year at Eventbrite organizers created 3 million events and we processed 150 million tickets. Behind all of those tickets and events is a number of teams working together to keep our product scalable and available as we grow. The Segment Services team is responsible for a number of the core services that help make Eventbrite successful, and we want you to be a part of that success. THE TEAM Our team is responsible for the APIs and services that our organizers depend upon. We have a few core services that are our primary responsibility, but we also work closely with other teams to help them meet their needs and goals. Getting to work this team means getting to touch a wide array of the pieces that make up Eventbrite. You can learn more about the team from some of our engineers. THE ROLE In this role you\u2019ll work closely with a small team of bright, dedicated engineers improving some of our most core services, and providing valuable feedback to the rest of the compa",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1488492166844.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Eventbrite - Software Engineer - Back End",
                    "og:url": "https://jobs.lever.co/eventbrite/eb5c45a9-c385-427b-b35a-242a72dd1268",
                    "twitter:description": "THE CHALLENGE Last year at Eventbrite organizers created 3 million events and we processed 150 million tickets. Behind all of those tickets and events is a number of teams working together to keep our product scalable and available as we grow. The Segment Services team is responsible for a number of the core services that help make Eventbrite successful, and we want you to be a part of that success. THE TEAM Our team is responsible for the APIs and services that our organizers depend upon. We have a few core services that are our primary responsibility, but we also work closely with other teams to help them meet their needs and goals. Getting to work this team means getting to touch a wide array of the pieces that make up Eventbrite. You can learn more about the team from some of our engineers. THE ROLE In this role you\u2019ll work closely with a small team of bright, dedicated engineers improving some of our most core services, and providing valuable feedback to the rest of the compa",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1476237511604.png",
                    "twitter:title": "Eventbrite - Software Engineer - Back End",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "3+ years building applications in a mainstream programming language: Python, \nPHP, Ruby, C#, C++, Java, etc. 2+ years of experience using some form of web\u00a0...",
        "title": "Eventbrite - Software Engineer - Back End"
    },
    {
        "cacheId": "AeeYcGEdYBQJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../78f4206b-7813-4d92-b220-c87b3b75fbc0",
        "htmlFormattedUrl": "https://jobs.lever.co/.../78f4206b-7813-4d92-b220-c87b3b75fbc0",
        "htmlSnippet": "... work with Python and Django web framework; 5+ years building applications in <br>\na mainstream programming language: Python, PHP, Ruby, <b>C#</b>, C++, Java, etc.",
        "htmlTitle": "Eventbrite - Senior Software Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/eventbrite/78f4206b-7813-4d92-b220-c87b3b75fbc0",
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
                    "og:description": "THE TEAM We opened our Mendoza office two years ago, merging with Eventioz, a local company, and we are looking to grow our amazing southeast engineering team. Hear from the Mendoza Engineering team and meet Ariel Chiat, Engineering Manager in Mendoza. Our primary stack is Python, Django, and Celery, all running on AWS with a MySQL backend. Some of the other tools that we use are Redis, RabbitMQ, Cassandra, Hbase, Hive, Backbone, Sass, Git, and an endless supply of coffee. Haven\u2019t worked with these technologies before? This is an amazing chance to jump in and learn. One thing you should know: we're a people-focused organization. Engineers help each other, work on problems together, mentor each other, fail together, and actively develop their careers. Weekly demos, tech talks, and quarterly hackathons are at the core of how we\u2019ve built our team and product.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1488492166844.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Eventbrite - Senior Software Engineer",
                    "og:url": "https://jobs.lever.co/eventbrite/78f4206b-7813-4d92-b220-c87b3b75fbc0",
                    "twitter:description": "THE TEAM We opened our Mendoza office two years ago, merging with Eventioz, a local company, and we are looking to grow our amazing southeast engineering team. Hear from the Mendoza Engineering team and meet Ariel Chiat, Engineering Manager in Mendoza. Our primary stack is Python, Django, and Celery, all running on AWS with a MySQL backend. Some of the other tools that we use are Redis, RabbitMQ, Cassandra, Hbase, Hive, Backbone, Sass, Git, and an endless supply of coffee. Haven\u2019t worked with these technologies before? This is an amazing chance to jump in and learn. One thing you should know: we're a people-focused organization. Engineers help each other, work on problems together, mentor each other, fail together, and actively develop their careers. Weekly demos, tech talks, and quarterly hackathons are at the core of how we\u2019ve built our team and product.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/31d06651-3ca0-4cc3-be3d-61f238e8cdc1-1476237511604.png",
                    "twitter:title": "Eventbrite - Senior Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... work with Python and Django web framework; 5+ years building applications in \na mainstream programming language: Python, PHP, Ruby, C#, C++, Java, etc.",
        "title": "Eventbrite - Senior Software Engineer"
    },
    {
        "cacheId": "bqpGsYN3G3sJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/f2537fe4-6c4e-4f22-a002-4455dda80675",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/f2537fe4-6c4e-4f22-a002-4455dda80675",
        "htmlSnippet": "Demonstrated software development proficiency (Go, Ruby, Python, Java, <b>C#</b>, <br>\nObj-C/Swift); Comprehension of algorithms and processes for programmatic&nbsp;...",
        "htmlTitle": "Twitch - Application Security Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/f2537fe4-6c4e-4f22-a002-4455dda80675",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Twitch is looking for a focused Application Security Engineer with a desire to play on the Blue Team. Maybe you\u2019re a pentester who is bored of always winning; maybe you\u2019re the local security champion within your development organization. However you got to where you are, we want one thing from you - help make Twitch\u2019s products as safe as they can be for our partners and viewers. In this role, you will be escorting Twitch\u2019s products and features from ideation to deployment. You will be providing consulting to product teams looking to try new things safely. You will be reviewing critical passages of code for adherence to standards and safe practices. Most importantly, you will be helping to build and automate the tools that do the above for you as a force multiplier. And yes, where warranted, there\u2019s some pentesting in it for you as well. You know, if you\u2019re into that.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Application Security Engineer",
                    "og:url": "https://jobs.lever.co/twitch/f2537fe4-6c4e-4f22-a002-4455dda80675",
                    "twitter:description": "Twitch is looking for a focused Application Security Engineer with a desire to play on the Blue Team. Maybe you\u2019re a pentester who is bored of always winning; maybe you\u2019re the local security champion within your development organization. However you got to where you are, we want one thing from you - help make Twitch\u2019s products as safe as they can be for our partners and viewers. In this role, you will be escorting Twitch\u2019s products and features from ideation to deployment. You will be providing consulting to product teams looking to try new things safely. You will be reviewing critical passages of code for adherence to standards and safe practices. Most importantly, you will be helping to build and automate the tools that do the above for you as a force multiplier. And yes, where warranted, there\u2019s some pentesting in it for you as well. You know, if you\u2019re into that.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Application Security Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Demonstrated software development proficiency (Go, Ruby, Python, Java, C#, \nObj-C/Swift); Comprehension of algorithms and processes for programmatic\u00a0...",
        "title": "Twitch - Application Security Engineer"
    },
    {
        "cacheId": "LcB4-0d3J30J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../6ab1ed78-430f-4e9c-8887-fee398045038",
        "htmlFormattedUrl": "https://jobs.lever.co/.../6ab1ed78-430f-4e9c-8887-fee398045038",
        "htmlSnippet": "... Experienced in <b>C#</b>; Experience of setting up test automation frameworks from <br>\nscratch; Understanding of agile methodologies such as test driven development,<br>\n&nbsp;...",
        "htmlTitle": "Trainline - Software Development Engineer in Test (SDET)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/thetrainline/6ab1ed78-430f-4e9c-8887-fee398045038",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/e7325281-bcf1-44ee-8fbb-cac3cc210349-1491409888732.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "112",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQ0KZwVSoEOnN4-xPVXPIcI5xCTSQ2R1Pte6AGPcbPttjWzL1hfHo56wQ",
                    "width": "450"
                }
            ],
            "metatags": [
                {
                    "og:description": "Purpose of the role.. To be the quality conscience of the Ecommerce/Online Payments team, actively bringing consideration of quality to all activities of the team from discovery thru implementation to operational running.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/e7325281-bcf1-44ee-8fbb-cac3cc210349-1491409888732.png",
                    "og:image:height": "200",
                    "og:title": "Trainline - Software Development Engineer in Test (SDET)",
                    "og:url": "https://jobs.lever.co/thetrainline/6ab1ed78-430f-4e9c-8887-fee398045038",
                    "twitter:description": "Purpose of the role.. To be the quality conscience of the Ecommerce/Online Payments team, actively bringing consideration of quality to all activities of the team from discovery thru implementation to operational running.",
                    "twitter:title": "Trainline - Software Development Engineer in Test (SDET)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... Experienced in C#; Experience of setting up test automation frameworks from \nscratch; Understanding of agile methodologies such as test driven development,\n\u00a0...",
        "title": "Trainline - Software Development Engineer in Test (SDET)"
    },
    {
        "cacheId": "J0hGAsplMeYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/pmxagency/0209b453-173b-4b05.../apply",
        "htmlFormattedUrl": "https://jobs.lever.co/pmxagency/0209b453-173b-4b05.../apply",
        "htmlSnippet": "Do you have at least 3 years of experience in <b>C#</b> ASP.NET development? Are <br>\nyou proficient in SQL? Are you comfortable mentoring other engineers?",
        "htmlTitle": "PMX Agency - Application Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/pmxagency/0209b453-173b-4b05-9f43-b1c603f54cdc/",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/4d84a8c6-35d5-4470-97d9-4a6614f62180-1481234499343.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "161",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRVrS3JZVlLTMRJooypP4H1_JW3DO0cF6BDFAnWExLRCaEdp-qfgQmH9c0",
                    "width": "313"
                }
            ],
            "metatags": [
                {
                    "og:description": "PMX Agency is a global independent integrated marketing agency that leads with an insight-driven, consumer-centric approach to performance. With a history steeped in performance marketing, PMX Agency combines an intuitive knowledge of the customer experience with customized, scalable strategies that address clients' most pressing business challenges, across: research, customer analytics, SEM, display, affiliate marketing, SEO, content, social, email, direct mail, print and insert, creative, website development and performance management. We are looking for a C# Developer responsible for building C# applications, including anything from back-end services to their user-facing counterparts. Your primary responsibilities will be to design and develop these applications, and to coordinate with the rest of the team working on different layers of the infrastructure. We have a tight knit team with a results oriented and supportive culture, so a true commitment to collaborative problem solvin",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/4d84a8c6-35d5-4470-97d9-4a6614f62180-1481234499343.png",
                    "og:image:height": "200",
                    "og:title": "PMX Agency - Application Developer",
                    "og:url": "https://jobs.lever.co/pmxagency/0209b453-173b-4b05-9f43-b1c603f54cdc/apply",
                    "twitter:description": "PMX Agency is a global independent integrated marketing agency that leads with an insight-driven, consumer-centric approach to performance. With a history steeped in performance marketing, PMX Agency combines an intuitive knowledge of the customer experience with customized, scalable strategies that address clients' most pressing business challenges, across: research, customer analytics, SEM, display, affiliate marketing, SEO, content, social, email, direct mail, print and insert, creative, website development and performance management. We are looking for a C# Developer responsible for building C# applications, including anything from back-end services to their user-facing counterparts. Your primary responsibilities will be to design and develop these applications, and to coordinate with the rest of the team working on different layers of the infrastructure. We have a tight knit team with a results oriented and supportive culture, so a true commitment to collaborative problem solvin",
                    "twitter:title": "PMX Agency - Application Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Do you have at least 3 years of experience in C# ASP.NET development? Are \nyou proficient in SQL? Are you comfortable mentoring other engineers?",
        "title": "PMX Agency - Application Developer"
    },
    {
        "cacheId": "6tL2_6pBHnoJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/circleci/dff63474-0350-4a76-9638-fec92aceba5e",
        "htmlFormattedUrl": "https://jobs.lever.co/circleci/dff63474-0350-4a76-9638-fec92aceba5e",
        "htmlSnippet": "Code development and debugging on Windows; Code development utilizing <br>\nVisual Studio in programming languages including C, C++, <b>C#</b>; Develop software<br>\n&nbsp;...",
        "htmlTitle": "CircleCI - Product Manager",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/circleci/dff63474-0350-4a76-9638-fec92aceba5e",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/circle-logo-horizontal.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "110",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRkKHbO9jzZy44Lc9SCqUkGBJ0VsGlWt5Tgm1A-QQNjTaGNOjxMNjm1eg",
                    "width": "459"
                }
            ],
            "metatags": [
                {
                    "og:description": "About Product Management at CircleCI Manage the design of software development tools and products from definition to deployment. Own the product strategy, roadmap, and execution of software products. Work closely with engineering to establish client requirements and define the product vision. Work in cross-functional teams to synthesize data and user-research to drive automated engineering decision making. Set the product strategy, prioritize software product features, build engineering an consensus and coordinate product schedules. Build use cases. Integrate usability studies, user research, market analysis, and industry feedback into the product requirements. Define methods and metrics for success, communicate clear objectives, and track team performance. Coordinate with other product managers, designers and engineers to ensure a uniform user experience. About CircleCI Velocity is critical for software teams in today's competitive landscape, but maintaining speed can be difficul",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/circle-logo-horizontal.png",
                    "og:image:height": "200",
                    "og:title": "CircleCI - Product Manager",
                    "og:url": "https://jobs.lever.co/circleci/dff63474-0350-4a76-9638-fec92aceba5e",
                    "twitter:description": "About Product Management at CircleCI Manage the design of software development tools and products from definition to deployment. Own the product strategy, roadmap, and execution of software products. Work closely with engineering to establish client requirements and define the product vision. Work in cross-functional teams to synthesize data and user-research to drive automated engineering decision making. Set the product strategy, prioritize software product features, build engineering an consensus and coordinate product schedules. Build use cases. Integrate usability studies, user research, market analysis, and industry feedback into the product requirements. Define methods and metrics for success, communicate clear objectives, and track team performance. Coordinate with other product managers, designers and engineers to ensure a uniform user experience. About CircleCI Velocity is critical for software teams in today's competitive landscape, but maintaining speed can be difficul",
                    "twitter:title": "CircleCI - Product Manager",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Code development and debugging on Windows; Code development utilizing \nVisual Studio in programming languages including C, C++, C#; Develop software\n\u00a0...",
        "title": "CircleCI - Product Manager"
    },
    {
        "cacheId": "F3-wzHV2nvcJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../1fe8241f-3430-4a5c-a3f6-004ad9a3b7b3",
        "htmlFormattedUrl": "https://jobs.lever.co/.../1fe8241f-3430-4a5c-a3f6-004ad9a3b7b3",
        "htmlSnippet": "... Experience with one or more general purpose programming languages <br>\nincluding but not limited to: Java, C/C++, <b>C#</b>, Objective C, Python, JavaScript, or <br>\nGo&nbsp;...",
        "htmlTitle": "Essential Products - Software Engineer, Home",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/essential/1fe8241f-3430-4a5c-a3f6-004ad9a3b7b3",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/d85708a4-14af-45f7-9d26-2003f4d9818e-1498075785866.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "128",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjTKmzFnkRDPVKl3TpCatuhbyoLoqnkObbuof00JyFxJ8eqCPjlpIkWjRm",
                    "width": "394"
                }
            ],
            "metatags": [
                {
                    "og:description": "We are working on technologies and products to simplify and improve the way people interact with their home devices and services. We envision people's homes as entities capable of sensing and managing the devices and services they contain, capable of offering a unified experience to interact with their resources, and capable, as well, of proactively reaching out to the people that inhabit them. We are looking for software engineers to help us build this vision. If you are passionate about home automation and have experience with distributed systems, artificial intelligence, media services, systems, or middleware services please do not hesitate to contact us.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/d85708a4-14af-45f7-9d26-2003f4d9818e-1498075785866.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Essential Products - Software Engineer, Home",
                    "og:url": "https://jobs.lever.co/essential/1fe8241f-3430-4a5c-a3f6-004ad9a3b7b3",
                    "twitter:description": "We are working on technologies and products to simplify and improve the way people interact with their home devices and services. We envision people's homes as entities capable of sensing and managing the devices and services they contain, capable of offering a unified experience to interact with their resources, and capable, as well, of proactively reaching out to the people that inhabit them. We are looking for software engineers to help us build this vision. If you are passionate about home automation and have experience with distributed systems, artificial intelligence, media services, systems, or middleware services please do not hesitate to contact us.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/d85708a4-14af-45f7-9d26-2003f4d9818e-1498075790059.png",
                    "twitter:title": "Essential Products - Software Engineer, Home",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... Experience with one or more general purpose programming languages \nincluding but not limited to: Java, C/C++, C#, Objective C, Python, JavaScript, or \nGo\u00a0...",
        "title": "Essential Products - Software Engineer, Home"
    },
    {
        "cacheId": "5OytZqWPL5cJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../98dc8552-fad7-4639-a0c2-4bed7addcfa3",
        "htmlFormattedUrl": "https://jobs.lever.co/.../98dc8552-fad7-4639-a0c2-4bed7addcfa3",
        "htmlSnippet": "... UX framework experience (Facebook React, Angular, JQuery) a plus; Expertise <br>\nin multiple programming languages, especially Java, Golang, <b>C#</b>; Comfort with&nbsp;...",
        "htmlTitle": "Frankly Inc. - SENIOR SOFTWARE DIRECTOR",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/franklyinc/98dc8552-fad7-4639-a0c2-4bed7addcfa3",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/0301deeb-d720-49d0-b38a-1a664131996f-1489534955930.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS_1kS5hGhl2bSZNuHIlMEDztH7aHQkzNM6D5jp_Sjt3rowoTTTGrjV4TEs",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "Frankly builds an integrated media platform for brands and media companies to create, distribute, analyze and monetize their content across all of their digital properties on web, mobile, and TV. Our customers include NBC, ABC, CBS and FOX affiliates, as well as top fashion brands, professional sports franchises and global organizations. Collectively, we reach nearly 80 million monthly users in the United States. The Company is publicly listed on the TSX Venture Exchange and trading under ticker \"TLK.\" Frankly is headquartered in San Francisco with major offices in New York. To learn more, please visit www.franklyinc.com. We are looking for a Senior Software Director.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/0301deeb-d720-49d0-b38a-1a664131996f-1489534955930.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Frankly Inc. - SENIOR SOFTWARE DIRECTOR",
                    "og:url": "https://jobs.lever.co/franklyinc/98dc8552-fad7-4639-a0c2-4bed7addcfa3",
                    "twitter:description": "Frankly builds an integrated media platform for brands and media companies to create, distribute, analyze and monetize their content across all of their digital properties on web, mobile, and TV. Our customers include NBC, ABC, CBS and FOX affiliates, as well as top fashion brands, professional sports franchises and global organizations. Collectively, we reach nearly 80 million monthly users in the United States. The Company is publicly listed on the TSX Venture Exchange and trading under ticker \"TLK.\" Frankly is headquartered in San Francisco with major offices in New York. To learn more, please visit www.franklyinc.com. We are looking for a Senior Software Director.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/0301deeb-d720-49d0-b38a-1a664131996f-1489534946489.png",
                    "twitter:title": "Frankly Inc. - SENIOR SOFTWARE DIRECTOR",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... UX framework experience (Facebook React, Angular, JQuery) a plus; Expertise \nin multiple programming languages, especially Java, Golang, C#; Comfort with\u00a0...",
        "title": "Frankly Inc. - SENIOR SOFTWARE DIRECTOR"
    },
    {
        "cacheId": "4JnQJ9UcOzgJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../262788f2-f88d-40bf-bfbd-9d1855718eac",
        "htmlFormattedUrl": "https://jobs.lever.co/.../262788f2-f88d-40bf-bfbd-9d1855718eac",
        "htmlSnippet": "5+ years of experience with software development in production; 3+ years of <br>\nexperience in working with <b>C#</b>, Unity, C++, graphics, shaders; Familiarity with&nbsp;...",
        "htmlTitle": "Luminar - Simulation Software Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/luminartech/262788f2-f88d-40bf-bfbd-9d1855718eac",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/18db9738-16b4-4c76-b845-07b16b5cfa21-1499986304249.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "89",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSFvf6FeCSFHt31BBS3B_ZWXQoYUt_5mNAAv__XU_Fd4rLXnz05WEurVA",
                    "width": "568"
                }
            ],
            "metatags": [
                {
                    "og:description": "Our vision is to power every autonomous vehicle with the first LiDAR capable of making them both safe and scalable. It\u2019s easy to get an autonomous vehicle to work 99% of the time, but it\u2019s the last 1% that\u2019s preventing them from becoming a reality. That\u2019s where we come in. We\u2019ve built a breakthrough LiDAR from the chip level up, delivering 50x better resolution and 10x longer range than the most advanced LiDARs available today. Luminar is not just a sensor, but the core of a platform that can enable the industry to have safe autonomous vehicles on the road. We are a diverse team of passionate and driven individuals, making us a powerhouse of innovation, design, engineering, and manufacturing. We are hiring the best and the brightest to accelerate the industry, and bring forward the next transportation revolution. OPPORTUNITY Luminar Technologies, Inc. is currently seeking applicants for a Simulation Software Engineer in Orlando, FL JOB DESCRIPTION We are looking for a",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/18db9738-16b4-4c76-b845-07b16b5cfa21-1499986304249.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Luminar - Simulation Software Engineer",
                    "og:url": "https://jobs.lever.co/luminartech/262788f2-f88d-40bf-bfbd-9d1855718eac",
                    "twitter:description": "Our vision is to power every autonomous vehicle with the first LiDAR capable of making them both safe and scalable. It\u2019s easy to get an autonomous vehicle to work 99% of the time, but it\u2019s the last 1% that\u2019s preventing them from becoming a reality. That\u2019s where we come in. We\u2019ve built a breakthrough LiDAR from the chip level up, delivering 50x better resolution and 10x longer range than the most advanced LiDARs available today. Luminar is not just a sensor, but the core of a platform that can enable the industry to have safe autonomous vehicles on the road. We are a diverse team of passionate and driven individuals, making us a powerhouse of innovation, design, engineering, and manufacturing. We are hiring the best and the brightest to accelerate the industry, and bring forward the next transportation revolution. OPPORTUNITY Luminar Technologies, Inc. is currently seeking applicants for a Simulation Software Engineer in Orlando, FL JOB DESCRIPTION We are looking for a",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/18db9738-16b4-4c76-b845-07b16b5cfa21-1499973943868.png",
                    "twitter:title": "Luminar - Simulation Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "5+ years of experience with software development in production; 3+ years of \nexperience in working with C#, Unity, C++, graphics, shaders; Familiarity with\u00a0...",
        "title": "Luminar - Simulation Software Engineer"
    },
    {
        "cacheId": "hvR82k33zE0J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7",
        "htmlFormattedUrl": "https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7",
        "htmlSnippet": "Twitch is building the future of interactive entertainment. The services we create <br>\nfor our users have deep, lasting effects on their lives. For many of our partnered&nbsp;...",
        "htmlTitle": "Twitch - Senior Software Engineer - Payments",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "86",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQwhiiUaX0nLhDUxpLDdXLy7EDppirezOyA1X1YPxZRDP9S-46TKPSCZug",
                    "width": "258"
                }
            ],
            "metatags": [
                {
                    "og:description": "Twitch is building the future of interactive entertainment. The services we create for our users have deep, lasting effects on their lives. For many of our partnered broadcasters, streaming on Twitch is a career, and our payments system is central to making that possible. We're looking for a software engineer who gets why the story, \"I bought a sub using my favorite streamer's sub button so I can talk in sub-only chat\" starts off looking simple, but isn't. You like wrangling existing technologies together to solve business problems. Maybe you've built an e-commerce site or two. On our team, you'll specialize in payments and related products like emotes and Turbo. Together, we're transforming the gaming world, $4.99 at a time.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504280272.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Twitch - Senior Software Engineer - Payments",
                    "og:url": "https://jobs.lever.co/twitch/88db8123-cd6b-437e-aabf-7acec6df54d7",
                    "twitter:description": "Twitch is building the future of interactive entertainment. The services we create for our users have deep, lasting effects on their lives. For many of our partnered broadcasters, streaming on Twitch is a career, and our payments system is central to making that possible. We're looking for a software engineer who gets why the story, \"I bought a sub using my favorite streamer's sub button so I can talk in sub-only chat\" starts off looking simple, but isn't. You like wrangling existing technologies together to solve business problems. Maybe you've built an e-commerce site or two. On our team, you'll specialize in payments and related products like emotes and Turbo. Together, we're transforming the gaming world, $4.99 at a time.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/afe693b8-cabb-45ce-8e8b-df618719e86f-1474504133475.png",
                    "twitter:title": "Twitch - Senior Software Engineer - Payments",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Twitch is building the future of interactive entertainment. The services we create \nfor our users have deep, lasting effects on their lives. For many of our partnered\u00a0...",
        "title": "Twitch - Senior Software Engineer - Payments"
    },
    {
        "cacheId": "34IQy9FsNzUJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../89287bd6-3beb-4c1a-b028-b0f62a58cf66",
        "htmlFormattedUrl": "https://jobs.lever.co/.../89287bd6-3beb-4c1a-b028-b0f62a58cf66",
        "htmlSnippet": "Fluency in C / Python / <b>C#</b> / .NET / - including unit testing, data analysis / <br>\nvisualization; Extreme attention to detail. Apply for this job &middot; KeepTruckin Home <br>\nPage.",
        "htmlTitle": "KeepTruckin - Embedded Software Engineer for Test",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/keeptruckin/89287bd6-3beb-4c1a-b028-b0f62a58cf66",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/929b350a-5ba5-4026-bb4f-0187a71d1371-1487288167719.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcReux21EcElRNdqzUTZpg2TNQX4I1XtIkkQ0_FVw7v65Hky8sYowyjY6tc",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "KeepTruckin is on a mission to improve the efficiency of America\u2019s trucking industry by connecting the millions of drivers and vehicles that haul freight on our roads. We are backed by Google Ventures and Index Ventures. In 2015, the U.S. Department of Transportation announced regulation that will require 4.5 million interstate truck drivers to use an Electronic Logging Device (ELD) to record their hours of service with the goal of improving road safety and reducing the paperwork burden on the industry. With the leading ELD in the market, KeepTruckin is poised to build the largest network of connected commercial vehicles in the world. The massive data generated from this network presents an opportunity to fundamentally change the way the trucking market operates. As an Embedded Software Engineer for Test, you have an amazing opportunity to shape the way we develop our products. We are looking for candidates with a strong S/W development background, with hands-on experience testing",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/929b350a-5ba5-4026-bb4f-0187a71d1371-1487288167719.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "KeepTruckin - Embedded Software Engineer for Test",
                    "og:url": "https://jobs.lever.co/keeptruckin/89287bd6-3beb-4c1a-b028-b0f62a58cf66",
                    "twitter:description": "KeepTruckin is on a mission to improve the efficiency of America\u2019s trucking industry by connecting the millions of drivers and vehicles that haul freight on our roads. We are backed by Google Ventures and Index Ventures. In 2015, the U.S. Department of Transportation announced regulation that will require 4.5 million interstate truck drivers to use an Electronic Logging Device (ELD) to record their hours of service with the goal of improving road safety and reducing the paperwork burden on the industry. With the leading ELD in the market, KeepTruckin is poised to build the largest network of connected commercial vehicles in the world. The massive data generated from this network presents an opportunity to fundamentally change the way the trucking market operates. As an Embedded Software Engineer for Test, you have an amazing opportunity to shape the way we develop our products. We are looking for candidates with a strong S/W development background, with hands-on experience testing",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/929b350a-5ba5-4026-bb4f-0187a71d1371-1487288162889.png",
                    "twitter:title": "KeepTruckin - Embedded Software Engineer for Test",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Fluency in C / Python / C# / .NET / - including unit testing, data analysis / \nvisualization; Extreme attention to detail. Apply for this job \u00b7 KeepTruckin Home \nPage.",
        "title": "KeepTruckin - Embedded Software Engineer for Test"
    },
    {
        "cacheId": "sMptG80EgYoJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/eaze/b3f8d324-afb9-4e06-9ac8-24e1c1bb793a",
        "htmlFormattedUrl": "https://jobs.lever.co/eaze/b3f8d324-afb9-4e06-9ac8-24e1c1bb793a",
        "htmlSnippet": "Our core JSON API and many of our supporting tools are written in Javascript and <br>\n<b>C#</b>, so having experience with Node.js or .NET is a plus. Have no fear if you&#39;re&nbsp;...",
        "htmlTitle": "Eaze - Senior Back End Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/eaze/b3f8d324-afb9-4e06-9ac8-24e1c1bb793a",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/18605c7f-37a2-401c-8494-5e4dcf4e8a7a-1468272972279.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQB0iT3Ye9Q1tPBWuCZRGHc-KPvd0-TnFPMngDbDDOxjuhjen3wC3mQVss",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "The Role We\u2019re looking for an experienced engineer to join our team at Eaze. As a back end engineer, you\u2019ll help shape the platform that powers the Eaze web and mobile apps. We like to iterate quickly, so engineers are involved early in the product design process. Once we begin prototyping and moving towards release, you\u2019ll own and ship your own code on infrastructure you help automate and maintain. You\u2019ll be involved in each step of the process from design to deployment, including monitoring and scaling. What We\u2019re Looking For Our core JSON API and many of our supporting tools are written in Javascript and C#, so having experience with Node.js or .NET is a plus. Have no fear if you\u2019re not an expert in either of these\u2014we love engineers who can rapidly learn the right language or tool in order to solve the problem at hand. Some of our ongoing challenges include real-time driver tracking and routing, dynamic product suggestions and of course scaling our system to accommodate our exponen",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/18605c7f-37a2-401c-8494-5e4dcf4e8a7a-1468272972279.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Eaze - Senior Back End Engineer",
                    "og:url": "https://jobs.lever.co/eaze/b3f8d324-afb9-4e06-9ac8-24e1c1bb793a",
                    "twitter:description": "The Role We\u2019re looking for an experienced engineer to join our team at Eaze. As a back end engineer, you\u2019ll help shape the platform that powers the Eaze web and mobile apps. We like to iterate quickly, so engineers are involved early in the product design process. Once we begin prototyping and moving towards release, you\u2019ll own and ship your own code on infrastructure you help automate and maintain. You\u2019ll be involved in each step of the process from design to deployment, including monitoring and scaling. What We\u2019re Looking For Our core JSON API and many of our supporting tools are written in Javascript and C#, so having experience with Node.js or .NET is a plus. Have no fear if you\u2019re not an expert in either of these\u2014we love engineers who can rapidly learn the right language or tool in order to solve the problem at hand. Some of our ongoing challenges include real-time driver tracking and routing, dynamic product suggestions and of course scaling our system to accommodate our exponen",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/18605c7f-37a2-401c-8494-5e4dcf4e8a7a-1469486151221.png",
                    "twitter:title": "Eaze - Senior Back End Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Our core JSON API and many of our supporting tools are written in Javascript and \nC#, so having experience with Node.js or .NET is a plus. Have no fear if you're\u00a0...",
        "title": "Eaze - Senior Back End Engineer"
    },
    {
        "cacheId": "2mtXI6UWLIMJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../c72ce9ba-8847-41c1-85e9-624c63419886",
        "htmlFormattedUrl": "https://jobs.lever.co/.../c72ce9ba-8847-41c1-85e9-624c63419886",
        "htmlSnippet": "Our R&amp;D team works with the latest technologies to create our innovative <br>\nplatform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, <b>C#</b>, Scala, <br>\nInternet&nbsp;...",
        "htmlTitle": "Mendix - Test Engineer - Cloud Systems",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/mendix/c72ce9ba-8847-41c1-85e9-624c63419886",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "125",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRnynl1eHE8prhfLNU0wZgSen53PbGkIcLcCtJDIaiOQs8dfDzqLHcxsZY",
                    "width": "402"
                }
            ],
            "metatags": [
                {
                    "og:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you. The Cloud Systems Team builds, operates, and expands the Mendix Cloud. The Mendi",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Mendix - Test Engineer - Cloud Systems",
                    "og:url": "https://jobs.lever.co/mendix/c72ce9ba-8847-41c1-85e9-624c63419886",
                    "twitter:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you. The Cloud Systems Team builds, operates, and expands the Mendix Cloud. The Mendi",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644141599.png",
                    "twitter:title": "Mendix - Test Engineer - Cloud Systems",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Our R&D team works with the latest technologies to create our innovative \nplatform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, \nInternet\u00a0...",
        "title": "Mendix - Test Engineer - Cloud Systems"
    },
    {
        "cacheId": "0zg_BzVJGkkJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../d29d95fa-fb02-4e9f-bfbb-b32633f7057c",
        "htmlFormattedUrl": "https://jobs.lever.co/.../d29d95fa-fb02-4e9f-bfbb-b32633f7057c",
        "htmlSnippet": "Our R&amp;D team works with the latest technologies to create our innovative <br>\nplatform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, <b>C#</b>, Scala, <br>\nInternet&nbsp;...",
        "htmlTitle": "Mendix - Test Engineer - Cloud Integration",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/mendix/d29d95fa-fb02-4e9f-bfbb-b32633f7057c",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "125",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRnynl1eHE8prhfLNU0wZgSen53PbGkIcLcCtJDIaiOQs8dfDzqLHcxsZY",
                    "width": "402"
                }
            ],
            "metatags": [
                {
                    "og:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Mendix - Test Engineer - Cloud Integration",
                    "og:url": "https://jobs.lever.co/mendix/d29d95fa-fb02-4e9f-bfbb-b32633f7057c",
                    "twitter:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644141599.png",
                    "twitter:title": "Mendix - Test Engineer - Cloud Integration",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Our R&D team works with the latest technologies to create our innovative \nplatform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, \nInternet\u00a0...",
        "title": "Mendix - Test Engineer - Cloud Integration"
    },
    {
        "cacheId": "9CFWKxKeOQQJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../6d52bf6b-4534-480d-995a-f09d73fe4856",
        "htmlFormattedUrl": "https://jobs.lever.co/.../6d52bf6b-4534-480d-995a-f09d73fe4856",
        "htmlSnippet": "Our R&amp;D team works with the latest technologies to create our innovative <br>\nplatform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, <b>C#</b>, Scala, <br>\nInternet&nbsp;...",
        "htmlTitle": "Mendix - Smart Apps Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/mendix/6d52bf6b-4534-480d-995a-f09d73fe4856",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "125",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRnynl1eHE8prhfLNU0wZgSen53PbGkIcLcCtJDIaiOQs8dfDzqLHcxsZY",
                    "width": "402"
                }
            ],
            "metatags": [
                {
                    "og:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you. On this new R&D team, you will focus on enabling our end-users to deliver next g",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644155427.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Mendix - Smart Apps Developer",
                    "og:url": "https://jobs.lever.co/mendix/6d52bf6b-4534-480d-995a-f09d73fe4856",
                    "twitter:description": "Mendix is a visual, model-based IDE to create mobile & web apps. On top of this, our platform supports cloud deployment, feedback & collaboration and reusable components via our app store. As a result, Mendix is the fastest and easiest way to create and continuously improve mobile and web apps at scale. Our R&D team works with the latest technologies to create our innovative platform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, Internet of Things, Machine Learning, etc. And because more than 40,000 developers from 4,000 organizations around the world rely on Mendix, each commit has the potential to impact not just them but millions of end users. We're investing to accelerate our momentum and we're looking to grow our global team. If you constantly strive for excellence, are passionate about innovation, and want to work with a collaborative, energetic team - then Mendix is for you. On this new R&D team, you will focus on enabling our end-users to deliver next g",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/f71dba67-640a-45a3-b8d3-ab8fdfc7e38a-1495644141599.png",
                    "twitter:title": "Mendix - Smart Apps Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Our R&D team works with the latest technologies to create our innovative \nplatform \u2014 React, Node.js, TypeScript, Cloudfoundry/Pivotal/AWS, C#, Scala, \nInternet\u00a0...",
        "title": "Mendix - Smart Apps Developer"
    },
    {
        "cacheId": "rSAuZxdMQn0J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../8bf0f9b8-ddd8-422c-b698-ff304cee87d8",
        "htmlFormattedUrl": "https://jobs.lever.co/.../8bf0f9b8-ddd8-422c-b698-ff304cee87d8",
        "htmlSnippet": "... performance; Experience transforming requirements into unit and system level <br>\ntests; Experience with continuous integration tools; C++, Python, <b>C#</b> experience&nbsp;...",
        "htmlTitle": "Luminar - Software Test Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/luminartech/8bf0f9b8-ddd8-422c-b698-ff304cee87d8",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/18db9738-16b4-4c76-b845-07b16b5cfa21-1499986304249.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "89",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSFvf6FeCSFHt31BBS3B_ZWXQoYUt_5mNAAv__XU_Fd4rLXnz05WEurVA",
                    "width": "568"
                }
            ],
            "metatags": [
                {
                    "og:description": "Our vision is to power every autonomous vehicle with the first LiDAR capable of making them both safe and scalable. It\u2019s easy to get an autonomous vehicle to work 99% of the time, but it\u2019s the last 1% that\u2019s preventing them from becoming a reality. That\u2019s where we come in. We\u2019ve built a breakthrough LiDAR from the chip level up, delivering 50x better resolution and 10x longer range than the most advanced LiDARs available today. Luminar is not just a sensor, but the core of a platform that can enable the industry to have safe autonomous vehicles on the road. We are a diverse team of passionate and driven individuals, making us a powerhouse of innovation, design, engineering, and manufacturing. We are hiring the best and the brightest to accelerate the industry, and bring forward the next transportation revolution. OPPORTUNITY Luminar Technologies, Inc. is currently seeking applicants for a Software Test Engineer in Orlando, FL Position Overview: A software test engineer will assist",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/18db9738-16b4-4c76-b845-07b16b5cfa21-1499986304249.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Luminar - Software Test Engineer",
                    "og:url": "https://jobs.lever.co/luminartech/8bf0f9b8-ddd8-422c-b698-ff304cee87d8",
                    "twitter:description": "Our vision is to power every autonomous vehicle with the first LiDAR capable of making them both safe and scalable. It\u2019s easy to get an autonomous vehicle to work 99% of the time, but it\u2019s the last 1% that\u2019s preventing them from becoming a reality. That\u2019s where we come in. We\u2019ve built a breakthrough LiDAR from the chip level up, delivering 50x better resolution and 10x longer range than the most advanced LiDARs available today. Luminar is not just a sensor, but the core of a platform that can enable the industry to have safe autonomous vehicles on the road. We are a diverse team of passionate and driven individuals, making us a powerhouse of innovation, design, engineering, and manufacturing. We are hiring the best and the brightest to accelerate the industry, and bring forward the next transportation revolution. OPPORTUNITY Luminar Technologies, Inc. is currently seeking applicants for a Software Test Engineer in Orlando, FL Position Overview: A software test engineer will assist",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/18db9738-16b4-4c76-b845-07b16b5cfa21-1499973943868.png",
                    "twitter:title": "Luminar - Software Test Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... performance; Experience transforming requirements into unit and system level \ntests; Experience with continuous integration tools; C++, Python, C# experience\u00a0...",
        "title": "Luminar - Software Test Engineer"
    },
    {
        "cacheId": "HVJH90pIg7oJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../4a174760-8c1a-4878-b348-900c56ed5f69",
        "htmlFormattedUrl": "https://jobs.lever.co/.../4a174760-8c1a-4878-b348-900c56ed5f69",
        "htmlSnippet": "Deep knowledge and proficiency in C++ with other languages such as <b>C#</b> and <br>\npython being a plus; Fundamental understanding of data structures, design&nbsp;...",
        "htmlTitle": "Luminar - Sr. Software Engineer, LIDAR",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/luminartech/4a174760-8c1a-4878-b348-900c56ed5f69",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/18db9738-16b4-4c76-b845-07b16b5cfa21-1499986304249.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "89",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSFvf6FeCSFHt31BBS3B_ZWXQoYUt_5mNAAv__XU_Fd4rLXnz05WEurVA",
                    "width": "568"
                }
            ],
            "metatags": [
                {
                    "og:description": "Our vision is to power every autonomous vehicle with the first LiDAR capable of making them both safe and scalable. It\u2019s easy to get an autonomous vehicle to work 99% of the time, but it\u2019s the last 1% that\u2019s preventing them from becoming a reality. That\u2019s where we come in. We\u2019ve built a breakthrough LiDAR from the chip level up, delivering 50x better resolution and 10x longer range than the most advanced LiDARs available today. Luminar is not just a sensor, but the core of a platform that can enable the industry to have safe autonomous vehicles on the road. We are a diverse team of passionate and driven individuals, making us a powerhouse of innovation, design, engineering, and manufacturing. We are hiring the best and the brightest to accelerate the industry, and bring forward the next transportation revolution. OPPORTUNITY Luminar Technologies, Inc. is currently seeking applicants for Sr. Software Engineer, LIDAR in Orlando, FL JOB DESCRIPTION A Sr. Senior Software Engineer (LIDAR",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/18db9738-16b4-4c76-b845-07b16b5cfa21-1499986304249.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Luminar - Sr. Software Engineer, LIDAR",
                    "og:url": "https://jobs.lever.co/luminartech/4a174760-8c1a-4878-b348-900c56ed5f69",
                    "twitter:description": "Our vision is to power every autonomous vehicle with the first LiDAR capable of making them both safe and scalable. It\u2019s easy to get an autonomous vehicle to work 99% of the time, but it\u2019s the last 1% that\u2019s preventing them from becoming a reality. That\u2019s where we come in. We\u2019ve built a breakthrough LiDAR from the chip level up, delivering 50x better resolution and 10x longer range than the most advanced LiDARs available today. Luminar is not just a sensor, but the core of a platform that can enable the industry to have safe autonomous vehicles on the road. We are a diverse team of passionate and driven individuals, making us a powerhouse of innovation, design, engineering, and manufacturing. We are hiring the best and the brightest to accelerate the industry, and bring forward the next transportation revolution. OPPORTUNITY Luminar Technologies, Inc. is currently seeking applicants for Sr. Software Engineer, LIDAR in Orlando, FL JOB DESCRIPTION A Sr. Senior Software Engineer (LIDAR",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/18db9738-16b4-4c76-b845-07b16b5cfa21-1499973943868.png",
                    "twitter:title": "Luminar - Sr. Software Engineer, LIDAR",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Deep knowledge and proficiency in C++ with other languages such as C# and \npython being a plus; Fundamental understanding of data structures, design\u00a0...",
        "title": "Luminar - Sr. Software Engineer, LIDAR"
    },
    {
        "cacheId": "OGwitkq6ZT4J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../3c8f7cb0-7f83-48fe-8ac2-ea12f2984eca",
        "htmlFormattedUrl": "https://jobs.lever.co/.../3c8f7cb0-7f83-48fe-8ac2-ea12f2984eca",
        "htmlSnippet": "... Engineering or Mathematics or comparable experience; Ability to develop <br>\nsoftware in <b>C#</b>, AngularJS, or other selected languages; Familiarity with AWS, <br>\nASP.",
        "htmlTitle": "Moxe Health - Software Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/moxehealth/3c8f7cb0-7f83-48fe-8ac2-ea12f2984eca",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/1ad77f65-1b38-4d56-a2f9-6e5016f69ae9-1497536867587.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "124",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs7czl9nZGl3ATDn8eNyceldioGp5PpWcNTsTLqRZZcaSDi05_WqGMZbI",
                    "width": "406"
                }
            ],
            "metatags": [
                {
                    "og:description": "Moxe is seeking Software Engineers who will work with product, implementation and business development teams on the design, development and installation of software solutions. The engineering team builds high-quality, innovative and fully-performing software in compliance with coding standards and technical design. At this time we are seeking applicants for Junior and Senior-level as well as Testing Engineers.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/1ad77f65-1b38-4d56-a2f9-6e5016f69ae9-1497536867587.png",
                    "og:image:height": "200",
                    "og:title": "Moxe Health - Software Engineer",
                    "og:url": "https://jobs.lever.co/moxehealth/3c8f7cb0-7f83-48fe-8ac2-ea12f2984eca",
                    "twitter:description": "Moxe is seeking Software Engineers who will work with product, implementation and business development teams on the design, development and installation of software solutions. The engineering team builds high-quality, innovative and fully-performing software in compliance with coding standards and technical design. At this time we are seeking applicants for Junior and Senior-level as well as Testing Engineers.",
                    "twitter:title": "Moxe Health - Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... Engineering or Mathematics or comparable experience; Ability to develop \nsoftware in C#, AngularJS, or other selected languages; Familiarity with AWS, \nASP.",
        "title": "Moxe Health - Software Engineer"
    },
    {
        "cacheId": "-dvzuUJDIFcJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../83e478fe-1f2e-43d7-898d-d01f32da9cfd",
        "htmlFormattedUrl": "https://jobs.lever.co/.../83e478fe-1f2e-43d7-898d-d01f32da9cfd",
        "htmlSnippet": "4+ years of professional experience using the following programming languages/<br>\ntechnologies: <b>C#</b> &amp; .NET MVC. JavaScript. HTML5 &amp; CSS3. T-SQL. Experience&nbsp;...",
        "htmlTitle": "OfferPad - Full Stack Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/offerpad/83e478fe-1f2e-43d7-898d-d01f32da9cfd",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/3dfbed2f-b80e-461a-91fa-324dd0353688-1489448079911.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "91",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRoK86kTiARBwQ36gRrsPi0PKyuf9QsWgzSaop0nRoplII-8JJRfQ0c",
                    "width": "551"
                }
            ],
            "metatags": [
                {
                    "og:description": "WHO WE ARE: We are OfferPad and we\u2019re on a mission to dominate the market of online home sales, serving over 5000 homeowners per month. WHO YOU ARE: Smart, get things done Passionate about developing web applications using the latest technologies Open minded and always learning DAY IN THE LIFE: Building and maintaining our internal home buying platform and customer facing websites, which are built on the latest technologies, obviously. Streamlining our business processes through automation and integration with external applications through web services, RESTful APIs and other technologies. Enhancing the platform\u2019s business intelligence engine to help optimize the return on our investments. Contributing to our suite of front & back-end automated tests scripts. Working closely with the Marketing & Business Teams to implement new features. And more\u2026 like we said, the company is expanding rapidly, and things are constantly evolving. WHAT YOU HAVE: Minimum Technical Qualifications\u00a0\u2013 we will ask you to dem",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/3dfbed2f-b80e-461a-91fa-324dd0353688-1489448079911.png",
                    "og:image:height": "200",
                    "og:title": "OfferPad - Full Stack Developer",
                    "og:url": "https://jobs.lever.co/offerpad/83e478fe-1f2e-43d7-898d-d01f32da9cfd",
                    "twitter:description": "WHO WE ARE: We are OfferPad and we\u2019re on a mission to dominate the market of online home sales, serving over 5000 homeowners per month. WHO YOU ARE: Smart, get things done Passionate about developing web applications using the latest technologies Open minded and always learning DAY IN THE LIFE: Building and maintaining our internal home buying platform and customer facing websites, which are built on the latest technologies, obviously. Streamlining our business processes through automation and integration with external applications through web services, RESTful APIs and other technologies. Enhancing the platform\u2019s business intelligence engine to help optimize the return on our investments. Contributing to our suite of front & back-end automated tests scripts. Working closely with the Marketing & Business Teams to implement new features. And more\u2026 like we said, the company is expanding rapidly, and things are constantly evolving. WHAT YOU HAVE: Minimum Technical Qualifications\u00a0\u2013 we will ask you to dem",
                    "twitter:title": "OfferPad - Full Stack Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "4+ years of professional experience using the following programming languages/\ntechnologies: C# & .NET MVC. JavaScript. HTML5 & CSS3. T-SQL. Experience\u00a0...",
        "title": "OfferPad - Full Stack Developer"
    },
    {
        "cacheId": "w4yNozoXwpYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/tunein/abfd6ed0-89fc-4b57-a4a9-921fe6e9574f",
        "htmlFormattedUrl": "https://jobs.lever.co/tunein/abfd6ed0-89fc-4b57-a4a9-921fe6e9574f",
        "htmlSnippet": "NET/<b>C#</b> preferred). History of building resilient, stateless, scalable, distributed <br>\nand observable systems. Experience with microservices, knowledge of modern&nbsp;...",
        "htmlTitle": "TuneIn - Staff Software Engineer, Core Platform",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/tunein/abfd6ed0-89fc-4b57-a4a9-921fe6e9574f",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/f3dcdf54-1d41-48ca-85d2-41c987f4df11-1498158700270.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "123",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQ1_N6VX8ABEgMmVitw5JO6vPRDL10pG2kAlrrH6C7MJ1I2FVfq1Bja22w",
                    "width": "408"
                }
            ],
            "metatags": [
                {
                    "og:description": "Staff Software Engineer, Core Platform Our mission is to deliver the world\u2019s best listening experiences. Every day we make good on that promise for millions of listeners through our flagship mobile and web applications along with more than 200 connected devices and services. About TuneIn Engineering We value being a top-notch engineering organization, and have the same high standards with our code and people. We make time for quality, we are agile and pragmatic, we keep it simple, we are data driven, and we love getting better. Check out our principals here: https://github.com/tunein/engineering/blob/master/Principles.md We regularly invest time in your future and support growth, and we show this in a number of ways\u2014clear job responsibilities and expectations for your career path, freedom to move teams, Mission Teams to contribute more broadly, and our quarterly Discovery Days, whereby you spend time in the form of building innovative features, products, or approaches to prob",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/f3dcdf54-1d41-48ca-85d2-41c987f4df11-1498158700270.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "TuneIn - Staff Software Engineer, Core Platform",
                    "og:url": "https://jobs.lever.co/tunein/abfd6ed0-89fc-4b57-a4a9-921fe6e9574f",
                    "twitter:description": "Staff Software Engineer, Core Platform Our mission is to deliver the world\u2019s best listening experiences. Every day we make good on that promise for millions of listeners through our flagship mobile and web applications along with more than 200 connected devices and services. About TuneIn Engineering We value being a top-notch engineering organization, and have the same high standards with our code and people. We make time for quality, we are agile and pragmatic, we keep it simple, we are data driven, and we love getting better. Check out our principals here: https://github.com/tunein/engineering/blob/master/Principles.md We regularly invest time in your future and support growth, and we show this in a number of ways\u2014clear job responsibilities and expectations for your career path, freedom to move teams, Mission Teams to contribute more broadly, and our quarterly Discovery Days, whereby you spend time in the form of building innovative features, products, or approaches to prob",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/f3dcdf54-1d41-48ca-85d2-41c987f4df11-1498158677995.png",
                    "twitter:title": "TuneIn - Staff Software Engineer, Core Platform",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "NET/C# preferred). History of building resilient, stateless, scalable, distributed \nand observable systems. Experience with microservices, knowledge of modern\u00a0...",
        "title": "TuneIn - Staff Software Engineer, Core Platform"
    },
    {
        "cacheId": "yb2f3-depvUJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../36e45a6b-72cf-4053-bd1d-c6f8169da5d5",
        "htmlFormattedUrl": "https://jobs.lever.co/.../36e45a6b-72cf-4053-bd1d-c6f8169da5d5",
        "htmlSnippet": "... Familiarity with React, Redux, Typescript and Node are a strong plus; Some <br>\nfamiliarity with a statically typed server-side language like Java, C++, <b>C#</b> etc is a<br>\n&nbsp;...",
        "htmlTitle": "knewton.com - Senior Software Engineer - Teach",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/knewton/36e45a6b-72cf-4053-bd1d-c6f8169da5d5",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/c1843acd-33bd-46c0-b86c-d84ae3adf84a-1458765198883.jpg"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "100",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3wXEbs1uvqQr4SsGZEnmp8KR2M4hKAV94oCHG4ojaO-1VkIEeOobP6g8",
                    "width": "350"
                }
            ],
            "metatags": [
                {
                    "og:description": "Knewton is on a mission to personalize education for students around the world. Education companies worldwide use the Knewton infrastructure platform to power course materials that dynamically adapt to each student\u2019s unique needs. You will be responsible for developing the product that our teachers use to administer and assess courses for their students. You will work on both setting direction and executing on the design of our product and our system. Your first big goal will be to make our system more resilient to failure as we drastically scale the number of users we have. You will work closely with our Product, UX and Data Science teams to develop features that you are passionate about, and that are performant and easy-to-maintain.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/c1843acd-33bd-46c0-b86c-d84ae3adf84a-1458765198883.jpg",
                    "og:image:height": "200",
                    "og:title": "knewton.com - Senior Software Engineer - Teach",
                    "og:url": "https://jobs.lever.co/knewton/36e45a6b-72cf-4053-bd1d-c6f8169da5d5",
                    "twitter:description": "Knewton is on a mission to personalize education for students around the world. Education companies worldwide use the Knewton infrastructure platform to power course materials that dynamically adapt to each student\u2019s unique needs. You will be responsible for developing the product that our teachers use to administer and assess courses for their students. You will work on both setting direction and executing on the design of our product and our system. Your first big goal will be to make our system more resilient to failure as we drastically scale the number of users we have. You will work closely with our Product, UX and Data Science teams to develop features that you are passionate about, and that are performant and easy-to-maintain.",
                    "twitter:title": "knewton.com - Senior Software Engineer - Teach",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... Familiarity with React, Redux, Typescript and Node are a strong plus; Some \nfamiliarity with a statically typed server-side language like Java, C++, C# etc is a\n\u00a0...",
        "title": "knewton.com - Senior Software Engineer - Teach"
    },
    {
        "cacheId": "2xjLsNtU3LUJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../3310737f-0a46-4729-be80-890032ca59c4",
        "htmlFormattedUrl": "https://jobs.lever.co/.../3310737f-0a46-4729-be80-890032ca59c4",
        "htmlSnippet": "... 5-8 years of experience in software development or engineering; 2 or more <br>\nyears of experience managing software developers, preferably working in a <b>C#</b> <br>\nor&nbsp;...",
        "htmlTitle": "BoomTown - Manager, Software Engineering (.Net)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/boomtownroi.com/3310737f-0a46-4729-be80-890032ca59c4",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/035d99be-98af-422a-aeb3-25d8c844018f-1468443033584.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRriALjfc-FHmorRLrF57SqKQ3DE7rrCgRuPs-6mpHIG6wQNoofhrq3Fcg",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "With more than 70 million unique users and half a billion monthly page views, our platform is one of the biggest social websites in real estate! With cutting edge work in social, big data, web and mobile apps - we offer a playground for technologists! We are looking for someone to lead our team of highly-talented software engineers that is self-directed, innovative and driven to release code rapidly and independently. We are not just focused on what we deliver but how we deliver it, and view our engineering capability as a core business differentiator.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/035d99be-98af-422a-aeb3-25d8c844018f-1468443033584.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "BoomTown - Manager, Software Engineering (.Net)",
                    "og:url": "https://jobs.lever.co/boomtownroi.com/3310737f-0a46-4729-be80-890032ca59c4",
                    "twitter:description": "With more than 70 million unique users and half a billion monthly page views, our platform is one of the biggest social websites in real estate! With cutting edge work in social, big data, web and mobile apps - we offer a playground for technologists! We are looking for someone to lead our team of highly-talented software engineers that is self-directed, innovative and driven to release code rapidly and independently. We are not just focused on what we deliver but how we deliver it, and view our engineering capability as a core business differentiator.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/035d99be-98af-422a-aeb3-25d8c844018f-1468443025221.png",
                    "twitter:title": "BoomTown - Manager, Software Engineering (.Net)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... 5-8 years of experience in software development or engineering; 2 or more \nyears of experience managing software developers, preferably working in a C# \nor\u00a0...",
        "title": "BoomTown - Manager, Software Engineering (.Net)"
    },
    {
        "cacheId": "ygh8VhqFH4oJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../87d9722e-ef97-4f01-a797-7341a94c5d23",
        "htmlFormattedUrl": "https://jobs.lever.co/.../87d9722e-ef97-4f01-a797-7341a94c5d23",
        "htmlSnippet": "o Ma\u00eetrise du langage C++ / STL / multi-threading;. o Ma\u00eetrise du langage <b>C#</b> et <br>\nlibrairie .net;. o Ma\u00eetrise des outils de gestion de code collaboratif (Subversion).",
        "htmlTitle": "Moment Factory - D\u00e9veloppeur d&#39;applications Multim\u00e9dia ...",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/momentfactory/87d9722e-ef97-4f01-a797-7341a94c5d23",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/MomentFactory_logo.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "164",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSZKzHKSkL7YDwo01wU1Tho3W4WE8FQL3CzSqtGEVPOkaTANCXHd4lvAeNy",
                    "width": "307"
                }
            ],
            "metatags": [
                {
                    "og:description": "English version below Le d\u00e9veloppeur d'application multim\u00e9dia applique ses connaissances en informatique et infographie 3D pour le d\u00e9veloppement d'applications ou de plugins 3D temps-r\u00e9el. Il est \u00e9galement amen\u00e9 \u00e0 utiliser et int\u00e9grer diverses plateformes logicielles et mat\u00e9rielles externes au sein d'un syst\u00e8me plus complexe. Il fait partie d\u2019une \u00e9quipe de d\u00e9veloppeurs d\u00e9di\u00e9e au d\u00e9veloppement de notre logiciel propri\u00e9taire X-Agora et doit \u00eatre un support technique \u00e0 l\u2019\u00e9quipe de d\u00e9veloppement. Il est \u00e9galement appel\u00e9 \u00e0 travailler sur certains projets clients utilisant les solutions issues de l\u2019\u00e9quipe d\u00e9veloppement. Il doit se tenir au courant des derni\u00e8res technologies, et avoir un bon esprit d'analyse et de recherche afin d'appliquer ses nouvelles connaissances au domaine du multim\u00e9dia. Son activit\u00e9 inclut \u00e9galement une participation et un suivi \u00e9crit de ses travaux de recherche scientifique appliqu\u00e9e, que ce soit un nouveau module li\u00e9 \u00e0 X-Agora ou tout autre projet de r",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/MomentFactory_logo.png",
                    "og:image:height": "200",
                    "og:title": "Moment Factory - D\u00e9veloppeur d'applications Multim\u00e9dia (Multimedia application developer)",
                    "og:url": "https://jobs.lever.co/momentfactory/87d9722e-ef97-4f01-a797-7341a94c5d23",
                    "twitter:description": "English version below Le d\u00e9veloppeur d'application multim\u00e9dia applique ses connaissances en informatique et infographie 3D pour le d\u00e9veloppement d'applications ou de plugins 3D temps-r\u00e9el. Il est \u00e9galement amen\u00e9 \u00e0 utiliser et int\u00e9grer diverses plateformes logicielles et mat\u00e9rielles externes au sein d'un syst\u00e8me plus complexe. Il fait partie d\u2019une \u00e9quipe de d\u00e9veloppeurs d\u00e9di\u00e9e au d\u00e9veloppement de notre logiciel propri\u00e9taire X-Agora et doit \u00eatre un support technique \u00e0 l\u2019\u00e9quipe de d\u00e9veloppement. Il est \u00e9galement appel\u00e9 \u00e0 travailler sur certains projets clients utilisant les solutions issues de l\u2019\u00e9quipe d\u00e9veloppement. Il doit se tenir au courant des derni\u00e8res technologies, et avoir un bon esprit d'analyse et de recherche afin d'appliquer ses nouvelles connaissances au domaine du multim\u00e9dia. Son activit\u00e9 inclut \u00e9galement une participation et un suivi \u00e9crit de ses travaux de recherche scientifique appliqu\u00e9e, que ce soit un nouveau module li\u00e9 \u00e0 X-Agora ou tout autre projet de r",
                    "twitter:title": "Moment Factory - D\u00e9veloppeur d'applications Multim\u00e9dia (Multimedia application developer)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "o Ma\u00eetrise du langage C++ / STL / multi-threading;. o Ma\u00eetrise du langage C# et \nlibrairie .net;. o Ma\u00eetrise des outils de gestion de code collaboratif (Subversion).",
        "title": "Moment Factory - D\u00e9veloppeur d'applications Multim\u00e9dia ..."
    },
    {
        "cacheId": "vsPDlrDr56wJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/eaze/b98a0286-6dfa-45f6-9212-826b532c3a00",
        "htmlFormattedUrl": "https://jobs.lever.co/eaze/b98a0286-6dfa-45f6-9212-826b532c3a00",
        "htmlSnippet": "Our platform runs on both Node.js and <b>C#</b> .NET, so experience with both unix <br>\nand windows is preferred, but not required. A Little About Us. We have a friendly,<br>\n&nbsp;...",
        "htmlTitle": "Eaze - DevOps Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/eaze/b98a0286-6dfa-45f6-9212-826b532c3a00",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/18605c7f-37a2-401c-8494-5e4dcf4e8a7a-1468272972279.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQB0iT3Ye9Q1tPBWuCZRGHc-KPvd0-TnFPMngDbDDOxjuhjen3wC3mQVss",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "The Role We\u2019re looking for an experienced DevOps Engineer to join our team at Eaze. As a DevOps Engineer, you\u2019ll help run and shape the infrastructure that our platform runs on. You\u2019ll use tools like Chef, Cloudformation, and everything AWS to automate, monitor, and build our infrastructure. We like to iterate quickly, so DevOps is included early and often in the product planning process. You\u2019ll work closely with our application engineers to help them ship reliable, high quality products. You and your team mates will be responsible for all of the infrastructure that runs our business. What We\u2019re Looking For Our infrastructure runs in AWS and uses many of the services that it provides. Our ideal candidate has extensive experience setting up automation, monitoring, alerting, and logging systems in the AWS cloud. Our platform runs on both Node.js and C# .NET, so experience with both unix and windows is preferred, but not required. A Little About Us We have a friendly, welcoming environm",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/18605c7f-37a2-401c-8494-5e4dcf4e8a7a-1468272972279.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Eaze - DevOps Engineer",
                    "og:url": "https://jobs.lever.co/eaze/b98a0286-6dfa-45f6-9212-826b532c3a00",
                    "twitter:description": "The Role We\u2019re looking for an experienced DevOps Engineer to join our team at Eaze. As a DevOps Engineer, you\u2019ll help run and shape the infrastructure that our platform runs on. You\u2019ll use tools like Chef, Cloudformation, and everything AWS to automate, monitor, and build our infrastructure. We like to iterate quickly, so DevOps is included early and often in the product planning process. You\u2019ll work closely with our application engineers to help them ship reliable, high quality products. You and your team mates will be responsible for all of the infrastructure that runs our business. What We\u2019re Looking For Our infrastructure runs in AWS and uses many of the services that it provides. Our ideal candidate has extensive experience setting up automation, monitoring, alerting, and logging systems in the AWS cloud. Our platform runs on both Node.js and C# .NET, so experience with both unix and windows is preferred, but not required. A Little About Us We have a friendly, welcoming environm",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/18605c7f-37a2-401c-8494-5e4dcf4e8a7a-1469486151221.png",
                    "twitter:title": "Eaze - DevOps Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Our platform runs on both Node.js and C# .NET, so experience with both unix \nand windows is preferred, but not required. A Little About Us. We have a friendly,\n\u00a0...",
        "title": "Eaze - DevOps Engineer"
    },
    {
        "cacheId": "0XnQZ5sjr44J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../cff593c4-632a-48aa-b3df-ea855792872f",
        "htmlFormattedUrl": "https://jobs.lever.co/.../cff593c4-632a-48aa-b3df-ea855792872f",
        "htmlSnippet": "... Engineering or Mathematics or comparable experience; Ability to develop <br>\nsoftware in <b>C#</b>, AngularJS, or other selected languages; Familiarity with AWS, <br>\nASP.",
        "htmlTitle": "Moxe Health - Cerner Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/moxehealth/cff593c4-632a-48aa-b3df-ea855792872f",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/1ad77f65-1b38-4d56-a2f9-6e5016f69ae9-1497536867587.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "124",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs7czl9nZGl3ATDn8eNyceldioGp5PpWcNTsTLqRZZcaSDi05_WqGMZbI",
                    "width": "406"
                }
            ],
            "metatags": [
                {
                    "og:description": "Moxe is seeking an experienced Cerner Engineer to lead software design and development related to integration work with Cerner's core applications. The engineering team builds high-quality, innovative and fully-performing software in compliance with coding standards and technical design.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/1ad77f65-1b38-4d56-a2f9-6e5016f69ae9-1497536867587.png",
                    "og:image:height": "200",
                    "og:title": "Moxe Health - Cerner Engineer",
                    "og:url": "https://jobs.lever.co/moxehealth/cff593c4-632a-48aa-b3df-ea855792872f",
                    "twitter:description": "Moxe is seeking an experienced Cerner Engineer to lead software design and development related to integration work with Cerner's core applications. The engineering team builds high-quality, innovative and fully-performing software in compliance with coding standards and technical design.",
                    "twitter:title": "Moxe Health - Cerner Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... Engineering or Mathematics or comparable experience; Ability to develop \nsoftware in C#, AngularJS, or other selected languages; Familiarity with AWS, \nASP.",
        "title": "Moxe Health - Cerner Engineer"
    },
    {
        "cacheId": "PQi5n6JRT3cJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../c4420b1b-36fc-4b93-9b8a-72e62484ed4f",
        "htmlFormattedUrl": "https://jobs.lever.co/.../c4420b1b-36fc-4b93-9b8a-72e62484ed4f",
        "htmlSnippet": "8 years of overall software engineering or development experience and recent <br>\ncoding experience in Unity, <b>C#</b>, C++, UnReal and other VR/AR development&nbsp;...",
        "htmlTitle": "Meta - Developer Success Program Mgr IV",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/metavision/c4420b1b-36fc-4b93-9b8a-72e62484ed4f",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/b51e8ed9-a449-4fb6-9bac-61e429a760d9-1459466298336.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "112",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSlCzDRy5T4BqYnZJU-8LOgLKSihpkwF4JkzLRrVd2Ni6j4sHkHAk59ku8",
                    "width": "449"
                }
            ],
            "metatags": [
                {
                    "og:description": "As a member of the Meta Customer Success team, the Developer Success Program Manager will be instrumental in building the Developer Community for the Meta 2 product line. In addition to hosting developer workshops, you will build and grow the Developer Community online, create content, and training materials for the Meta 2 Developer Community. - Work with Enterprise and Independent Developers on projects for their business and or Meta solutions. - Working to define and improve the way Meta engages with the Developer Community. - Work with the Developer Community to create demo applications, collateral and training documentation. - Create and deliver hands-on workshops, presentations, blog/media posts, and subsequent resources that others in the developer community can use to increase awareness and adoption of the Meta 2 platform. - Build excitement amongst the Developer Community, and encourage participation in the development of applicatio",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/b51e8ed9-a449-4fb6-9bac-61e429a760d9-1459466298336.png",
                    "og:image:height": "200",
                    "og:title": "Meta - Developer Success Program Mgr IV",
                    "og:url": "https://jobs.lever.co/metavision/c4420b1b-36fc-4b93-9b8a-72e62484ed4f",
                    "twitter:description": "As a member of the Meta Customer Success team, the Developer Success Program Manager will be instrumental in building the Developer Community for the Meta 2 product line. In addition to hosting developer workshops, you will build and grow the Developer Community online, create content, and training materials for the Meta 2 Developer Community. - Work with Enterprise and Independent Developers on projects for their business and or Meta solutions. - Working to define and improve the way Meta engages with the Developer Community. - Work with the Developer Community to create demo applications, collateral and training documentation. - Create and deliver hands-on workshops, presentations, blog/media posts, and subsequent resources that others in the developer community can use to increase awareness and adoption of the Meta 2 platform. - Build excitement amongst the Developer Community, and encourage participation in the development of applicatio",
                    "twitter:title": "Meta - Developer Success Program Mgr IV",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "8 years of overall software engineering or development experience and recent \ncoding experience in Unity, C#, C++, UnReal and other VR/AR development\u00a0...",
        "title": "Meta - Developer Success Program Mgr IV"
    },
    {
        "cacheId": "ZbAQCAe4nFwJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../5cdd9d5d-aa97-490b-888d-456f8a25b7d6",
        "htmlFormattedUrl": "https://jobs.lever.co/.../5cdd9d5d-aa97-490b-888d-456f8a25b7d6",
        "htmlSnippet": "... organized, and a team player. Highly Desired. Knowledge of web architecture <br>\nand the HTTP protocol; Some Java and/or objective-C/C++/<b>C#</b> knowledge&nbsp;...",
        "htmlTitle": "Rocket Lawyer - Software Engineer, Mobile (iOS/Android)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/rocketlawyer/5cdd9d5d-aa97-490b-888d-456f8a25b7d6",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/676d3de8-bf16-40f6-98be-f6e8fe5b9942-1498519152482.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "76",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbpSISh06Lx5xz_PiSYAL1PPs0dqZ_JX5t9fYnkesVeBmWgMzgxe_HEDY",
                    "width": "218"
                }
            ],
            "metatags": [
                {
                    "og:description": "About Rocket Lawyer We believe everyone deserves affordable and simple access to legal services. Rocket Lawyer is one of the largest and most widely used online legal service platforms in the world. Rocket Lawyer has helped over 20 million people create over 3 million legal documents, and answer over 30,000 legal questions. We are in a unique position to enhance and expand the Rocket Lawyer platform to a scale never seen before in the company\u2019s history, to capture audiences worldwide. We are expanding the engineering team to take on this challenge! About the Position We are looking for a passionate front-end engineer with mobile focus who wants to work in a fast-paced, dynamic environment with a talented agile team. As part of a team consisting of a product manager, UX designer, and software engineers and QA analysts, the mobile software engineer is an active partner in the design, coding, unit testing, and release of new features and enhancements for our growing customer base.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/676d3de8-bf16-40f6-98be-f6e8fe5b9942-1498519152482.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Rocket Lawyer - Software Engineer, Mobile (iOS/Android)",
                    "og:url": "https://jobs.lever.co/rocketlawyer/5cdd9d5d-aa97-490b-888d-456f8a25b7d6",
                    "twitter:description": "About Rocket Lawyer We believe everyone deserves affordable and simple access to legal services. Rocket Lawyer is one of the largest and most widely used online legal service platforms in the world. Rocket Lawyer has helped over 20 million people create over 3 million legal documents, and answer over 30,000 legal questions. We are in a unique position to enhance and expand the Rocket Lawyer platform to a scale never seen before in the company\u2019s history, to capture audiences worldwide. We are expanding the engineering team to take on this challenge! About the Position We are looking for a passionate front-end engineer with mobile focus who wants to work in a fast-paced, dynamic environment with a talented agile team. As part of a team consisting of a product manager, UX designer, and software engineers and QA analysts, the mobile software engineer is an active partner in the design, coding, unit testing, and release of new features and enhancements for our growing customer base.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/676d3de8-bf16-40f6-98be-f6e8fe5b9942-1469662672443.png",
                    "twitter:title": "Rocket Lawyer - Software Engineer, Mobile (iOS/Android)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... organized, and a team player. Highly Desired. Knowledge of web architecture \nand the HTTP protocol; Some Java and/or objective-C/C++/C# knowledge\u00a0...",
        "title": "Rocket Lawyer - Software Engineer, Mobile (iOS/Android)"
    },
    {
        "cacheId": "4SwNWTl5b2IJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../116d38c3-1168-4e3a-8f27-00e88de730ae",
        "htmlFormattedUrl": "https://jobs.lever.co/.../116d38c3-1168-4e3a-8f27-00e88de730ae",
        "htmlSnippet": "5+ years <b>C#</b> / ASP.NET [Windows or Linux]; 3+ years Microsoft SQL databases, <br>\nwith Distributed Workflow engines; 3+ years *Linux, ideally Mono; 3+ years node.",
        "htmlTitle": "Audible Magic - Senior Backend Software Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/audiblemagic/116d38c3-1168-4e3a-8f27-00e88de730ae",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/b86f76c7-02fe-4a12-9c90-68ab6e0f32a6-1463446031565.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "48",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRpZ5zAh2Ktpya9GsC3_D-grZ8MWRjA_ij9mWeBF3afurLFlyXUMgU6kQ",
                    "width": "208"
                }
            ],
            "metatags": [
                {
                    "og:description": "We are building one of the most revolutionary music recognition products, the global music industry is asking for; to do this we are looking for a Senior Software Engineer. The objectives are simple, but difficult to execute. As a senior member of the team, you will be expected to drive the requirements for and own large components of the system throughout their lifecycle: requirements, architecture/design, implementation, testing, and launch. You will need to exhibit strong leadership and communication skills, define and successfully execute on the engineering and release priorities in a very agile application development environment. Audible Magic's senior software engineers develop the next-generation technologies that change how music recognition is shared with millions of users , explore, and interact with global music industry. Our products need to handle information at large scale, and extend well beyond web applications. We're looking for engineers who bring fresh ideas from a",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/b86f76c7-02fe-4a12-9c90-68ab6e0f32a6-1463446031565.png",
                    "og:image:height": "200",
                    "og:title": "Audible Magic - Senior Backend Software Engineer",
                    "og:url": "https://jobs.lever.co/audiblemagic/116d38c3-1168-4e3a-8f27-00e88de730ae",
                    "twitter:description": "We are building one of the most revolutionary music recognition products, the global music industry is asking for; to do this we are looking for a Senior Software Engineer. The objectives are simple, but difficult to execute. As a senior member of the team, you will be expected to drive the requirements for and own large components of the system throughout their lifecycle: requirements, architecture/design, implementation, testing, and launch. You will need to exhibit strong leadership and communication skills, define and successfully execute on the engineering and release priorities in a very agile application development environment. Audible Magic's senior software engineers develop the next-generation technologies that change how music recognition is shared with millions of users , explore, and interact with global music industry. Our products need to handle information at large scale, and extend well beyond web applications. We're looking for engineers who bring fresh ideas from a",
                    "twitter:title": "Audible Magic - Senior Backend Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "5+ years C# / ASP.NET [Windows or Linux]; 3+ years Microsoft SQL databases, \nwith Distributed Workflow engines; 3+ years *Linux, ideally Mono; 3+ years node.",
        "title": "Audible Magic - Senior Backend Software Engineer"
    },
    {
        "cacheId": "LC6y4yfoFV8J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/brolly/3d5c78b5-f275-4aee-aa06-6c56d443218d",
        "htmlFormattedUrl": "https://jobs.lever.co/brolly/3d5c78b5-f275-4aee-aa06-6c56d443218d",
        "htmlSnippet": "A developer with all your heart; Very experienced with at least two of the <br>\nfollowing: JS, Java, ObjectiveC, Swift, Python, <b>C#</b>; Enthusiastic about <br>\ncollaborating in a&nbsp;...",
        "htmlTitle": "Brolly - Front-end developer (mobile)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/brolly/3d5c78b5-f275-4aee-aa06-6c56d443218d",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/59da2648-9f1b-47c4-9501-7db7cf57dbc7-1491566390262.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "225",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRmDTCyy-d7xSKiXzr1MVBkXXGxizbK1-p-4c2-NVsj0mYUv0DMHSN3LbbR",
                    "width": "225"
                }
            ],
            "metatags": [
                {
                    "og:description": "We are looking for a mobile app software engineer with experience building world-class mobile applications. The ideal candidate has a proven track record of building exceptional quality mobile apps or mobile-optimised websites, enjoys collaborating with a team, and is obsessed with building a consumer product that customers love.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/59da2648-9f1b-47c4-9501-7db7cf57dbc7-1491566390262.png",
                    "og:image:height": "200",
                    "og:title": "Brolly - Front-end developer (mobile)",
                    "og:url": "https://jobs.lever.co/brolly/3d5c78b5-f275-4aee-aa06-6c56d443218d",
                    "twitter:description": "We are looking for a mobile app software engineer with experience building world-class mobile applications. The ideal candidate has a proven track record of building exceptional quality mobile apps or mobile-optimised websites, enjoys collaborating with a team, and is obsessed with building a consumer product that customers love.",
                    "twitter:title": "Brolly - Front-end developer (mobile)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "A developer with all your heart; Very experienced with at least two of the \nfollowing: JS, Java, ObjectiveC, Swift, Python, C#; Enthusiastic about \ncollaborating in a\u00a0...",
        "title": "Brolly - Front-end developer (mobile)"
    },
    {
        "cacheId": "fK5TM7veTnUJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../12cd581a-6300-41e0-b472-bae44194d157",
        "htmlFormattedUrl": "https://jobs.lever.co/.../12cd581a-6300-41e0-b472-bae44194d157",
        "htmlSnippet": "NET, Java, <b>C#</b> or similar languages; Good command of written and spoken <br>\nEnglish; Strong communication skills and a good team player; Strong sense of&nbsp;...",
        "htmlTitle": "Trendyol - Tech Talent Program - Intern",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/trendyol/12cd581a-6300-41e0-b472-bae44194d157",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/a81a734c-54a8-4378-85ba-2eee13010fb6-1502976769600.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQxncxuxq-iTpXIwKjDQLyYxA_by4qvx_tXZvVABZCwZ4pVC1k5J4UOt9pN",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "Join the region\u2019s fastest growing technology company and largest fashion e-tailer in this exciting opportunity! Trendyol.com is the largest fashion e-commerce company in Turkey and the MENA region selling more than 25 million fashion items per year. Trendyol's mission is to make fashion accessible and serves over 12 million customers, has 50 million monthly visits and is the fastest growing e-commerce company in the region. Founded in 2010, Trendyol is the biggest internet employer in Turkey with a team of ca. 1200 people. Investors include Kleiner Perkins, Tiger Global and EBRD. We are looking for passionate Tech Talents who is enthusiastic to play a key role in helping Trendyol provide the best experience to millions of customers! You should be energetic and flexible because we want you to adapt to our dynamic and lively environment!",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/a81a734c-54a8-4378-85ba-2eee13010fb6-1502976769600.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Trendyol - Tech Talent Program - Intern",
                    "og:url": "https://jobs.lever.co/trendyol/12cd581a-6300-41e0-b472-bae44194d157",
                    "twitter:description": "Join the region\u2019s fastest growing technology company and largest fashion e-tailer in this exciting opportunity! Trendyol.com is the largest fashion e-commerce company in Turkey and the MENA region selling more than 25 million fashion items per year. Trendyol's mission is to make fashion accessible and serves over 12 million customers, has 50 million monthly visits and is the fastest growing e-commerce company in the region. Founded in 2010, Trendyol is the biggest internet employer in Turkey with a team of ca. 1200 people. Investors include Kleiner Perkins, Tiger Global and EBRD. We are looking for passionate Tech Talents who is enthusiastic to play a key role in helping Trendyol provide the best experience to millions of customers! You should be energetic and flexible because we want you to adapt to our dynamic and lively environment!",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/a81a734c-54a8-4378-85ba-2eee13010fb6-1502963363823.png",
                    "twitter:title": "Trendyol - Tech Talent Program - Intern",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "NET, Java, C# or similar languages; Good command of written and spoken \nEnglish; Strong communication skills and a good team player; Strong sense of\u00a0...",
        "title": "Trendyol - Tech Talent Program - Intern"
    },
    {
        "cacheId": "r6FzRqfD9tgJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../07c8e46f-d002-4e8f-8914-bb444aa92d65",
        "htmlFormattedUrl": "https://jobs.lever.co/.../07c8e46f-d002-4e8f-8914-bb444aa92d65",
        "htmlSnippet": "... Engineering or Mathematics or comparable experience; Ability to develop <br>\nsoftware in <b>C#</b>, AngularJS, or other selected languages; Familiarity with AWS, <br>\nASP.",
        "htmlTitle": "Moxe Health - Integration Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/moxehealth/07c8e46f-d002-4e8f-8914-bb444aa92d65",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/1ad77f65-1b38-4d56-a2f9-6e5016f69ae9-1497536867587.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "124",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs7czl9nZGl3ATDn8eNyceldioGp5PpWcNTsTLqRZZcaSDi05_WqGMZbI",
                    "width": "406"
                }
            ],
            "metatags": [
                {
                    "og:description": "Moxe is seeking experienced healthcare Integration Engineers to lead design and software development focused on healthcare data exchange. The engineering team builds high-quality, innovative and fully-performing software in compliance with coding standards and technical design.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/1ad77f65-1b38-4d56-a2f9-6e5016f69ae9-1497536867587.png",
                    "og:image:height": "200",
                    "og:title": "Moxe Health - Integration Engineer",
                    "og:url": "https://jobs.lever.co/moxehealth/07c8e46f-d002-4e8f-8914-bb444aa92d65",
                    "twitter:description": "Moxe is seeking experienced healthcare Integration Engineers to lead design and software development focused on healthcare data exchange. The engineering team builds high-quality, innovative and fully-performing software in compliance with coding standards and technical design.",
                    "twitter:title": "Moxe Health - Integration Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... Engineering or Mathematics or comparable experience; Ability to develop \nsoftware in C#, AngularJS, or other selected languages; Familiarity with AWS, \nASP.",
        "title": "Moxe Health - Integration Engineer"
    },
    {
        "cacheId": "zyyMZNgCHMAJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../4f0bb75e-5124-48ae-845d-95227e055fb3",
        "htmlFormattedUrl": "https://jobs.lever.co/.../4f0bb75e-5124-48ae-845d-95227e055fb3",
        "htmlSnippet": "You&#39;re comfortable interfacing with and migrating object oriented code bases in <br>\n<b>C#</b> or similar. You&#39;re comfortable working on multiple operating systems and&nbsp;...",
        "htmlTitle": "BoomTown - Scala Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/boomtownroi.com/4f0bb75e-5124-48ae-845d-95227e055fb3",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/035d99be-98af-422a-aeb3-25d8c844018f-1468443033584.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRriALjfc-FHmorRLrF57SqKQ3DE7rrCgRuPs-6mpHIG6wQNoofhrq3Fcg",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "What we do: As a Scala developer on the Foundation team, you provide the web services, messaging systems, data stores, and other server-side systems our product teams need to get their job done quickly and easily. You\u2019ll be charged with continuously enhancing and reinventing BoomTown\u2019s server side platform. You\u2019ll use functional Scala to implement high performance web services backed by Redis, DynamoDB, SQL server, etc. You\u2019ll be a key player in designing and refining BoomTown\u2019s server side APIs.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/035d99be-98af-422a-aeb3-25d8c844018f-1468443033584.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "BoomTown - Scala Developer",
                    "og:url": "https://jobs.lever.co/boomtownroi.com/4f0bb75e-5124-48ae-845d-95227e055fb3",
                    "twitter:description": "What we do: As a Scala developer on the Foundation team, you provide the web services, messaging systems, data stores, and other server-side systems our product teams need to get their job done quickly and easily. You\u2019ll be charged with continuously enhancing and reinventing BoomTown\u2019s server side platform. You\u2019ll use functional Scala to implement high performance web services backed by Redis, DynamoDB, SQL server, etc. You\u2019ll be a key player in designing and refining BoomTown\u2019s server side APIs.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/035d99be-98af-422a-aeb3-25d8c844018f-1468443025221.png",
                    "twitter:title": "BoomTown - Scala Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "You're comfortable interfacing with and migrating object oriented code bases in \nC# or similar. You're comfortable working on multiple operating systems and\u00a0...",
        "title": "BoomTown - Scala Developer"
    },
    {
        "cacheId": "PXeIikiXPzwJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../081e7bae-1bdb-4209-b08f-96fc3002042e",
        "htmlFormattedUrl": "https://jobs.lever.co/.../081e7bae-1bdb-4209-b08f-96fc3002042e",
        "htmlSnippet": "... Basic knowledge of some the following coding languages: <b>C#</b>, Python, Ruby, <br>\nJAVA; Expert knowledge in administrating databases (SQL); Experience working<br>\n&nbsp;...",
        "htmlTitle": "Kasasa - STAT Engineer I",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/kasasa/081e7bae-1bdb-4209-b08f-96fc3002042e",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/25a8cb0b-98da-45bd-b15d-752bd4af69e7-1495631361165.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "163",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQDqAcJPxNb5IUyXkhJJ6Dc-MvZgu0wMSvM_TTtz2sadc_R9biYgODTC38",
                    "width": "310"
                }
            ],
            "metatags": [
                {
                    "og:description": "SUMMARY OF PURPOSE: The STAT Engineer I is a key member of the Kasasa Technical Operations Team. STAT Engineer I\u2019s primary responsibility is to function as an escalation point for Kasasa\u2019s Technical Support and Technical Installation Teams while embodying the Patch Values. This includes acting as a subject matter expert (SME) on Kasasa\u2019s On Premise and SAAS model software, executing strategic client facing project plans, and representing Technical Operations in Product Team initiatives. She/He will also be responsible for maintaining product-to-3rd Party Vendor interfaces to ensure continuous successful integration of Kasasa Products with Community Financial Institutions\u2019 Core Vendors and for providing support to Kasasa\u2019s internal Billing and Analytics departments. The STAT Engineer I is a highly motivated and experienced professional, with a strong work ethic, a broad range of technical skills, and a deep knowledge of Kasasa\u2019s products and services. He/She must also work independe",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/25a8cb0b-98da-45bd-b15d-752bd4af69e7-1495631361165.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Kasasa - STAT Engineer I",
                    "og:url": "https://jobs.lever.co/kasasa/081e7bae-1bdb-4209-b08f-96fc3002042e",
                    "twitter:description": "SUMMARY OF PURPOSE: The STAT Engineer I is a key member of the Kasasa Technical Operations Team. STAT Engineer I\u2019s primary responsibility is to function as an escalation point for Kasasa\u2019s Technical Support and Technical Installation Teams while embodying the Patch Values. This includes acting as a subject matter expert (SME) on Kasasa\u2019s On Premise and SAAS model software, executing strategic client facing project plans, and representing Technical Operations in Product Team initiatives. She/He will also be responsible for maintaining product-to-3rd Party Vendor interfaces to ensure continuous successful integration of Kasasa Products with Community Financial Institutions\u2019 Core Vendors and for providing support to Kasasa\u2019s internal Billing and Analytics departments. The STAT Engineer I is a highly motivated and experienced professional, with a strong work ethic, a broad range of technical skills, and a deep knowledge of Kasasa\u2019s products and services. He/She must also work independe",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/25a8cb0b-98da-45bd-b15d-752bd4af69e7-1495631367055.png",
                    "twitter:title": "Kasasa - STAT Engineer I",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... Basic knowledge of some the following coding languages: C#, Python, Ruby, \nJAVA; Expert knowledge in administrating databases (SQL); Experience working\n\u00a0...",
        "title": "Kasasa - STAT Engineer I"
    },
    {
        "cacheId": "GJ9S1j-FV9MJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../a055b223-af8b-4eec-a2fc-af90c820e113",
        "htmlFormattedUrl": "https://jobs.lever.co/.../a055b223-af8b-4eec-a2fc-af90c820e113",
        "htmlSnippet": "Bonus if you can rock Swift, <b>C#</b> or Ruby. You have an innate, built-in, almost <br>\nscary penchant for programming. You communicate clearly. You have a proven&nbsp;...",
        "htmlTitle": "Livefront - Android Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/livefront/a055b223-af8b-4eec-a2fc-af90c820e113",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/5c98fa6a-854c-488b-8144-4e7aa1313a44-1495825781391.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "103",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTzoCAGsBCqEFIIKQkNhm_VuvfdLMBcwb6hTtKagfv03GBFwybrHCoNvQ",
                    "width": "491"
                }
            ],
            "metatags": [
                {
                    "og:description": "We're looking for another great mobile developer to join our team. We are a tight-knit, talented group of engineers and designers building custom mobile software for smart clients. We have an incredible attention to detail and very high standards\u2014if you want to join our team, you'll need to demonstrate that you do too. Your primary role will be development of mobile applications on the Android platform. Bonus if you can rock Swift, C# or Ruby. You have an innate, built-in, almost scary penchant for programming. You communicate clearly. You have a proven track-record of self-motivation. You're active in the tech community. You never tire of Chipotle. We are looking for someone to join our team in Minneapolis. For the right talent we offer high salaries, Aeron chairs, fancy gadgets, and other pleasantries.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/5c98fa6a-854c-488b-8144-4e7aa1313a44-1495825781391.png",
                    "og:image:height": "200",
                    "og:title": "Livefront - Android Developer",
                    "og:url": "https://jobs.lever.co/livefront/a055b223-af8b-4eec-a2fc-af90c820e113",
                    "twitter:description": "We're looking for another great mobile developer to join our team. We are a tight-knit, talented group of engineers and designers building custom mobile software for smart clients. We have an incredible attention to detail and very high standards\u2014if you want to join our team, you'll need to demonstrate that you do too. Your primary role will be development of mobile applications on the Android platform. Bonus if you can rock Swift, C# or Ruby. You have an innate, built-in, almost scary penchant for programming. You communicate clearly. You have a proven track-record of self-motivation. You're active in the tech community. You never tire of Chipotle. We are looking for someone to join our team in Minneapolis. For the right talent we offer high salaries, Aeron chairs, fancy gadgets, and other pleasantries.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/5c98fa6a-854c-488b-8144-4e7aa1313a44-1495825787567.png",
                    "twitter:title": "Livefront - Android Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Bonus if you can rock Swift, C# or Ruby. You have an innate, built-in, almost \nscary penchant for programming. You communicate clearly. You have a proven\u00a0...",
        "title": "Livefront - Android Developer"
    },
    {
        "cacheId": "PY3IMsYIHegJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../16c6ccd0-5af8-4f40-8f55-c97c6f3e38cd",
        "htmlFormattedUrl": "https://jobs.lever.co/.../16c6ccd0-5af8-4f40-8f55-c97c6f3e38cd",
        "htmlSnippet": "Unit tests and creating software based test tools. \u00b7 Coding with other languages, <br>\nsuch as C++, <b>C#</b>, etc. We are an equal opportunity employer. Apply for this job.",
        "htmlTitle": "Pivotal Commware - Embedded Software Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/pivotalcommware/16c6ccd0-5af8-4f40-8f55-c97c6f3e38cd",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/b734df48-47a2-4e61-b8ef-1291799b5ef9-1500063391715.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "37",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS7pendMLx8ORB_b5ymxcK3gcPg9oxgxk-QUjuKCBT8anABYXy2ITDfESI",
                    "width": "161"
                }
            ],
            "metatags": [
                {
                    "og:description": "Pivotal is seeking a Embedded Software Engineer supporting the design and maintenance of C code on an NXP/Freescale Coldfire processor, PIC32 and ATMega controllers or an off the shelf SBC. In this position, the engineer will be writing software in C for systems without and with an operating system such as MQX, QNX or Embedded Linux. Responsibilities: \u00b7 Responsible for developing, modifying and maintaining embedded C code for our antenna systems product requirements \u00b7 Ability to work with a team of engineers and have good communication skills \u00b7 Unit test validation of all modifications Qualifications: \u00b7 Bachelor\u2019s or Master\u2019s Degree in Electrical Engineering, Electronics Engineering, Computer Engineering, Computer Science or equivalent \u00b7 2+ years of relevant embedded software development experience as an Embedded Software Engineer, Embedded Developer, Software Engineer, Firmware Engineer or related title \u00b7 Experience in C programm",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/b734df48-47a2-4e61-b8ef-1291799b5ef9-1500063391715.png",
                    "og:image:height": "200",
                    "og:title": "Pivotal Commware - Embedded Software Engineer",
                    "og:url": "https://jobs.lever.co/pivotalcommware/16c6ccd0-5af8-4f40-8f55-c97c6f3e38cd",
                    "twitter:description": "Pivotal is seeking a Embedded Software Engineer supporting the design and maintenance of C code on an NXP/Freescale Coldfire processor, PIC32 and ATMega controllers or an off the shelf SBC. In this position, the engineer will be writing software in C for systems without and with an operating system such as MQX, QNX or Embedded Linux. Responsibilities: \u00b7 Responsible for developing, modifying and maintaining embedded C code for our antenna systems product requirements \u00b7 Ability to work with a team of engineers and have good communication skills \u00b7 Unit test validation of all modifications Qualifications: \u00b7 Bachelor\u2019s or Master\u2019s Degree in Electrical Engineering, Electronics Engineering, Computer Engineering, Computer Science or equivalent \u00b7 2+ years of relevant embedded software development experience as an Embedded Software Engineer, Embedded Developer, Software Engineer, Firmware Engineer or related title \u00b7 Experience in C programm",
                    "twitter:title": "Pivotal Commware - Embedded Software Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Unit tests and creating software based test tools. \u00b7 Coding with other languages, \nsuch as C++, C#, etc. We are an equal opportunity employer. Apply for this job.",
        "title": "Pivotal Commware - Embedded Software Engineer"
    },
    {
        "cacheId": "bfW5kLWbcoYJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../0b103e97-ee4f-4c34-ab71-672fc723ee19",
        "htmlFormattedUrl": "https://jobs.lever.co/.../0b103e97-ee4f-4c34-ab71-672fc723ee19",
        "htmlSnippet": "Experience in a compiled production-class OO or FP programming language <br>\nsuch as Java, Scala, C++, <b>C#</b>, Haskell, ML, Erlang, Clojure, Rust, etc. Experience<br>\n&nbsp;...",
        "htmlTitle": "CiBO Technologies - Computer Vision Scientist - St Louis",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/cibotechnologies/0b103e97-ee4f-4c34-ab71-672fc723ee19",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/dd2e0aa0-4905-44cc-a2a4-d74d85838438-1492695934888.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "121",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSkmNvkyMjhJq32mxdKanJki0nAy_6paCQ_h3P1jKJ5K5DpyaPXOcgPUQ",
                    "width": "415"
                }
            ],
            "metatags": [
                {
                    "og:description": "As a Computer Vision Scientist at CiBO you\u2019ll be part of a collaborative team of developers, data scientists, agronomists, and other remote sensing experts. You will help enrich our pipeline of image-based knowledge components in support of our core platform that creates, improves, and scales agricultural models and optimization. Our culture is built on cross-disciplinary collaboration, learning, and rapid prototyping. CiBO is a science-based company, so prepare to learn and invent with us! Qualifications: Solid foundation in computer vision, image processing and analysis, and remote sensing principles. Understanding at least one of ground, airborne, and space-based image collection platforms. Experience sourcing, curating, processing, and interpreting data from multiple imaging modalities, such as multi/hyperspectral, thermal, LiDAR, radar, etc. Experience developing algorithms and methods for object detection and classification. Experience with remote sensing/GIS tools: ArcGIS",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/dd2e0aa0-4905-44cc-a2a4-d74d85838438-1492695934888.png",
                    "og:image:height": "200",
                    "og:title": "CiBO Technologies - Computer Vision Scientist - St Louis",
                    "og:url": "https://jobs.lever.co/cibotechnologies/0b103e97-ee4f-4c34-ab71-672fc723ee19",
                    "twitter:description": "As a Computer Vision Scientist at CiBO you\u2019ll be part of a collaborative team of developers, data scientists, agronomists, and other remote sensing experts. You will help enrich our pipeline of image-based knowledge components in support of our core platform that creates, improves, and scales agricultural models and optimization. Our culture is built on cross-disciplinary collaboration, learning, and rapid prototyping. CiBO is a science-based company, so prepare to learn and invent with us! Qualifications: Solid foundation in computer vision, image processing and analysis, and remote sensing principles. Understanding at least one of ground, airborne, and space-based image collection platforms. Experience sourcing, curating, processing, and interpreting data from multiple imaging modalities, such as multi/hyperspectral, thermal, LiDAR, radar, etc. Experience developing algorithms and methods for object detection and classification. Experience with remote sensing/GIS tools: ArcGIS",
                    "twitter:title": "CiBO Technologies - Computer Vision Scientist - St Louis",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Experience in a compiled production-class OO or FP programming language \nsuch as Java, Scala, C++, C#, Haskell, ML, Erlang, Clojure, Rust, etc. Experience\n\u00a0...",
        "title": "CiBO Technologies - Computer Vision Scientist - St Louis"
    },
    {
        "cacheId": "SpL9B_ejKbUJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/axon/289e11b7-68e5-4a85-a0e9-27f01b9c4fdb",
        "htmlFormattedUrl": "https://jobs.lever.co/axon/289e11b7-68e5-4a85-a0e9-27f01b9c4fdb",
        "htmlSnippet": "4+ years experience in designing and developing software; Significant <br>\nprogramming experience in one of these: Scala, Java, <b>C#</b>, Go (Golang, Ruby or <br>\nthe like.",
        "htmlTitle": "Axon - Full Stack Engineer - Connected Devices",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/axon/289e11b7-68e5-4a85-a0e9-27f01b9c4fdb",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/6aa14d12-a323-4bcb-9368-48a4fd3d7aca-1497567326829.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "190",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSv4tWaK_c0_aSAH7VHCIUaK9xIw5lCeCQPyYa_yNBPWqTL6cv1-JKwKWur",
                    "width": "266"
                }
            ],
            "metatags": [
                {
                    "og:description": "Your Impact Have you ever wondered if you can write code to save lives? At Axon our mission is to protect life. We are passionate about bringing state of the art technology to law enforcement so officers can focus on helping their communities instead of fighting with bad software. We are looking for talented full stack software engineers to help us build world-class cloud applications. You will work with product managers and designers to deliver top quality products that are innovative and practical for our end users. You will work with different client teams (body cameras, mobile apps, desktop apps, etc..) to ensure we are building seamlessly integrated products that will give police officers the tools and insight to make our communities safer. Should you join the team, you will be surrounded by like-minded people who are passionate about our mission to protect life. Are you ready to help us make a difference? We believe in pushing autonomy as deeply as possible into the team. A dee",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/6aa14d12-a323-4bcb-9368-48a4fd3d7aca-1497567326829.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Axon - Full Stack Engineer - Connected Devices",
                    "og:url": "https://jobs.lever.co/axon/289e11b7-68e5-4a85-a0e9-27f01b9c4fdb",
                    "twitter:description": "Your Impact Have you ever wondered if you can write code to save lives? At Axon our mission is to protect life. We are passionate about bringing state of the art technology to law enforcement so officers can focus on helping their communities instead of fighting with bad software. We are looking for talented full stack software engineers to help us build world-class cloud applications. You will work with product managers and designers to deliver top quality products that are innovative and practical for our end users. You will work with different client teams (body cameras, mobile apps, desktop apps, etc..) to ensure we are building seamlessly integrated products that will give police officers the tools and insight to make our communities safer. Should you join the team, you will be surrounded by like-minded people who are passionate about our mission to protect life. Are you ready to help us make a difference? We believe in pushing autonomy as deeply as possible into the team. A dee",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/6aa14d12-a323-4bcb-9368-48a4fd3d7aca-1497567377352.png",
                    "twitter:title": "Axon - Full Stack Engineer - Connected Devices",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "4+ years experience in designing and developing software; Significant \nprogramming experience in one of these: Scala, Java, C#, Go (Golang, Ruby or \nthe like.",
        "title": "Axon - Full Stack Engineer - Connected Devices"
    },
    {
        "cacheId": "cNuRlOr8WSwJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/axon/c21f4afd-a7d3-4ab6-95b3-32168d837efe",
        "htmlFormattedUrl": "https://jobs.lever.co/axon/c21f4afd-a7d3-4ab6-95b3-32168d837efe",
        "htmlSnippet": "Back-end service experience in managed languages such as Java, Scala, Go, <br>\n<b>C#</b>, or similar. Some experience in frontend technologies like React or Angular&nbsp;...",
        "htmlTitle": "Axon - Sr Full Stack Engineer, Technical Lead",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/axon/c21f4afd-a7d3-4ab6-95b3-32168d837efe",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/6aa14d12-a323-4bcb-9368-48a4fd3d7aca-1497567326829.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "190",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSv4tWaK_c0_aSAH7VHCIUaK9xIw5lCeCQPyYa_yNBPWqTL6cv1-JKwKWur",
                    "width": "266"
                }
            ],
            "metatags": [
                {
                    "og:description": "Your Impact At Axon, we build the next generation of law enforcement and public safety technologies to empower our customers to serve and protect their communities. Our team is solving some of the hardest cloud challenges today. Every day we manage petabytes of video from hundreds of thousands of police officers around the world, and help the public with creative solutions from the courtroom to public disclosure. Come work in an exciting environment in which you use your passion, experience, and strong analytical skills to help bring new technologies to public safety and leave a positive impact on the world. Are you a natural leader who will own design and implementation of high quality systems which provide compelling features for your end-user? Do you have a passion for building cloud services, designing scalable, secure systems, and designing features that delight customers? As a tech lead on our evidence management system, you will lead a high-energy team of engineers that ha",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/6aa14d12-a323-4bcb-9368-48a4fd3d7aca-1497567326829.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Axon - Sr Full Stack Engineer, Technical Lead",
                    "og:url": "https://jobs.lever.co/axon/c21f4afd-a7d3-4ab6-95b3-32168d837efe",
                    "twitter:description": "Your Impact At Axon, we build the next generation of law enforcement and public safety technologies to empower our customers to serve and protect their communities. Our team is solving some of the hardest cloud challenges today. Every day we manage petabytes of video from hundreds of thousands of police officers around the world, and help the public with creative solutions from the courtroom to public disclosure. Come work in an exciting environment in which you use your passion, experience, and strong analytical skills to help bring new technologies to public safety and leave a positive impact on the world. Are you a natural leader who will own design and implementation of high quality systems which provide compelling features for your end-user? Do you have a passion for building cloud services, designing scalable, secure systems, and designing features that delight customers? As a tech lead on our evidence management system, you will lead a high-energy team of engineers that ha",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/6aa14d12-a323-4bcb-9368-48a4fd3d7aca-1497567377352.png",
                    "twitter:title": "Axon - Sr Full Stack Engineer, Technical Lead",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Back-end service experience in managed languages such as Java, Scala, Go, \nC#, or similar. Some experience in frontend technologies like React or Angular\u00a0...",
        "title": "Axon - Sr Full Stack Engineer, Technical Lead"
    },
    {
        "cacheId": "lGvO7b3oALIJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/axon/bf783632-57dc-417f-a7fd-51409366ddff",
        "htmlFormattedUrl": "https://jobs.lever.co/axon/bf783632-57dc-417f-a7fd-51409366ddff",
        "htmlSnippet": "Back-end service experience in managed languages such as Java, Scala, Go, <br>\n<b>C#</b>, or similar. Strong knowledge of standards such as OpenID Connect, OAUTH,<br>\n&nbsp;...",
        "htmlTitle": "Axon - Senior Software Engineer, Security",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/axon/bf783632-57dc-417f-a7fd-51409366ddff",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/6aa14d12-a323-4bcb-9368-48a4fd3d7aca-1497567326829.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "190",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSv4tWaK_c0_aSAH7VHCIUaK9xIw5lCeCQPyYa_yNBPWqTL6cv1-JKwKWur",
                    "width": "266"
                }
            ],
            "metatags": [
                {
                    "og:description": "Our team is solving some of the hardest cloud challenges today. Every day we manage petabytes of video from hundreds of thousands of police officers around the world, and help the public with creative solutions from the courtroom to public disclosure. Come work in an exciting environment in which you use your passion, experience, and strong analytical skills to help bring new technologies to public safety and leave a positive impact on the world. Your Impact Do you love to find flaws in protocols such as JWT? How about finding novel ways into getting software to do things it shouldn't? Can you describe the attacks against Merkle trees? Are you someone who sees the OWASP Top 10 a great bedtime story? You are a Senior Software Engineer with a background in security, cryptography, and distributed systems. You will be responsible for innovating upon Axon's core security and cryptography technology platform. You will have the opportunity to: - Build authorization, authentication and",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/6aa14d12-a323-4bcb-9368-48a4fd3d7aca-1497567326829.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Axon - Senior Software Engineer, Security",
                    "og:url": "https://jobs.lever.co/axon/bf783632-57dc-417f-a7fd-51409366ddff",
                    "twitter:description": "Our team is solving some of the hardest cloud challenges today. Every day we manage petabytes of video from hundreds of thousands of police officers around the world, and help the public with creative solutions from the courtroom to public disclosure. Come work in an exciting environment in which you use your passion, experience, and strong analytical skills to help bring new technologies to public safety and leave a positive impact on the world. Your Impact Do you love to find flaws in protocols such as JWT? How about finding novel ways into getting software to do things it shouldn't? Can you describe the attacks against Merkle trees? Are you someone who sees the OWASP Top 10 a great bedtime story? You are a Senior Software Engineer with a background in security, cryptography, and distributed systems. You will be responsible for innovating upon Axon's core security and cryptography technology platform. You will have the opportunity to: - Build authorization, authentication and",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/6aa14d12-a323-4bcb-9368-48a4fd3d7aca-1497567377352.png",
                    "twitter:title": "Axon - Senior Software Engineer, Security",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Back-end service experience in managed languages such as Java, Scala, Go, \nC#, or similar. Strong knowledge of standards such as OpenID Connect, OAUTH,\n\u00a0...",
        "title": "Axon - Senior Software Engineer, Security"
    },
    {
        "cacheId": "LhJkhrvLEZIJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../4cfe59f5-5c17-45a9-95d6-ea189d37a66d",
        "htmlFormattedUrl": "https://jobs.lever.co/.../4cfe59f5-5c17-45a9-95d6-ea189d37a66d",
        "htmlSnippet": "... is fine too as long as you don&#39;t mind switching); Experience with at least one or <br>\nmultiple: <b>C#</b>, C++, Java; You&#39;ve worked on developing or optimizing an engine&nbsp;...",
        "htmlTitle": "LiveLike - Sr. Unity VR Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/livelike/4cfe59f5-5c17-45a9-95d6-ea189d37a66d",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/8f88efa0-afe3-464a-81a4-36b26e103a5b-1487892293689.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "102",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRg40aMJwtikEXQxmMCQW16ziv5alRMuT1FfgDktYB9sFMx3unn7bfAMzI",
                    "width": "492"
                }
            ],
            "metatags": [
                {
                    "og:description": "NOTE: This role isn't currently open, but will be in a few months. If you'd like to apply, your resume/portfolio will be the first to be reviewed when the time comes. At LiveLike we build things that challenge the typical concept of what it means to watch live sports. So it's only natural for us to specialize in creating one of the best platforms to watch live sports in virtual reality. For that to happen though, we need a team of developers and designers that are not only the some of the best, but who are comfortable working outside of the status quo. We\u2019re looking for the newest member of our Front-end development team. Someone who not only is a Unity Development specialist, but someone who brings the same fire to work everyday that we do. If you think you\u2019ve got the skills and are up for the challenge then consider this your calling.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/8f88efa0-afe3-464a-81a4-36b26e103a5b-1487892293689.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "LiveLike - Sr. Unity VR Developer",
                    "og:url": "https://jobs.lever.co/livelike/4cfe59f5-5c17-45a9-95d6-ea189d37a66d",
                    "twitter:description": "NOTE: This role isn't currently open, but will be in a few months. If you'd like to apply, your resume/portfolio will be the first to be reviewed when the time comes. At LiveLike we build things that challenge the typical concept of what it means to watch live sports. So it's only natural for us to specialize in creating one of the best platforms to watch live sports in virtual reality. For that to happen though, we need a team of developers and designers that are not only the some of the best, but who are comfortable working outside of the status quo. We\u2019re looking for the newest member of our Front-end development team. Someone who not only is a Unity Development specialist, but someone who brings the same fire to work everyday that we do. If you think you\u2019ve got the skills and are up for the challenge then consider this your calling.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/8f88efa0-afe3-464a-81a4-36b26e103a5b-1487955294475.png",
                    "twitter:title": "LiveLike - Sr. Unity VR Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... is fine too as long as you don't mind switching); Experience with at least one or \nmultiple: C#, C++, Java; You've worked on developing or optimizing an engine\u00a0...",
        "title": "LiveLike - Sr. Unity VR Developer"
    },
    {
        "cacheId": "CKQ_glLD48QJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../d099bfef-cce8-447e-aa26-65387c531e09",
        "htmlFormattedUrl": "https://jobs.lever.co/.../d099bfef-cce8-447e-aa26-65387c531e09",
        "htmlSnippet": "Experience in a compiled production-class OO or FP programming language <br>\nsuch as Java, Scala, C++, <b>C#</b>, Haskell, ML, Erlang, Clojure, Rust, etc. Experience<br>\n&nbsp;...",
        "htmlTitle": "CiBO Technologies - Senior Remote Sensing Scientist - St Louis",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/cibotechnologies/d099bfef-cce8-447e-aa26-65387c531e09",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/dd2e0aa0-4905-44cc-a2a4-d74d85838438-1492695934888.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "121",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSkmNvkyMjhJq32mxdKanJki0nAy_6paCQ_h3P1jKJ5K5DpyaPXOcgPUQ",
                    "width": "415"
                }
            ],
            "metatags": [
                {
                    "og:description": "As a Senior Remote Sensing Scientist at CiBO you\u2019ll be part of a collaborative team of developers, data scientists, agronomists, and other remote sensing experts. You will help enrich the pipeline of image-based knowledge components in support of our core platform that creates, improves, and scales agricultural models and optimization. Our culture is built on cross-disciplinary collaboration, learning, and rapid prototyping. CiBO is a science-based company, so prepare to learn and invent with us! Qualifications: Solid foundation in computer vision, image processing and analysis, and remote sensing principles. Comprehensive understanding and experience with ground, airborne, and space-based image collection platforms. Significant experience sourcing, curating, processing, and interpreting large volumes of data from variety of imaging modalities, such as multi/hyperspectral, thermal, LiDAR, radar, etc. Significant experience developing algorithms and methods for object detection an",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/dd2e0aa0-4905-44cc-a2a4-d74d85838438-1492695934888.png",
                    "og:image:height": "200",
                    "og:title": "CiBO Technologies - Senior Remote Sensing Scientist - St Louis",
                    "og:url": "https://jobs.lever.co/cibotechnologies/d099bfef-cce8-447e-aa26-65387c531e09",
                    "twitter:description": "As a Senior Remote Sensing Scientist at CiBO you\u2019ll be part of a collaborative team of developers, data scientists, agronomists, and other remote sensing experts. You will help enrich the pipeline of image-based knowledge components in support of our core platform that creates, improves, and scales agricultural models and optimization. Our culture is built on cross-disciplinary collaboration, learning, and rapid prototyping. CiBO is a science-based company, so prepare to learn and invent with us! Qualifications: Solid foundation in computer vision, image processing and analysis, and remote sensing principles. Comprehensive understanding and experience with ground, airborne, and space-based image collection platforms. Significant experience sourcing, curating, processing, and interpreting large volumes of data from variety of imaging modalities, such as multi/hyperspectral, thermal, LiDAR, radar, etc. Significant experience developing algorithms and methods for object detection an",
                    "twitter:title": "CiBO Technologies - Senior Remote Sensing Scientist - St Louis",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Experience in a compiled production-class OO or FP programming language \nsuch as Java, Scala, C++, C#, Haskell, ML, Erlang, Clojure, Rust, etc. Experience\n\u00a0...",
        "title": "CiBO Technologies - Senior Remote Sensing Scientist - St Louis"
    },
    {
        "cacheId": "1qp3NsxdMg0J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../40ffcf93-5a9d-4157-a9e3-88738329be56",
        "htmlFormattedUrl": "https://jobs.lever.co/.../40ffcf93-5a9d-4157-a9e3-88738329be56",
        "htmlSnippet": "5+ years as a software engineer working with OOP languages such as: Python, <br>\n<b>C#</b>, C++, Java. Background in electrical engineering, applied math, gaming,&nbsp;...",
        "htmlTitle": "Tempo Automation - Senior Software Engineer (Factory Automation)",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/tempoautomation/40ffcf93-5a9d-4157-a9e3-88738329be56",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/tempoautomationlogo.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "64",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTqy0euUBBsar9f7SInSE4tQPnw5ec5t6fP4GqEULWOxu-eACv5xQthqQ",
                    "width": "600"
                }
            ],
            "metatags": [
                {
                    "og:description": "Join a growing team that's using software to revolutionize the world of electronics manufacturing! We are looking for talented developers who want to make it as fast and seamless as possible for electrical engineers to manufacture their designs, iterate on their ideas, and bring their products to market. This position offers the opportunity to work on CAD analysis tools and robotic factory automation software. A great candidate would have a passion for automating manual processes, building software that delights customers and interest in the hardware space. We are looking for a team player who will learn, coach, and help us make this incredible vision a reality. To learn more about working at Tempo, visit our careers page.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/tempoautomationlogo.png",
                    "og:image:height": "200",
                    "og:title": "Tempo Automation - Senior Software Engineer (Factory Automation)",
                    "og:url": "https://jobs.lever.co/tempoautomation/40ffcf93-5a9d-4157-a9e3-88738329be56",
                    "twitter:description": "Join a growing team that's using software to revolutionize the world of electronics manufacturing! We are looking for talented developers who want to make it as fast and seamless as possible for electrical engineers to manufacture their designs, iterate on their ideas, and bring their products to market. This position offers the opportunity to work on CAD analysis tools and robotic factory automation software. A great candidate would have a passion for automating manual processes, building software that delights customers and interest in the hardware space. We are looking for a team player who will learn, coach, and help us make this incredible vision a reality. To learn more about working at Tempo, visit our careers page.",
                    "twitter:title": "Tempo Automation - Senior Software Engineer (Factory Automation)",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "5+ years as a software engineer working with OOP languages such as: Python, \nC#, C++, Java. Background in electrical engineering, applied math, gaming,\u00a0...",
        "title": "Tempo Automation - Senior Software Engineer (Factory Automation)"
    },
    {
        "cacheId": "P3zq7zWal1UJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../8d0f4e75-fd03-470c-a166-c23e693b2a4c",
        "htmlFormattedUrl": "https://jobs.lever.co/.../8d0f4e75-fd03-470c-a166-c23e693b2a4c",
        "htmlSnippet": "NET, Java, <b>C#</b> or similar languages. Good command of written and spoken <br>\nEnglish. Strong communication skills and a good team player. Strong sense of&nbsp;...",
        "htmlTitle": "Trendyol - Tech Talent Program - New Grad",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/trendyol/8d0f4e75-fd03-470c-a166-c23e693b2a4c",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/a81a734c-54a8-4378-85ba-2eee13010fb6-1502976769600.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "159",
                    "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQxncxuxq-iTpXIwKjDQLyYxA_by4qvx_tXZvVABZCwZ4pVC1k5J4UOt9pN",
                    "width": "318"
                }
            ],
            "metatags": [
                {
                    "og:description": "Join the region\u2019s fastest growing technology company and largest fashion e-tailer in this exciting opportunity! Trendyol.com is the largest fashion e-commerce company in Turkey and the MENA region selling more than 25 million fashion items per year. Trendyol's mission is to make fashion accessible and serves over 12 million customers, has 50 million monthly visits and is the fastest growing e-commerce company in the region. Founded in 2010, Trendyol is the biggest internet employer in Turkey with a team of ca. 1200 people. Investors include Kleiner Perkins, Tiger Global and EBRD. We are looking for passionate Tech Talents who is enthusiastic to play a key role in helping Trendyol provide the best experience to millions of customers! You should be energetic and flexible because we want you to adapt to our dynamic and lively environment!",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/a81a734c-54a8-4378-85ba-2eee13010fb6-1502976769600.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Trendyol - Tech Talent Program - New Grad",
                    "og:url": "https://jobs.lever.co/trendyol/8d0f4e75-fd03-470c-a166-c23e693b2a4c",
                    "twitter:description": "Join the region\u2019s fastest growing technology company and largest fashion e-tailer in this exciting opportunity! Trendyol.com is the largest fashion e-commerce company in Turkey and the MENA region selling more than 25 million fashion items per year. Trendyol's mission is to make fashion accessible and serves over 12 million customers, has 50 million monthly visits and is the fastest growing e-commerce company in the region. Founded in 2010, Trendyol is the biggest internet employer in Turkey with a team of ca. 1200 people. Investors include Kleiner Perkins, Tiger Global and EBRD. We are looking for passionate Tech Talents who is enthusiastic to play a key role in helping Trendyol provide the best experience to millions of customers! You should be energetic and flexible because we want you to adapt to our dynamic and lively environment!",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/a81a734c-54a8-4378-85ba-2eee13010fb6-1502963363823.png",
                    "twitter:title": "Trendyol - Tech Talent Program - New Grad",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "NET, Java, C# or similar languages. Good command of written and spoken \nEnglish. Strong communication skills and a good team player. Strong sense of\u00a0...",
        "title": "Trendyol - Tech Talent Program - New Grad"
    },
    {
        "cacheId": "pWq7Y21MbHsJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../3abce5a9-9eaa-465b-a93f-7573bd5a27a0",
        "htmlFormattedUrl": "https://jobs.lever.co/.../3abce5a9-9eaa-465b-a93f-7573bd5a27a0",
        "htmlSnippet": "... Strong coding ability in an object oriented language (Python, Ruby, Java, <b>C#</b>, <br>\netc.) Excellent team player with strong communication skills (verbal and written)&nbsp;...",
        "htmlTitle": "shopkick - Senior Manager, Engineering, Growth Team",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/shopkick/3abce5a9-9eaa-465b-a93f-7573bd5a27a0",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/eee4151d-2983-4094-8923-70602a8e396e-1458237928467.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "162",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQvQeQ4dWP5C806HB7CzfQs5KLGpvD8P9s72kpHKMQZiLcYClTV-yCnpNg",
                    "width": "311"
                }
            ],
            "metatags": [
                {
                    "og:description": "At Shopkick, the leading in-store shopping app in the USA, we love our users and of course we love finding new ways we can get more! To that end we are looking for a quick-thinking, constantly testing, and naturally persistent Senior Manager to lead our Growth team to A/B test our way to more users.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/eee4151d-2983-4094-8923-70602a8e396e-1458237928467.png",
                    "og:image:height": "200",
                    "og:title": "shopkick - Senior Manager, Engineering, Growth Team",
                    "og:url": "https://jobs.lever.co/shopkick/3abce5a9-9eaa-465b-a93f-7573bd5a27a0",
                    "twitter:description": "At Shopkick, the leading in-store shopping app in the USA, we love our users and of course we love finding new ways we can get more! To that end we are looking for a quick-thinking, constantly testing, and naturally persistent Senior Manager to lead our Growth team to A/B test our way to more users.",
                    "twitter:title": "shopkick - Senior Manager, Engineering, Growth Team",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... Strong coding ability in an object oriented language (Python, Ruby, Java, C#, \netc.) Excellent team player with strong communication skills (verbal and written)\u00a0...",
        "title": "shopkick - Senior Manager, Engineering, Growth Team"
    },
    {
        "cacheId": "CYkqu9cWBlcJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../17599681-9cac-4d0c-9f84-62d85874797a",
        "htmlFormattedUrl": "https://jobs.lever.co/.../17599681-9cac-4d0c-9f84-62d85874797a",
        "htmlSnippet": "... server software; Strong experience building location-based services; Strong <br>\ncoding ability in an object oriented language (Python, Ruby, Java, <b>C#</b>, etc.)&nbsp;...",
        "htmlTitle": "shopkick - Senior Server Engineer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/shopkick/17599681-9cac-4d0c-9f84-62d85874797a",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/eee4151d-2983-4094-8923-70602a8e396e-1458237928467.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "162",
                    "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQvQeQ4dWP5C806HB7CzfQs5KLGpvD8P9s72kpHKMQZiLcYClTV-yCnpNg",
                    "width": "311"
                }
            ],
            "metatags": [
                {
                    "og:description": "At Shopkick, the leading in-store shopping app in the USA, we are looking to form a new strike team in Toronto to extend our leading mobile shopping rewards experience on our native mobile clients. We are looking for an amazing server engineer to act as a lead for this major expansion. Working with our Silicon Valley headquarters to guide the architectural direction and implementation you will be responsible for the successful operation and extension of this critical feature.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/eee4151d-2983-4094-8923-70602a8e396e-1458237928467.png",
                    "og:image:height": "200",
                    "og:title": "shopkick - Senior Server Engineer",
                    "og:url": "https://jobs.lever.co/shopkick/17599681-9cac-4d0c-9f84-62d85874797a",
                    "twitter:description": "At Shopkick, the leading in-store shopping app in the USA, we are looking to form a new strike team in Toronto to extend our leading mobile shopping rewards experience on our native mobile clients. We are looking for an amazing server engineer to act as a lead for this major expansion. Working with our Silicon Valley headquarters to guide the architectural direction and implementation you will be responsible for the successful operation and extension of this critical feature.",
                    "twitter:title": "shopkick - Senior Server Engineer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "... server software; Strong experience building location-based services; Strong \ncoding ability in an object oriented language (Python, Ruby, Java, C#, etc.)\u00a0...",
        "title": "shopkick - Senior Server Engineer"
    },
    {
        "cacheId": "040sTW_2KeIJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../98c1de49-4e12-4c46-b99f-be36a0d1f290",
        "htmlFormattedUrl": "https://jobs.lever.co/.../98c1de49-4e12-4c46-b99f-be36a0d1f290",
        "htmlSnippet": "2+ years programming experience; Expert in <b>C#</b>; Working knowledge of common <br>\nprotocols/standards; Working knowledge of common APIs/Libraries&nbsp;...",
        "htmlTitle": "Mobcrush - Junior Game Developer",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/mobcrush/98c1de49-4e12-4c46-b99f-be36a0d1f290",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/220bff99-d63b-42c5-bbe5-5d63cb8075f7-1498612753186.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "168",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTl_RUOpgT9cFwq83h6lYXBREq3gggcmxVjsV6Dy5b5tKGoSU6H0r4EtTVg",
                    "width": "299"
                }
            ],
            "metatags": [
                {
                    "og:description": "Mobcrush is a live mobile game streaming platform based in Los Angeles, California, with the mission to connect the world\u2019s mobile gaming communities. We're comprised of passionate technologists, design and product team members, funded by top-tier investors, with the unique opportunity to go after a large and growing market. We\u2019re seeking an ambitious, fast-paced learner to join our team. As a Junior Software Developer, you will be working with our in-house Minecraft server software on service compatibility, game updates, and stability. You will collaborate with a small team throughout the development life cycle on a schedule that keeps us as a leader in the market while expanding your technology skill set.",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/220bff99-d63b-42c5-bbe5-5d63cb8075f7-1498612753186.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Mobcrush - Junior Game Developer",
                    "og:url": "https://jobs.lever.co/mobcrush/98c1de49-4e12-4c46-b99f-be36a0d1f290",
                    "twitter:description": "Mobcrush is a live mobile game streaming platform based in Los Angeles, California, with the mission to connect the world\u2019s mobile gaming communities. We're comprised of passionate technologists, design and product team members, funded by top-tier investors, with the unique opportunity to go after a large and growing market. We\u2019re seeking an ambitious, fast-paced learner to join our team. As a Junior Software Developer, you will be working with our in-house Minecraft server software on service compatibility, game updates, and stability. You will collaborate with a small team throughout the development life cycle on a schedule that keeps us as a leader in the market while expanding your technology skill set.",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/220bff99-d63b-42c5-bbe5-5d63cb8075f7-1498612403486.png",
                    "twitter:title": "Mobcrush - Junior Game Developer",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "2+ years programming experience; Expert in C#; Working knowledge of common \nprotocols/standards; Working knowledge of common APIs/Libraries\u00a0...",
        "title": "Mobcrush - Junior Game Developer"
    },
    {
        "cacheId": "9qKKrPwmXA4J",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../65440ff5-b06e-441f-a6b8-ba2a13f68756",
        "htmlFormattedUrl": "https://jobs.lever.co/.../65440ff5-b06e-441f-a6b8-ba2a13f68756",
        "htmlSnippet": "Desired Skills and Experience. 2 Years of work experience in a similar role (<br>\noptional); Experience in Object Oriented Programming (Java, <b>C#</b>, etc.) <br>\nExperience in&nbsp;...",
        "htmlTitle": "Capital Float - Software Engineer - Back End",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/capitalfloat/65440ff5-b06e-441f-a6b8-ba2a13f68756",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/8eb4383d-6f87-4bd9-a0f9-d05249136fed-1461029210202.jpg"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "140",
                    "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfaB89hxizyMkXrziJWnrQRdEl4bd-5N1e2AIHf6dtxUoGZXLSy7SvCIJC",
                    "width": "360"
                }
            ],
            "metatags": [
                {
                    "og:description": "Job Description: 1) Integration of existing API\u2019s as well as third party API\u2019s (be it JSON, XML, etc.) 2) Building out new functionality and API\u2019s as per specs provided by product team 3) Unifying data structures across multiple internal built systems to ensure continuity and enhancements of functionality 4) Implement scalable, robust and highly available solutions 5) Identify and/or question problems/issues and have the ability to scope out a solution with clean modular code 6) Work with the QA team to ensure that your code is always delivered on time and matching the criteria of all stories",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/8eb4383d-6f87-4bd9-a0f9-d05249136fed-1461029210202.jpg",
                    "og:image:height": "200",
                    "og:title": "Capital Float - Software Engineer - Back End",
                    "og:url": "https://jobs.lever.co/capitalfloat/65440ff5-b06e-441f-a6b8-ba2a13f68756",
                    "twitter:description": "Job Description: 1) Integration of existing API\u2019s as well as third party API\u2019s (be it JSON, XML, etc.) 2) Building out new functionality and API\u2019s as per specs provided by product team 3) Unifying data structures across multiple internal built systems to ensure continuity and enhancements of functionality 4) Implement scalable, robust and highly available solutions 5) Identify and/or question problems/issues and have the ability to scope out a solution with clean modular code 6) Work with the QA team to ensure that your code is always delivered on time and matching the criteria of all stories",
                    "twitter:title": "Capital Float - Software Engineer - Back End",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Desired Skills and Experience. 2 Years of work experience in a similar role (\noptional); Experience in Object Oriented Programming (Java, C#, etc.) \nExperience in\u00a0...",
        "title": "Capital Float - Software Engineer - Back End"
    },
    {
        "cacheId": "ATsAbjJ6cggJ",
        "displayLink": "jobs.lever.co",
        "formattedUrl": "https://jobs.lever.co/.../39352b26-1e12-4e64-9971-9f5464d43d9e",
        "htmlFormattedUrl": "https://jobs.lever.co/.../39352b26-1e12-4e64-9971-9f5464d43d9e",
        "htmlSnippet": "Prior industry experience as a software engineer (or domain knowledge in <br>\nlending, though not required); Experience with Javascript, Node.js, Python or <b>C#</b><br>\n&nbsp;...",
        "htmlTitle": "Blend - Software Engineer - Client Integrations",
        "kind": "customsearch#result",
        "link": "https://jobs.lever.co/blendlabs/39352b26-1e12-4e64-9971-9f5464d43d9e",
        "pagemap": {
            "cse_image": [
                {
                    "src": "https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png"
                }
            ],
            "cse_thumbnail": [
                {
                    "height": "163",
                    "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSNCrJkMtLwCgS-SEcJpCUkVpXhLZ2CE73LfALkuA_Tn5sy_q80jYcNPmcq",
                    "width": "310"
                }
            ],
            "metatags": [
                {
                    "og:description": "At Blend, we\u2019re dedicated to improving lending. We are a financial technology company with a product that affects the most important purchase most people will make in their lifetime\u2014their home. For homebuyers, our product provides a clear and guided path to a new home, and for lenders, it streamlines their work process, enabling employees to spend more time assisting customers, rather than performing repetitive or manual tasks. By aligning and modernizing the mortgage industry, and consumer finance more generally, we believe everybody wins. We\u2019re motivated by the fact that our product won\u2019t just affect the lives of a few people in the Bay Area\u2014 it affects people all over the U.S., not to mention a foundational part of the U.S. economy. We\u2019re looking for talented software developers who are driven to understand how complex systems work and enjoy solving challenging problems to join our diverse and growing team. As a Software Engineer on our Client Integrations team, you will be respo",
                    "og:image": "https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968610278.png",
                    "og:image:height": "630",
                    "og:image:width": "1200",
                    "og:title": "Blend - Software Engineer - Client Integrations",
                    "og:url": "https://jobs.lever.co/blendlabs/39352b26-1e12-4e64-9971-9f5464d43d9e",
                    "twitter:description": "At Blend, we\u2019re dedicated to improving lending. We are a financial technology company with a product that affects the most important purchase most people will make in their lifetime\u2014their home. For homebuyers, our product provides a clear and guided path to a new home, and for lenders, it streamlines their work process, enabling employees to spend more time assisting customers, rather than performing repetitive or manual tasks. By aligning and modernizing the mortgage industry, and consumer finance more generally, we believe everybody wins. We\u2019re motivated by the fact that our product won\u2019t just affect the lives of a few people in the Bay Area\u2014 it affects people all over the U.S., not to mention a foundational part of the U.S. economy. We\u2019re looking for talented software developers who are driven to understand how complex systems work and enjoy solving challenging problems to join our diverse and growing team. As a Software Engineer on our Client Integrations team, you will be respo",
                    "twitter:image": "https://lever-client-logos.s3.amazonaws.com/b223b84f-8202-4cc5-8f26-b63b8e635cc1-1496968602742.png",
                    "twitter:title": "Blend - Software Engineer - Client Integrations",
                    "viewport": "width=device-width, initial-scale=1, maximum-scale=1"
                }
            ]
        },
        "snippet": "Prior industry experience as a software engineer (or domain knowledge in \nlending, though not required); Experience with Javascript, Node.js, Python or C#\n\u00a0...",
        "title": "Blend - Software Engineer - Client Integrations"
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
            print(web_data)

            data_to_send_in_request_body["description"] = web_data

            for data_key in data_to_send_in_request_body:
                # data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key].encode('UTF8').decode('utf-8')
                data_to_send_in_request_body[data_key] = data_to_send_in_request_body[data_key]

            #test print json formatted complete listing
            # print(data_to_send_in_request_body)
    
        response_per_post = requests.post(
            url=CODEFORCASH_BASE_URL+'/api/metum/create',
            data=data_to_send_in_request_body)
        
        with open('responseFromCodeforcash','ab+') as f:
            pickle.dump(response_per_post, f)

if __name__ == '__main__':
    save_gse_call_results(send_job_listings_to_codeforcash(get_job_listings_from_google()))

    # save_gse_call_results(send_job_listings_to_codeforcash(remove_non_ascii(get_job_listings_from_google())))

    # send_job_listings_to_codeforcash(return_value)
    # save_gse_call_results(return_value)

    # save_result_of_sending_job_listings_to_codeforcash(send_job_listings_to_codeforcash(return_value))

    # save_gse_call_results(get_job_listings_from_google())

    # save_result_of_sending_job_listings_to_codeforcash(
    #     get_job_listings_from_google())
        
