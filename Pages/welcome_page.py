import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class welcome_page():

    def __init__(self,driver):
        self.driver = driver
        self.search_locator = "gh-ac"
        self.advanced_locator = self.driver.find_element(By.ID, "gh-as-a")

    def search_for_item(self,item_to_search):
        ps5_videogame = self.driver.find_element(By.ID, self.search_locator)
        ps5_videogame.click()
        time.sleep(3)
        ps5_videogame.send_keys(item_to_search)
        ps5_videogame.send_keys(Keys.RETURN)

    def search_for_item_xbox(self, item_to_search):
        xbox_videogame = self.driver.find_element(By.ID, self.search_locator)
        xbox_videogame.click()
        time.sleep(3)
        # Type "XBOX SERIES X video game digital" in the search, and press ENTER #HOMEPAGE
        xbox_videogame.send_keys(item_to_search)
        xbox_videogame.send_keys(Keys.RETURN)
        # Clicking the advanced search #HOMEPAGE
    def click_advanced(self):
        advanced = self.driver.find_element(By.ID, "gh-as-a")
        advanced.click()
        time.sleep(3)