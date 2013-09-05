import urllib2
import re

auth = urllib2.HTTPBasicAuthHandler()
auth.add_password('pluses and minuses', 'www.pythonchallenge.com',
    'butter', 'fly')
urllib2.install_opener(urllib2.build_opener(auth))
url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
range = re.compile('bytes (\d+)-(\d+)/(\d+)').search
req = urllib2.Request(url)
resp = urllib2.urlopen(req)
start, end, length = [int(i)
    for i in range(resp.info()['content-range']).groups()]
req.add_header('Range', '')
while end:
    req.headers['Range'] = 'bytes=%i-' % (end + 1)
    resp = urllib2.urlopen(req)
    print(resp.read())
    start, end, length = [int(i)
    for i in range(resp.info()['content-range']).groups()]


