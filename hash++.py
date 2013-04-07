import base64, binascii, httplib, random, time, urllib, os
 
r = random.SystemRandom()
while True:
    b = bytearray()
    for i in range(128):
        b.append(r.getrandbits(8))
    s = binascii.b2a_base64(b)
    h = httplib.HTTPConnection('almamater.xkcd.com')
    h.connect()
    h.request('POST', '/?edu=mit.edu', urllib.urlencode({'hashable': s}))
    re = h.getresponse()
    print '\n'+s+'\n', re.read()
    h.close()
