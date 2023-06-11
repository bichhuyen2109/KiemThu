from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

kw = input("Nhap tu khoa = ")

driver = webdriver.Chrome(service = Service('venv/chromedriver.exe'))
driver.get('https://www.google.com/')

el = driver.find_element(By.NAME, 'q')
el.send_keys(kw)
el.submit()

results = driver.find_elements(By.CSS_SELECTOR, '.g h3')

for r in results:
    print(r.text)

driver.quit()