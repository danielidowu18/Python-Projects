from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://tinder.com/")



time.sleep(5)
driver.quit()