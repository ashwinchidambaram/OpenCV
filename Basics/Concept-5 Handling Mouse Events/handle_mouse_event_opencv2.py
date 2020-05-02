import numpy as np
import cv2

# -- Read what 'EVENT' type functions exist in cv2
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):

    # When left button clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' , ', y)

        font = cv2.FONT_HERSHEY_DUPLEX
        strXY = str(x) + ', ' + str(y)

        cv2.putText(img, strXY, (x, y), font, .5, (0, 255, 10), 2)

        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        font = cv2.FONT_HERSHEY_DUPLEX
        strXY = str(blue) + ', ' + str(green) + ', ' + str(red)

        cv2.putText(img, strXY, (x, y), font, .5, (102, 0, 75), 2)

        cv2.imshow('image', img)

img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()