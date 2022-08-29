from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

url = 'https://www.youtube.com/c/JohnWatsonRooney/videos?view=0&sort=p&flow=grid'

driver =webdriver.Chrome()

driver.get(url)

videos = driver.find_elements(by=By.CLASS_NAME, value='style-scope ytd-grid-video-renderer')

for video in videos:
    title = video.find_element(by=By.XPATH, value='.//*[@id="video-title"]').text
    views = video.find_element(by=By.XPATH, value='.//*[@id="metadata-line"]/span[1]').text
    when = video.find_element(by=By.XPATH, value='.//*[@id="metadata-line"]/span[2]').text
    print(title, views, when)