import time
from selenium.webdriver.common.by import By
class results_xbox_ebay():
    def __init__(self,driver):
        self.driver = driver
    def analyze_prices_xbox(self):
        price_elements = self.driver.find_elements(By.CSS_SELECTOR, '.s-item__price')[2:5]
        prices = []
        # Convert the string into a numeric value and clean it up
        for element in price_elements:
            price_text = element.text
            price_text = price_text.replace('ILS', '').strip()
            price_as_float = float(price_text)
            prices.append(price_as_float)
            assert price_as_float >= 50, "price found but less than 50 ILS"
        cheapest_price = min(prices)
        cheapest_index = prices.index(cheapest_price)
        with open("cheapest_price_xbox.txt", "w") as f:
            f.write(str(cheapest_price))

        print(f"Prices: {prices}")
        print(
            f"The cheapest price is: {cheapest_price} Shekels (Item {cheapest_index + 3})")  # Add 3 to account for skipped results

        time.sleep(3)









    # def advanced_search_xbox(self):
    #     # Selecting the Video game category #ADVANCEDSETTINGS
    #     Category_xbox = self.driver.find_element(By.ID, "s0-1-17-4[0]-7[3]-_sacat")
    #     select_category = Select(Category_xbox)
    #     select_category.select_by_index(33)
    #
    #     # Looking for only "Buy it now" Items #ADVANCEDSETTINGS
    #     Buy_now = self.driver.find_element(By.ID, "s0-1-17-6[3]-[2]-LH_BIN")
    #     Buy_now.click()
    #
    #     # Making sure the items shown are New #ADVANCEDSETTINGS
    #     New = self.driver.find_element(By.ID, "s0-1-17-6[4]-[0]-LH_ItemCondition")
    #     New.click()
    #
    #     # Includes free shipping #ADVANCEDSETTINGS
    #     Free_shipping = self.driver.find_element(By.ID, "s0-1-17-5[6]-[0]-LH_FS")
    #     Free_shipping.click()
    #
    #     # Limiting the cost #ADVANCEDSETTINGS
    #     item_price = self.driver.find_element(By.ID, "s0-1-17-5[2]-[0]-")
    #     item_price.click()
    #     low_price = self.driver.find_element(By.ID, "s0-1-17-5[2]-@range-comp[]-@range-textbox[]-textbox")
    #     low_price.send_keys("50")
    #     high_price = self.driver.find_element(By.ID, "s0-1-17-5[2]-@range-comp[]-@range-textbox[]_1-textbox")
    #     high_price.send_keys("200")
    #
    #     # Sort it by lowest price #ADVANCEDSETTINGS
    #     Lowest_price = self.driver.find_element(By.ID, "s0-1-17-8[9]-1[0]-_sop")
    #     Lowest_select = Select(Lowest_price)
    #     Lowest_price.click()
    #     Lowest_select.select_by_visible_text("Price + Shipping: lowest first")
    #
    #     # Click the search #ADVANCEDSETTINGS
    #     Search = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn--primary")
    #     Search.click()