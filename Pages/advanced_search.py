import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# TEST 1 - LOOKING FOR PS5 VIDEO GAMES (HOMEPAGE/ADVANCEDSETTINGS/)

# Writing video game in the search #HOMEPAGE

class advanced_search():
    def __init__(self, driver):
        self.driver = driver

    def advanced_filters(self):
        # Selecting the Video game category #ADVANCEDSETTINGS
        Category = self.driver.find_element(By.ID, "s0-1-17-4[0]-7[3]-_sacat")
        select_category = Select(Category)
        select_category.select_by_index(33)

        # Looking for only "Buy it now" Items #ADVANCEDSETTINGS
        Buy_now = self.driver.find_element(By.ID, "s0-1-17-6[3]-[2]-LH_BIN")
        Buy_now.click()

        # Making sure the items shown are New #ADVANCEDSETTINGS
        New = self.driver.find_element(By.ID, "s0-1-17-6[4]-[0]-LH_ItemCondition")
        New.click()

        # Includes free shipping #ADVANCEDSETTINGS
        Free_shipping = self.driver.find_element(By.ID, "s0-1-17-5[6]-[0]-LH_FS")
        Free_shipping.click()

        # Limiting the cost #ADVANCEDSETTINGS
        item_price = self.driver.find_element(By.ID, "s0-1-17-5[2]-[0]-")
        item_price.click()
        low_price = self.driver.find_element(By.ID, "s0-1-17-5[2]-@range-comp[]-@range-textbox[]-textbox")
        low_price.send_keys("50")
        high_price = self.driver.find_element(By.ID, "s0-1-17-5[2]-@range-comp[]-@range-textbox[]_1-textbox")
        high_price.send_keys("200")

        # Sort it by lowest price #ADVANCEDSETTINGS
        Lowest_price = self.driver.find_element(By.ID, "s0-1-17-8[9]-1[0]-_sop")
        Lowest_select = Select(Lowest_price)
        Lowest_price.click()
        Lowest_select.select_by_visible_text("Price + Shipping: lowest first")

        #Click the search #ADVANCEDSETTINGS
        Search = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn--primary")
        Search.click()


        time.sleep(3)

