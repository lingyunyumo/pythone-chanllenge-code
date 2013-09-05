import urllib2

nothing = '12345'
baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

while(1):
    page = urllib2.urlopen(baseurl+nothing, timeout=10)
    nothing = page.read().split(' ')[-1]
    print(nothing)


