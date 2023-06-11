from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

kw = input('Nhập sản phẩm: ')

driver = webdriver.Chrome(service=Service('venv/chromedriver.exe'))
driver.get('https://tiki.vn/')

sp = driver.find_element(By.CLASS_NAME, 'FormSearchStyle__InputRevamp-sc-1idbenb-5')
sp.send_keys(kw)

driver.find_element(By.CLASS_NAME, 'FormSearchStyle__ButtonRevamp-sc-1idbenb-6').click()
# driver.find_element(By.CLASS_NAME, 'style__StyledItem-sc-18svp8n-0 fkDgwT').click()

driver.quit()
