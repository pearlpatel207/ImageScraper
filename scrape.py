import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup as bs
import os
import urllib
import requests

# Path to the folder for saving images
dir_path = 'images'

# Function to take an image url and save the image in the given directory
def download_image(url):
    print("[INFO] downloading {}".format(url))
    name = str(url.split('/')[-1])
    urllib.request.urlretrieve(url,os.path.join(dir_path, name))

# Function for infinite scroll. Change the value of n depending on the number of images you wish to scrape
def scroll(browser, n=20, sleep_time=4 ):
    for _ in range(n):
        browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(sleep_time)


driver = webdriver.Chrome(executable_path=r'PATH_TO_CHROME_DRIVER') #set path to the driver
driver.get('https://9gag.com/meme') # Set this to the desired URL

scroll(driver)

content = driver.page_source
soup = bs(content, 'html.parser')

posts = soup.findAll('div', class_='post-container')

links_list = []

for post in posts:
    image = bs(str(post), 'html.parser').img
    if image != None:
        if image['src'] not in links_list:
            links_list.append(image['src'])

# Function to take an image url and save the image in the given directory
def download_image(url):
    print("[INFO] downloading {}".format(url))
    name = str(url.split('/')[-1])
    urllib.request.urlretrieve(url,os.path.join(dir_path, name))

for img_link in links_list:
    download_image(img_link)
