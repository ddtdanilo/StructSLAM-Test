#!/usr/bin/env python

'''
Este programa detecta bordes de una trayectoria
seguida por el 'robot'
Usage:
  app.py [<video source>] (app.py video.avi)
  Trackbars controlan thresholds.
'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
from matplotlib import pyplot as plt

# built-in module
import sys

if __name__ == '__main__':
    print (__doc__)

    try:
        video = sys.argv[1]
    except:
        video = '/home/adminmecatronica/Escritorio/EC5801/vidELE3.mp4'

    def nothing(*arg):
        pass

    cv2.namedWindow('edge')
    cv2.createTrackbar('thrs1', 'edge', 1476, 5000, nothing)
    cv2.createTrackbar('thrs2', 'edge', 3400, 5000, nothing)

    # Capture video
    video = cv2.VideoCapture(video)

    while True:

        _, img = video.read()
        if (type(img) == type(None)):
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thrs1 = cv2.getTrackbarPos('thrs1', 'edge')
        thrs2 = cv2.getTrackbarPos('thrs2', 'edge')

        edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5, L2gradient=True)

        vis = img.copy()
        vis = np.uint8(vis/2.)
        vis[edge != 0] = (0, 255, 0)

        cv2.imshow('edge', vis)

        if (0xFF & cv2.waitKey(5) == 27) or img.size == 0:
            break

    cv2.destroyAllWindows()
    video.release()