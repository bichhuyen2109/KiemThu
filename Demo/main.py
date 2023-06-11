
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ex

driver = webdriver.Chrome(service=Service('venv/chromedriver.exe'))
driver.get('https://lms.ou.edu.vn/')

driver.find_element(By.CLASS_NAME, 'main-btn').click()
driver.find_element(By.CLASS_NAME, 'login100-form-btn').click()

user_type = Select(driver.find_element(By.ID, 'form-usertype'))
user_type.select_by_index(0)

username = driver.find_element(By.ID, 'form-username')
password = driver.find_element(By.ID, 'form-password')

username.send_keys('2051050172')
password.send_keys('khainguyenty')

driver.find_element(By.CLASS_NAME, 'm-loginbox-submit-btn').click()
#course-info-container-1764-6
course = WebDriverWait(driver, 15).until(ex.presence_of_all_elements_located((By.CSS_SELECTOR, 'a > span.multiline')))
# course = driver.find_elements(By.CSS_SELECTOR, 'a > spam.multiline')
for c in course:
    print(c.text)

driver.execute_script("windows.scrollto(0, 300)")
driver.save_screenshot("lms.png")

driver.quit()
