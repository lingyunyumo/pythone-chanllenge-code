import xmlrpclib
url = 'http://www.pythonchallenge.com/pc/phonebook.php'
phonebook = xmlrpclib.Server(url)
evil = phonebook.phone('Bert')
print(evil)
