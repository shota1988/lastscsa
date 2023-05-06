from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
import  allure
from Locators.testl import loc

class Main_Step(loc):
    def __init__(self):
        self.driver = None

    @allure.step
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://the-internet.herokuapp.com/")

    @allure.step
    def open_upload_file(self):
        self.driver.find_element(*loc.upload).click()

    @allure.step
    def upload_file(self):
        file_path = os.path.abspath("qa.png")
        self.driver.find_element(*loc.file_up).send_keys(file_path)

    @allure.step
    def submit_upload_file(self):
        self.driver.find_element(*loc.submit).submit()

    @allure.step
    def check_uploaded_file(self):
        return self.driver.page_source.find(*loc.checker)

    @allure.step
    def tearDown(self) -> None:
        self.driver.close()