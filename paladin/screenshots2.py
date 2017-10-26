from selenium import webdriver
from time import sleep
import contextlib

@contextlib.contextmanager
def quitting(thing):
    yield thing
    thing.quit()

with quitting(webdriver.Firefox()) as driver:
    driver.implicitly_wait(10)
    driver.get('https://www.youtube.com/watch?v=aWyed-LWKgw')
    sleep(5)
    element = driver.find_element_by_id("placeholder-player")
    location = element.location
    size = element.size

    print (location,size)
    #driver.get_screenshot_as_file('screenshot.png')
    driver.get_screenshot_as_png()
    drive.
    driver.quit()