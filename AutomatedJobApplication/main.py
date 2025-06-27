from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


USERNAME = "danielidowu100@gmail.com"
PASSWORD = "Daniel@love100"
PHONE = "09133476365"

driver = webdriver.Chrome()
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3732435164&f_AL=true&f_E=1%2C2&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
    )


login = driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
login.click()
time.sleep(3)
username_input = driver.find_element(by=By.ID, value="username")
password_input = driver.find_element(by=By.ID, value="password")
sign_in_button = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
sign_in_button.click()

time.sleep(2)
jobs_list = driver.find_elements(by=By.CSS_SELECTOR, value=".scaffold-layout__list-container .disabled.ember-view.job-card-container__link.job-card-list__title")
if len(jobs_list) > 0:
    for job in jobs_list:
        print(job.text)
        time.sleep(2)
        job.click()
        time.sleep(2)
        try:
            easy_apply_button = driver.find_element(by=By.CSS_SELECTOR,
                                                    value=".jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view")
            # print(easy_apply_button.get_attribute("id"))
            easy_apply_button.click()
            time.sleep(1)
            phone_number_input = driver.find_element(by=By.CSS_SELECTOR, value=".artdeco-text-input--container.ember-view .artdeco-text-input--input")
            # print(phone_number_input.get_attribute("id"))
            
            for _ in range(15):
                phone_number_input.send_keys(Keys.BACKSPACE)
            phone_number_input.send_keys("09133476365")
            submit_application = driver.find_element(by=By.CLASS_NAME, value="artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
            if submit_application.get_attribute("aria-label") == "Submit application":
                submit_application.click()
                close_add_skill = driver.find_element(by=By.CLASS_NAME, value="artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--2.artdeco-button--tertiary.ember-view artdeco-modal__dismiss")
                close_add_skill.click()
                print("Applied Successfully.")
            else:
                close_application = driver.find_element(by=By.CLASS_NAME, value="artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--2.artdeco-button--tertiary.ember-view.artdeco-modal__dismiss")
                close_application.click()
                confirm_close = driver.find_element(by=By.CLASS_NAME, value="artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view.artdeco-modal__confirm-dialog-btn")
                confirm_close.click()
                print("Unsuccessfull, Too many steps.")
        except NoSuchElementException:
            print("No application button, skipped.")
            continue
        

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(sign_in_button)).click()

time.sleep(5)
driver.quit()