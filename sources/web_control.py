import sys
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import keyboard as key


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(r"..\assets\chromedriver.exe", options=options)

def enter_meeting_with_web(dv, webex_address):
    dv.get(webex_address)
    key.send("RETURN")


def get_element(driver, find_method, value: str, time_out=10):
    try:
        found_element = WebDriverWait(driver, time_out).until(EC.presence_of_element_located((find_method, value)))
        print(value, " is ready!")
        return found_element
    except TimeoutException:
        print(value, " took too much time!")
        return None


if __name__ == "__main__":
    dv = get_driver()
    webex_address = r"https://meet143.webex.com/meet/pr26416942764"
    # have to hadle exception
    dv.implicitly_wait(10)
    dv.get(webex_address)
    print(dir(dv))
    key.send("RETURN")

    dv.find_element_by_id("push_download_join_by_browser").click()
    iframe = get_element(dv, "name", "thinIframe")
    dv.switch_to.frame(iframe)

    input_box = get_element(dv, By.CLASS_NAME, "style-input-33p0A")
    input_box.send_keys("_" + Keys.RETURN)
    
    try:
        # auto_selec = WebDriverWait(dv, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '')))
        container = WebDriverWait(dv, 10).until(EC.presence_of_element_located((By.ID, 'meetingSimpleContainer')))
        print("container: ", container)
        time.sleep(4)
        key.send("ESCAPE")
        auto_selec = dv.find_elements_by_tag_name('button')
        auto_selec[1].click()
        key.send("DOWN + RETURN")
        print("audio selection is ready!")
    except TimeoutException:
        print("audio selection loading took too much time!")

    btns = dv.find_elements_by_tag_name("button")
    print(btns)
    btns[0].click()
    # auto_selec = dv.find_elements_by_tag_name('button')[0].click()

    dv.switch_to.default_content()

        



"""
cli command for record screen
.\ffmpeg.exe -f dshow -i video="screen-capture-recorder" -f dshow -i audio="virtual-audio-capturer" output.mkv
"""
