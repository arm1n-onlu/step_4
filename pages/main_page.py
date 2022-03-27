from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.ID, "login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.ID, "login_link_invalid"), "Login link is not presented"

    def add_to_busket(self):
        busket_link = self.browser.find_element(By.ID, "add_to_basket_form")
        busket_link.click()

