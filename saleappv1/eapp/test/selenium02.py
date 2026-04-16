from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='../../.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://tiki.vn/do-choi-me-be/c2549")
driver.execute_script('window.scrollTo(0, 300)')
driver.implicitly_wait(5)

products = driver.find_elements(By.CSS_SELECTOR, 'a.product-item')
print(len(products))
links = []
for p in products[:5]:
    text = p.find_element(By.CSS_SELECTOR, 'span > div.content > div.info > div.sc-68e86366-4.cqgHDv > div:nth-child(1) > h3')
    href = p.get_attribute('href')
    print(text.text)
    print(href)
    links.append(href)
    print("=========================")

for l in links:
    driver.get(l)
    driver.execute_script('window.scrollTo(0, 3500)')
    driver.implicitly_wait(3)
    print("link: " + l)
    comments = driver.find_elements(By.CSS_SELECTOR, 'div.customer-reviews__inner > div.review-comment')
    print(len(comments))
    for c in comments:
        elements = c.find_elements(
            By.CSS_SELECTOR,
            f'div:nth-child(2) > div.review-comment__content'
        )

        if elements:
            text = elements[0].text.strip()
            if text:
                print(text).

            else:
                print("Empty content")
        else:
            print("Element not found")

driver.quit()