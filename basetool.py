#!/usr/bin/python3

import urllib
import urllib.request

import logging

headers = {}
headers['User-Agent'] ='Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; da-dk) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'


def saveAs(url, filename):
    req = urllib.request.Request(url, headers = headers)
    res = urllib.request.urlopen(req)
    bhtml = res.read()
    with open(filename, 'wb') as f:
        f.write(bhtml)
    logging.debug('save as %s ok.'%filename)



def get_track(distance):
    track = []    
    current = 0
    mid = distance * 3 / 4
    t = 0.2
    v = 0
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a*t
        dx = v0*t + 1/2 *a*t*t
        current += dx
        track.append(round(dx))
    return track




