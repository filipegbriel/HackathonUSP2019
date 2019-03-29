#! /usr/bin/python2
import sys

sys.path.append('/usr/local/lib/python2.7/dist-packages')

import time

delta = 60 * 1 #seconds

while True :
    execfile("tiraFoto.py")
    execfile("enviaFoto.py")    
    time.sleep(delta)

    
        
            
