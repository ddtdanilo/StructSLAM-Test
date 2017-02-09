import cv2
import numpy as np
from matplotlib import pyplot as plt

video = '/home/adminmecatronica/Escritorio/EC5801/vidELE3.mp4'
thrs1 = 1476
thrs2 = 3400


# Capture video
video = cv2.VideoCapture(video)

while True:
    _, img = video.read()

    if (type(img) == type(None)):
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5, L2gradient=True)
 
    print edge

    vis = img.copy()
    vis = np.uint8(vis/2.)
    vis[edge != 0] = (0, 255, 0)

    cv2.imshow('Edge detection', vis)

    if (0xFF & cv2.waitKey(5) == 27) or img.size == 0:
        break

cv2.destroyAllWindows()
video.release()