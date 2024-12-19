from python_training.project_pageobject.Pages.advanced_search import advanced_search
from python_training.project_pageobject.Pages.welcome_page import welcome_page
from python_training.project_pageobject.Tests.ebay_seleniumbase import SeleniumBase


class advanced_search_ebay_ps5:
    base = SeleniumBase()
    driver = base.selenium_start("https://ebay.com")

    welcome_page_object = welcome_page(driver)
    welcome_page_object.search_for_item("PS5 video game digital")
    advanced_page_object = advanced_search(driver)
    advanced_page_object.advanced_filters()

    base.selenium_end(driver)