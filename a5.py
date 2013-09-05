import urllib2

url = "http://www.pythonchallenge.com/pc/def/banner.p"

page = urllib2.urlopen(url, timeout=10)
data = page.read()

import pickle
obj = pickle.loads(data)

for line in obj:
    print("".join(p[0]*p[1] for p in line))



