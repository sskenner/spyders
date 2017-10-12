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

# INSERT GOOGLE SEARCH ENGINE TOKEN SETS HERE ######################
AVAILABLE_TOKEN_SETS = {
    'c4c': {
        'api_key': 'XXXXXXXXXXXXXXXXXX:XXXXXXX',
        'cse_id': 'XXXXXXXXXXXXXXXXXX:XXXXXXX'
    }
    # uncomment for additional token set
    # ,
    # 'c4c2': {
    #     'api_key': 'XXXXXXXXXXXXXXXXXX:XXXXXXX,
    #     'cse_id': 'XXXXXXXXXXXXXXXXXX:XXXXXXX'
    # }
}

NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN = 'c4c'

API_KEY_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['api_key']
CSE_ID_TO_USE_FOR_THIS_RUN = AVAILABLE_TOKEN_SETS[NAME_OF_TOKEN_SET_TO_USE_FOR_THIS_RUN]['cse_id']

CODEFORCASH_BASE_URL = 'https://i.codefor.cash'
CODEFORCASH_API_KEY = '5b26197b391c5dab05c5606d43fba9c6'

MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY = 10

skills = ["ruby","rails"," php","ruby on rails"," css","heroku"," aws","python","javascript"," sql","scraping","statistics","scraper","scripting","automate","data analy","data visual","crawl"," api","analytics","aws","html5","html","css","bootstrap","twilio","node","devops","mysql","mongodb","postgresql","wordpress","blogging","writing","laravel","codeigniter","mongo","postgres","sqlite","leveldb","firebase","neo4j","redis","jquery","nodejs","angular","express","vuejs","node.js","chat bot"," vue","webpack","github","stripe"," bot",".net","dot net"," c# ","react","asp.net","r studio","machine learning","react native"," nlp","apache spark","business intelligence"," d3 ","dataviz","hadoop","hbase","hive","kafka","matlab","mssql","powerbi","predictive analytics","quant","quantitative finance","scala","tableau"," vba","backbonejs","deployment","responsive","smtp","interactive brokers","ipsec","openbsd","twisted","bash","numpy","xmlrpc","qmail","dovecot","mailfront","rblsmtpd","djbdns","daemontools","golang"," c++","arduino","lambda","ansible","blockchain","ethereum","cryptocurrency","crypto-currency","bitcoin","docker","startup"," cto ","prototype","minimum viable product","automation"," qa ","java","rspec","phantomjs","selenium","cucumber","junit"," wcf","rest assured","rest-assured","nunit","jmeter"," ios","swift","objectivec","objective-c","objective c","admob","mobile","dotnet"," c ","full stack","windows services","azure","cloud","disaster recovery","business continuity","virtual it","web design","video","video editing","video editor","animation","flexbox","apache","typescript","rxjs","ecmascript","redux","babel","jekyll","nginx"," npm","gulp","grunt","sdssf","meteor","digital ocean","serverless"," bpm","process improvement","digital transformation","workflow","xamarin","project management","unity3d","unity","game programming","android","intern","freelance","angular2","spring","hibernate","cofounder","systems","linux","sysadmin","database","ember","ember.js","emberjs","data scientist","deep learning","unix"," qnx","embedded"," git","pandas","svr4"," aix","powerpc"," avr","emacs","lisp","shell"," iot","braintree","reactjs","browser","landing","knockout","kockout.js","web development","web app","website","web application","remote","part-time","knockoutjs","contract","kockout","d3js","d3.js","data visualization","woocommerce","visualcomposer","avada","eventscalendar","listify","xcode","scenekit","uikit","cocoapods","albanian","react-native","webdevelopment"," web","development","web-design"," es6","adwords","youtube"," ppc","google analytics","paid search","facebook ads","flask","django","symfony","haskell","functional programming","fullstack","full-stack"," f# ","start up","reflex-frp"," coq","framework","native","mobile app","mockups","mock-ups","mock ups","wire frames","wireframes","css3","es2016","react.js","front-end developer","react js"," js "," es7"," es8","es2015","es2017"," ts ","electron","cordova","blueprintjs","onsen","onsenui","reactnative",".net core","coreos","centos","rhel","red hat","redhat","ubuntu","debian","apache2","haproxy","kubernetes","docker swarm","node js","pascal","delphi","cobol","webapi","aurelia"," mvc","materialize","internet of things","maker","mean","software development","php7","nosql","data","data analysis","data mining","data architecture","database architecture","data warehouse","etl scripts"," etl","oracle","jenkins","architecture","microservices","continuous integration","logi","salesforce.com","wireframing","entry-level","critical-thinking","innovator","junior","frontend","material","worldpress","vue.js","sass","vuex","shopify","openstack"," ovh","vue","pyramid","sinatra","haxe","openfl","vertx","game servers","java8","mobile app development","apps","software","hardware"," mvp","watchos","tvos","macos","kotlin","objc","carthage","scss","rest api","website design","maintenance","user","interface","backend","clojure","clojurescript"," ux ","hack","sketch","ui/ux","rxswift","reactivecocoa"," frp"," wpf","windows client","kiosk","touchscreen","angularjs","aureliajs","ravendb","flux","angular 2","design","websites","develop","photoshop","healthcare","microservice"," s3 ","application","portfolio"," c9 ","sublime","nixos"," cto"," htm","numenta","datomic","play","restful","garden","generation","front end"," ai ","sikulix","generative","load","repl-driven-development","taxonomy","relational","theory","distributed","akka"," go ","blocks"," csp","communicating-sequential-processes","regex","om-next","boot","marketing","illustrator","user interface"," app","back end","rudy"," ui ","digital marketing","google maps","ecommerce","web dev"," mac","back-end","commerce","science","terminal","divi","ajax","rest","rabbitmq","senior","architect","chef","agile","joomla","minimal","salesforce","front-end","jupyter notebook","mailgun","j2ee","less","websockets"," xml","ionic"," r ","cakephp","excel","office","t-sql","entity framework","git hub","sql server 2014","visual studio 2015","adobe photoshop","elasticsearch","search","backbone","html/css","phonegap","alexa","dynamodb","meteor.js"," ror","angular.js","magento","drupal","moodle","elearning","webdesign","socialmediamarketing","digitalmarketing","training","coaching"]

