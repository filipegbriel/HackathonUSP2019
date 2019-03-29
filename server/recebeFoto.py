#! /usr/bin/python2
import sys

sys.path.append('/usr/local/lib/python2.7/dist-packages')

import socket
from PIL import Image
import socket
import base64
import time

size = 77324

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('192.168.43.2', 8000))
serv.listen(5)

print 'waiting for data tx'

#while True:
conn, addr = serv.accept()
from_client = ''
while True:
    data = conn.recv(size)
    if data :
        from_client += data
        print 'data received'
        conn.send("status: received\n")
        fh = open("tmp.jpg", "wb")
        fh.write(str(from_client).decode('base64'))
        fh.close()
        done = True
        time.sleep(size/100000)
        break
        
conn.close()
print 'client disconnected'

    
