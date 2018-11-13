
#local
from locators import locators

class GooglePage():

    def __init__(self, driver):
        self.driver = driver

    def GoogleSearch(self, searchText):
        self.driver.find_element_by_xpath(locators.GoogleSearchInputXPATH).send_keys(searchText)
        self.driver.find_element_by_xpath(locators.GoogleSearchBtnXPATH).submit()

    def GoogleClickFound(self, resultText):
        self.driver.find_element_by_partial_link_text(resultText).click()