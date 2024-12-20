from python_training.project_pageobject.Pages.advanced_search import advanced_search
from python_training.project_pageobject.Pages.welcome_page import welcome_page
from python_training.project_pageobject.Tests.ebay_seleniumbase import SeleniumBase

# This test types the item wanted and applies the advanced settings
base = SeleniumBase()
url = "https://www.ebay.com"
driver = base.selenium_start_temp(url)
# Open the page and click the advanced settings page
welcome_page_object = welcome_page(driver)
welcome_page_object.search_for_item_xbox("XBOX SERIES X video game digital")
welcome_page_object.click_advanced()
advanced_page_object = advanced_search(driver)
# Run all the advanced settings filters
advanced_page_object.advanced_filters()
advanced_search(driver)

base.selenium_end(driver)










    # base = SeleniumBase()
    # driver = base.selenium_start("https://ebay.com")
    # # TEST 2 - LOOKING FOR XBOX VIDEO GAMES (HOMEPAGE/ADVANCEDSETTINGS/RESULTS
    # # Writing video game in the search #HOMEPAGE
    # xbox_videogame = driver.find_element(By.ID, "gh-ac")
    # xbox_videogame.click()
    # time.sleep(3)
    # # Type "XBOX SERIES X video game digital" in the search, and press ENTER #HOMEPAGE
    # xbox_videogame.send_keys("XBOX SERIES X video game digital")
    # xbox_videogame.send_keys(Keys.RETURN)
    # # Clicking the advanced search #HOMEPAGE
    # Advanced = driver.find_element(By.ID, "gh-as-a")
    # Advanced.click()
    # time.sleep(3)
    #
    # # Selecting the Video game category #ADVANCEDSETTINGS
    # Category = driver.find_element(By.ID, "s0-1-17-4[0]-7[3]-_sacat")
    # select_category = Select(Category)
    # select_category.select_by_index(33)
    #
    # # Looking for only "Buy it now" Items #ADVANCEDSETTINGS
    # Buy_now = driver.find_element(By.ID, "s0-1-17-6[3]-[2]-LH_BIN")
    # Buy_now.click()
    #
    # # Making sure the items shown are New #ADVANCEDSETTINGS
    # New = driver.find_element(By.ID, "s0-1-17-6[4]-[0]-LH_ItemCondition")
    # New.click()
    #
    # # Includes free shipping #ADVANCEDSETTINGS
    # Free_shipping = driver.find_element(By.ID, "s0-1-17-5[6]-[0]-LH_FS")
    # Free_shipping.click()
    #
    # # Limiting the cost #ADVANCEDSETTINGS
    # item_price = driver.find_element(By.ID, "s0-1-17-5[2]-[0]-")
    # item_price.click()
    # low_price = driver.find_element(By.ID, "s0-1-17-5[2]-@range-comp[]-@range-textbox[]-textbox")
    # low_price.send_keys("50")
    # high_price = driver.find_element(By.ID, "s0-1-17-5[2]-@range-comp[]-@range-textbox[]_1-textbox")
    # high_price.send_keys("200")
    #
    # # Sort it by lowest price #ADVANCEDSETTINGS
    # Lowest_price = driver.find_element(By.ID, "s0-1-17-8[9]-1[0]-_sop")
    # Lowest_select = Select(Lowest_price)
    # Lowest_price.click()
    # Lowest_select.select_by_visible_text("Price + Shipping: lowest first")
    #
    # #Click the search #ADVANCEDSETTINGS
    # Search = driver.find_element(By.CSS_SELECTOR, "button.btn.btn--primary")
    # Search.click()
    #
    #
    # time.sleep(3)
    #
    #
    # base.selenium_end(driver)