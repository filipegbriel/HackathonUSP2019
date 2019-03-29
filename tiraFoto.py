#! /usr/bin/python2
import sys

sys.path.append('/usr/local/lib/python2.7/dist-packages')

import cv2
from PIL import Image
import time

#WebCam#
print ("initializing camera")
camera_port = 0
camera = cv2.VideoCapture(camera_port)
time.sleep(0.2)
n = 0
while (n < 5):
    return_value, imagem = camera.read()
    n=n+1
    #print (n)
del(camera)


cv2.imwrite("tmp.jpg", imagem)

print 'done'
