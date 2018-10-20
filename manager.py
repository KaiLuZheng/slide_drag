#!/usr/bin/python3

from reqcore import selereq
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time
import logging
import sys

from basetool import saveAs
from basetool import get_track
from findblock import findplace

qqnews = selereq()
qqnews.get_openurl('http://news.qq.com/')

print('wait one key...')
locator = EC.presence_of_element_located((By.ID, 'onekey'))
element = qqnews.wait_EC_locator(locator)
element.click()

print('find login_frame')
locator = EC.presence_of_element_located((By.ID, 'login_frame'))
login_frame = qqnews.wait_EC_locator(locator)
print('turn to login_frame')
qqnews.switch2frame(login_frame)
element = qqnews.element_by_id('switcher_plogin')
element.click()

print('wait username block')
locator = EC.presence_of_element_located((By.ID, 'u'))
qqnews.wait_EC_locator(locator)


# wrong way
qqnews.sendkeys_byid('u', '123456')
qqnews.sendkeys_byid('p', 'cccccc')

print('click login button')
login_button = qqnews.element_by_id('login_button')
login_button.click()
time.sleep(2)

print('check ok or return ')
qqnews.switch2upper()
username = qqnews.element_by_id('userName')
if username.text == '':
    qqnews.switch2frame(login_frame)
else:
    print(username.text)
    qqnews.quit()
    sys.exit()


# slide ! work #
print('login error. slide work')
try:
    slide_iframe = qqnews.element_by_xpath('//iframe')
    qqnews.switch2frame(slide_iframe)

    '''
    with open('temp.html', 'w') as f:
        f.write(qqnews.check_source())
    qqnews.quit()
    sys.exit()
    '''

except Exception as e:
    logging.error('error: %s'%e)
    qqnews.quit()
    sys.exit()


print('find button')
drag_button = 'tcaptcha_drag_button'
locator = EC.presence_of_element_located((By.ID, drag_button))
qqnews.wait_EC_locator(locator)

try:
    button = qqnews.element_by_id(drag_button)
except Exception as e:
    logging.error('error: %s'%e)
    qqnews.quit()
    sys.exit()


print('do while ')
while True:
    isOk = False
    offset = 5
    times = 0


    slideBlock_url = qqnews.element_by_id('slideBlock').get_attribute('src')
    saveAs(slideBlock_url, 'template.png')
    time.sleep(1)
    bkg_url = qqnews.element_by_id('slideBkg').get_attribute('src')
    saveAs(bkg_url, 'target.jpeg')
    distance = findplace() + 5

    while True:
        action = qqnews.openerAction()

        while True:
            try:
                action.click_and_hold(button).perform()
                break
            except Exception as e:
                print('fuck ad absolute.')
                time.sleep(1)
                continue

        action.reset_actions()
        print('now distance: ', distance)

        track = get_track(distance)
        for i in track:
            action.move_by_offset(xoffset = i, yoffset = 0).perform()
            action.reset_actions()

        time.sleep(0.5)
        action.release().perform()
        time.sleep(5) # need moves

        if qqnews.check_byclass('tcaptcha-title') is True:
            tmp_url = qqnews.element_by_id('slideBlock').get_attribute('src')
            if slideBlock_url == tmp_url:
                pass
            else:
                print('img changed.')
                break

            times += 1 
            if times > 5 :
                break

            distance -= offset
            print('wrong place, again')
        else:
            print('do ok!')
            isOk = True
            break


    if isOk is True:
        break

qqnews.switch2upper()
qqnews.check_source()


time.sleep(5)
qqnews.quit()
