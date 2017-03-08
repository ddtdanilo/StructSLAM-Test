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
        video = 'vidELE3.mp4'

    def nothing(*arg):
        pass

    cv2.namedWindow('edge')
    cv2.createTrackbar('thrs1', 'edge', 800, 5000, nothing)
    cv2.createTrackbar('thrs2', 'edge', 800, 5000, nothing)

    # Capture video
    video = cv2.VideoCapture(video)

    while True:

        _, img = video.read()
        if (type(img) == type(None)):
            break
      #  img = cv2.imread("hall.jpg")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thrs1 = cv2.getTrackbarPos('thrs1', 'edge')
        thrs2 = cv2.getTrackbarPos('thrs2', 'edge')

        edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5, L2gradient=True)

        lines = cv2.HoughLines(edge,1,np.pi/180,200)
     
        if lines != None:
            for i in range(0,len(lines)):
                rho = lines[i][0][0]
                theta = lines[i][0][1]
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                
                if theta > 170*np.pi/180 or theta < 10*np.pi/180:
                    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
                elif theta > 80*np.pi/180 and theta < 100*np.pi/180:
                    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
                else:
                    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
                     

        #vis = img.copy()
        #vis = np.uint8(vis/2.)
        #is[edge != 0] = (0, 255, 0)

        cv2.imshow('edge', img)

        if (0xFF & cv2.waitKey(5) == 27) or img.size == 0:
            break

    cv2.destroyAllWindows()
    video.release()