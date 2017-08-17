import urllib.request, urllib.parse, urllib.error
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(http://.*?)"', html)
for link in links:
    print(link.decode())

# doesnt work ??
# Enter - https://www.py4e.com/book.htm
# Traceback (most recent call last):
#   File "urlregex.py", line 11, in <module>
#     html = urllib.request.urlopen(url, context=ctx).read()
#   File "/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 223, in urlopen
#     return opener.open(url, data, timeout)
#   File "/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 532, in open
#     response = meth(req, response)
#   File "/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 642, in http_response
#     'http', request, response, code, msg, hdrs)
#   File "/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 570, in error
#     return self._call_chain(*args)
#   File "/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 504, in _call_chain
#     result = func(*args)
#   File "/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/urllib/request.py", line 650, in http_error_default
#     raise HTTPError(req.full_url, code, msg, hdrs, fp)
# urllib.error.HTTPError: HTTP Error 403: Forbidden
