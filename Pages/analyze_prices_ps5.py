from time import sleep

from selenium.webdriver.common.by import By


class results_ps5_ebay:
    def __init__(self, driver):
        self.driver = driver


    def analyze_prices_ps5(self):
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
        with open("cheapest_price_ps5.txt", "w") as f:
            f.write(str(cheapest_price))
        print(f"Prices: {prices}")
        print(
            f"The cheapest price is: {cheapest_price} Shekels (Item {cheapest_index + 3})")  # Add 3 to account for skipped results

        sleep(3)