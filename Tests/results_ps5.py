from python_training.project_pageobject.Pages.advanced_search import advanced_search
from python_training.project_pageobject.Pages.analyze_prices_ps5 import results_ps5_ebay
from python_training.project_pageobject.Pages.welcome_page import welcome_page
from python_training.project_pageobject.Tests.ebay_seleniumbase import SeleniumBase

# This test grabs the first 3 prices on the results website and gives the lowest of them to the comparison
class results_ps5():
    base = SeleniumBase()
    url = "https://www.ebay.com"
    driver = base.selenium_start_temp(url)
    # Open the page and click the advanced settings page
    welcome_page_object = welcome_page(driver)
    welcome_page_object.search_for_item("PS5 video game digital")
    welcome_page_object.click_advanced()
    # Run all the advanced settings filters
    advanced_page_object = advanced_search(driver)
    advanced_page_object.advanced_filters()
    advanced_search(driver)
    # Create a list of the first 3 item's prices and print out the cheapest one among them
    results_ebay_object = results_ps5_ebay(driver)
    results_ebay_object.analyze_prices_ps5()

