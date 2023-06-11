from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

date_input = input("Nhập ngày tháng năm (dd-mm-yyyy): ")
number = int(input("Nhập số của bạn: "))

driver = webdriver.Chrome(service=Service('venv/chromedriver.exe'))
driver.get('https://www.xskthcm.com/')
driver.find_element(By.CLASS_NAME, 'select2-container').click()

ul_result = driver.find_element(By.CLASS_NAME, 'select2-results')
li_elements = ul_result.find_elements(By.CSS_SELECTOR, 'li')

for item in li_elements:
    div = item.find_element(By.TAG_NAME, 'div')
    print(div.text)
    if div.text == date_input:
        item.click()
        #lưu ảnh
        screenshot = driver.get_screenshot_as_png()
        filename = f"{date_input}.png"
        with open(filename, "wb") as f:
            f.write(screenshot)
        #lấy dữ liệu từ table
        table = driver.find_element(By.CLASS_NAME, 'table-bordered')
        #bỏ qua dòng dầu nha
        rows = table.find_elements(By.TAG_NAME, "tr")[1:]
        results = {}
        #duyệt hàng nè
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            #nếu cột == 2 rồi thì mới làm vì nó 2 cột lận
            if len(cols) == 2:
                prize = cols[0].text
                numbers = cols[1].text
                if "-" in numbers:
                    #này là lấy số trúng ra do nó có định dạng -
                    numbers = numbers.replace("-", ", ")
                    #in ra theo định dạng của thầy
                print(f"{prize}: {numbers}")
                #này là lấy các số cắt và convert sang int bỏ vào directory
                results[prize] = set(map(int, numbers.split(", ")))
        # So sánh với kết quả xổ số
        matched = False
        for prize, numbers in results.items():
            if number in numbers:
                print(f"Bạn đã trúng giải {prize}")
                matched = True
                break
        if not matched:
            print("Chúc bạn may mắn lần sau!")

        break

time.sleep(5)
driver.quit()




