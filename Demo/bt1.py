from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

nt = input("Nhập ngày tháng năm theo định đạng (dd-mm-yyyy): ")
s = int(input("Nhập số của bạn: "))

driver = webdriver.Chrome(service=Service('venv/chromedriver.exe'))
driver.get('https://www.xskthcm.com/')

driver.find_element(By.CLASS_NAME, 'select2-container').click()

ul = driver.find_element(By.CLASS_NAME, 'select2-results')
lis = ul.find_elements(By.CSS_SELECTOR, 'li')

for li in lis:
    div = li.find_element(By.TAG_NAME, 'div')
    print(div.text)
    if div.text == nt:
        li.click()
        screenshort = driver.get_screenshot_as_png()
        filename = f"{nt}.png"
        with open(filename, "wb") as f:
            f.write(screenshort)
        table = driver.find_element(By.CLASS_NAME, 'table-bordered')
        rows = table.find_elements(By.TAG_NAME, "tr") [1:]
        results = {}
        for row in rows:
            td = row.find_elements(By.TAG_NAME, "td")
            if len(td) == 2:
                giai = td[0].text
                so = td[1].text
                if "-" in so:
                    so = so.replace("-", ", ")
                print(f"{giai}: {so}")
                results[giai] = set(map(int, so.split(", ")))
        check = False
        for giai, so in results.items():
            if s in so:
                print(f"Chúc bạn đã đạt giải {giai}")
                check = True
                break
        if not check:
            print("Chúc bạn may mắn lần sau")

        break

driver.quit()
