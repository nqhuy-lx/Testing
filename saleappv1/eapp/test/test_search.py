import time

from selenium.webdriver.common.by import By

from eapp.test.pages.HomePage import HomePage
from eapp.test.test_base import driver, test_app

def test_search(driver):
    home = HomePage(driver=driver)
    home.open_page()
    kw = 'iP'
    home.search(kw)
    time.sleep(1)
    rs = driver.find_elements(By.CSS_SELECTOR, '.card-body h4')

    assert all(kw in r.text for r in rs)

def test_order(driver):
    home = HomePage(driver=driver)
    home.open_page()
    home.order()
    time.sleep(1)
    rs = driver.find_element(By.CLASS_NAME, 'cart-counter')

    assert int(rs.text) == 3