def do_google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    print('<<<< CSE Query Loop >>>>')
    print(res['queries']['request'][0]['startIndex'], 'CSE Start Index')
    print(res['queries']['request'][0]['totalResults'], 'CSE Query Results')

    if res['queries']['request'][0]['totalResults'] == '0':
        # # # prints when reach the gse page where totalResults == '0'
        print('@@@@ NO CSE QUERY RESULTS @@@@')
        # print(res)
        return res['items']
    else:
        return res['items']


# set gse query parameters to iterate through results
def get_job_listings_from_google(cse_search_term, number_of_listings_to_get):
    return_value = []
    for search_result_number_from_which_api_query_results_start in range(1, number_of_listings_to_get + 1, MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY):
        try:
            return_value.extend(do_google_search(
                search_term=cse_search_term,
                api_key=API_KEY_TO_USE_FOR_THIS_RUN, cse_id=CSE_ID_TO_USE_FOR_THIS_RUN,
                num=MAXIMUM_NUMBER_OF_SEARCH_RESULTS_PER_GOOGLE_API_QUERY, start=search_result_number_from_which_api_query_results_start))
        except:
            print(len(return_value), 'Listings + Empty Index')
            return return_value[:number_of_listings_to_get]
    return return_value[:number_of_listings_to_get]

def save_gse_call_results(listings):
    print('@@@@', len(listings), 'Listings Saved @@@@')
    # save gse results as a file
    with open('./saved_files/saved_gse_results.txt','a+') as f:
        f.write(json.dumps(listings))

def save_print_log(data):
    # save post metrics as file
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
                time.sleep(2)
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
            else:
                data_to_send_in_request_body["remote_ok"] = 'doesnt_say'

            count += 1

        print("*********************************************")
        save_print_log("*********************************************")

        # # test print json formatted complete listing
        # print(data_to_send_in_request_body)

        # send formatted json to code4cash api
        response_per_post = requests.post(
            url=CODEFORCASH_BASE_URL+'/api/metum/create',
            data=data_to_send_in_request_body)
        # save code4cash response
        print(response_per_post)
        with open('./saved_files/saved_C4C_response','ab+') as f:
            pickle.dump(response_per_post, f)

        # save prePostListings before post to c4c
        with open('./saved_files/saved_post_data.txt','a+') as f:
            f.write(json.dumps(data_to_send_in_request_body))

    print('XXXX', count, 'Listings Posted XXXX')
    save_print_log(count)
    save_print_log("*********************************************")

if __name__ == '__main__':
    # send_job_listings_to_codeforcash(get_job_listings_from_google())
    for skill in skills:
        print('**** ROOT:', skill, '****')
        send_job_listings_to_codeforcash(get_job_listings_from_google("site:jobs.lever.co/ " + skill, 101))
