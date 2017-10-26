from selenium import webdriver
from time import sleep




from PIL import Image


site = "https://www.youtube.com/watch?v="
video = "yfdKc4JM0BY"
timing="?t=15s"

fox = webdriver.Firefox()
fox.implicitly_wait(10)

fox.get(site+video+timing)
#fox.get('http://stackoverflow.com/')
sleep(30)
# now that we have the preliminary stuff out of the way time to get that image :D
#element = fox.find_element_by_id('placeholder-player') # find part of the page you want image of

element = fox.find_element_by_css_selector('div.player-api.player-width.player-height') # find part of the page you want image of
#player-api player-width player-height
location = element.location
size = element.size
fox.save_screenshot(video+'.png') # saves screenshot of entire page
fox.quit()

im = Image.open(video+'.png') # uses PIL library to open image in memory

left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

im = im.crop((left, top, right, bottom)) # defines crop points
im.save(video+'.png') # saves new cropped image