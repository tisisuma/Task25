from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class imdb:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def booting_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True
        except:
            print("ERROR : Unable to run the code !")
            return False

    def shutdown(self):
        self.driver.quit()

    def imdb(self):
        input_locator = "/html/body/div[2]/nav/div[2]/div[1]/form/div[2]/div/input"
        search_locator = '/html/body/div[2]/nav/div[2]/div[1]/form/button/svg/path[2]'
        dropdown = '//span[text()="All"]'
        dropdownvalues_locator = "/html/body/div[2]/nav/div[2]/div[1]/form/div[1]/div/label/span"

        try:
            self.driver.implicitly_wait(30)
            element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, dropdown)))
            element.click()
            self.driver.find_element(by=By.XPATH, value=dropdownvalues_locator).click()
            self.driver.find_element(by=By.XPATH, value=input_locator).send_keys(moviename)
            self.driver.implicitly_wait(30)
            self.driver.find_element(by=By.XPATH,value=search_locator).click()
        except NoSuchElementException as e:
            print("Error : ", e)


url = "https://www.imdb.com/search/name/"
moviename= "KGF"

execute = imdb(url)
execute.booting_function()
execute.imdb()
execute.shutdown()