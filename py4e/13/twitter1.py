import urllib.request, urllib.parse, urllib.error
import twurl
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if(len(acct) < 1): break
    url = twurl.augment(TWITTER_URL, {
        'screen_name': acct, 'count': '2'})
    print('Retrieving', url)
    html = urlopen(url, context=ctx).read()
    req = urllib.request.Request(acct, headers={'User-Agent': 'Mozilla/5.0'})
    connection = urllib.request.urlopen(html, context=ctx)
    data = connection.read().decode()
    print(data[:250])
    headers = dict(connection.getheaders())
    # print headers
    print('Remaining', headers['x-rate-limit-remaining'])
