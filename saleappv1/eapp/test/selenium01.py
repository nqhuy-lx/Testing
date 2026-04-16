from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='../../.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://vnexpress.net/kinh-doanh/chung-khoan")
driver.execute_script('window.scrollTo(0, 300)')
driver.implicitly_wait(5)

articles = driver.find_elements(By.CSS_SELECTOR, '#automation_TV0 article')
print(len(articles))
for a in articles:
    text = a.find_element(By.TAG_NAME, 'h2')
    img = a.find_element(By.CSS_SELECTOR, ' div > a > picture > img')
    print(text.text)
    print(img.get_attribute("src"))
    print("=========================")

driver.quit()