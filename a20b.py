import urllib2

auth = urllib2.HTTPBasicAuthHandler()
auth.add_password('pluses and minuses', 'www.pythonchallenge.com', 'butter', 'fly')
urllib2.install_opener(urllib2.build_opener(auth))
url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
req = urllib2.Request(url, headers={'Range': 'bytes=2123456789-'})
resp = urllib2.urlopen(req)
print resp.read()
