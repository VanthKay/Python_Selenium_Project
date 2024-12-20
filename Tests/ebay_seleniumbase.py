from selenium import webdriver


class SeleniumBase():
    def selenium_start(self, url):
        print("The test will begin now.")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.refresh()
        driver.get(url)
        driver.implicitly_wait(10)
        return driver
    def selenium_start_temp(self,url):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.refresh()
        driver.get(url)
        driver.implicitly_wait(10)
        return driver
    def selenium_end(self, driver):
        print("The Test has Ended Successfully!")
        driver.close()
    def selenium_end_temp(self, driver):
        driver.close()