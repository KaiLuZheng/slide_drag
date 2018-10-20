#!/usr/bin/python3

import cv2
import numpy as np
import sys



def findplace():
    otemp = 'template.png' # block img little
    oblk = 'target.jpeg' # source img

    target = cv2.imread(otemp, 0)
    template = cv2.imread(oblk, 0)

    w, h = target.shape[::-1]

    bw, bh = template.shape[::-1]

    temp = 'temp.jpg'
    targ = 'targ.jpg'

    cv2.imwrite(temp, template)
    cv2.imwrite(targ, target)

    target = cv2.imread(targ)
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    target = abs(255 - target)
    cv2.imwrite(targ, target)

    target = cv2.imread(targ)
    template = cv2.imread(temp)

    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED) ##

    x, y = np.unravel_index(result.argmax(), result.shape)
    cv2.rectangle(template, (y, x), (y + w, x + h), (255, 255, 0), 2)
    cv2.imwrite('ok.jpeg', template)

    realpx = 55
    persent = realpx/w
    place = round(y*persent)
    print(y)
    print(place)
    return place

if __name__ == '__main__':
    findplace()

