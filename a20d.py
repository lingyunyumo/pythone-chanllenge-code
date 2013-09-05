import urllib2
from cStringIO import StringIO

auth = urllib2.HTTPBasicAuthHandler()
auth.add_password('pluses and minuses', 'www.pythonchallenge.com',
    'butter', 'fly')
urllib2.install_opener(urllib2.build_opener(auth))
url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
req = urllib2.Request(url)
req.add_header('Range', 'bytes=1152983631-')
resp = urllib2.urlopen(req)

with open('a20.zip', 'wb') as f:
    f.write(resp.read())




