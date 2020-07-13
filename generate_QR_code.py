# qrcode

import qrcode

data = 'https//www.google.com'
filename = "web.png"
img = qrcode.make(data)
img.save(filename)
