#! /usr/bin/python2
import sys

sys.path.append('/usr/local/lib/python2.7/dist-packages')

from PIL import Image
import socket
import base64
 
with open("tmp.jpg", "rb") as imageFile:
    foto_s = base64.b64encode(imageFile.read())
    

file = open("tmp.txt","w") 
 
file.write(foto_s)  

file.close() 

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(('192.168.43.223', 8080))

#c.connect(('0.0.0.0', 8080))
print 'sending :', len(foto_s), 'bytes'

for n in range(0, len(foto_s)):
    c.send(foto_s[n])
    print n

from_server = c.recv(4096)

c.close()

print from_server
