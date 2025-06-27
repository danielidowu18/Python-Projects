import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
cookie_button = driver.find_element(by=By.ID, value="cookie")

n = 0
start_time = time.time()
while time.time() < (start_time + 300):
    cookie_button.click()
    
    if n % 5 == 0:
        available_boosters = driver.find_elements(by=By.CSS_SELECTOR, value="#store div:not(.grayed)")
        if len(available_boosters) > 0:
            available_boosters[-1].click()    
            # WebDriverWait(driver, 10).until((EC.element_to_be_clickable(available_boosters[-1]))).click()

    n += 1

cookie_per_sec = driver.find_element(by=By.XPATH, value='//*[@id="cps"]')
print(cookie_per_sec.text)