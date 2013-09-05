import urllib2
import re

auth = urllib2.HTTPBasicAuthHandler()
auth.add_password('pluses and minuses', 'www.pythonchallenge.com',
    'butter', 'fly')
urllib2.install_opener(urllib2.build_opener(auth))
url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
req = urllib2.Request(url)
start = 2123456789
req.add_header('Range', '')
while start:
    req.headers['Range'] = 'bytes=%i-' % (start)
    resp = urllib2.urlopen(req)
    print(start, resp.read())
    start -= 1



