from python_training.project_pageobject.Pages.advanced_search import advanced_search
from python_training.project_pageobject.Pages.analyze_prices_xbox import results_xbox_ebay
from python_training.project_pageobject.Pages.welcome_page import welcome_page
from python_training.project_pageobject.Tests.ebay_seleniumbase import SeleniumBase

class results_xbox_ebay():
    base = SeleniumBase()
    url = "https://www.ebay.com"
    driver = base.selenium_start(url)
# Open the page and click the advanced settings page
    welcome_page_object = welcome_page(driver)
    welcome_page_object.search_for_item_xbox("XBOX SERIES X video game digital")
    welcome_page_object.click_advanced()
    advanced_page_object = advanced_search(driver)
# Run all the advanced settings filters
    advanced_page_object.advanced_filters()
    advanced_search(driver)
# Create a list of the first 3 item's prices and print out the cheapest one among them

    results_ebay_object = results_xbox_ebay(driver)
    results_ebay_object.analyze_prices_xbox()

    base.selenium_end(driver)
