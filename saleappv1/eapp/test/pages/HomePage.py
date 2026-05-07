from selenium.webdriver.common.by import By

from eapp.test.pages.BasePage import BasePage


class HomePage(BasePage):
    URL = 'http://127.0.0.1:5000/'

    INPUT_SEARCH = (By.CSS_SELECTOR, '#collapsibleNavbar > form > input')
    BTN_SEARCH = (By.CSS_SELECTOR, '#collapsibleNavbar > form > button')
    ORDER_BTN_1 = (By.CSS_SELECTOR, 'body > section > div > div:nth-child(1) > div > div > button')
    ORDER_BTN_2 = (By.CSS_SELECTOR, 'body > section > div > div:nth-child(2) > div > div > button')

    def open_page(self):
        self.open(self.URL)

    def search(self, kw):
        self.typing(*self.INPUT_SEARCH, kw)
        self.click(*self.BTN_SEARCH)

    def order(self):
        self.click(*self.ORDER_BTN_1)
        self.driver.implicitly_wait(1)
        self.click(*self.ORDER_BTN_1)
        self.driver.implicitly_wait(1)
        self.click(*self.ORDER_BTN_2)
        self.driver.implicitly_wait(1)
