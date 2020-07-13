# pyshorteners

import pyshorteners

s = pyshorteners.Shortener()
url = "www.blahblahblah.com/blahblah/anotherblahblah"
print(s.tinyurl.short(url))
