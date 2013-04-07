from httplib2 import Http
from urllib import urlencode
import string
import random
import sys
h = Http()
while True:
  hash = "".join(random.sample(string.digits+string.letters, 62))
	print hash
	resp, content = h.request("http://almamater.xkcd.com/?"+"edu=mit.edu","POST",urlencode(dict(hashable=hash)))
	print(content)
