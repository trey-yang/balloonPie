#!/usr/bin/env python2

from picamera import PiCamera
import time
import datetime
import sys

STDERR = sys.stderr
def excepthook(*args):
    print >> STDERR, 'caught'
    print >> STDERR, args

sys.excepthook = excepthook


# new camera instance
camera = PiCamera()

# take pic
camera.start_preview(alpha=240)
time.sleep(3)
camera.capture('/home/pi/dev/balloonPie/camera/pics/'+str(datetime.datetime.today())+".jpg")
camera.stop_preview()


#EOF
