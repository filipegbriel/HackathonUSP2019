#! /usr/bin/python2
import sys

sys.path.append('/usr/local/lib/python2.7/dist-packages')

from PIL import Image
import socket
import base64
 
with open("tmp.jpg", "rb") as imageFile:
    foto_s = base64.b64encode(imageFile.read())
    
print foto_s[1]
file = open("tmp.txt","w") 
 
file.write(foto_s)  

file.close() 


 
