from selenium import webdriver

#local
from locators import locators

class PixelluPage():

    def __init__(self, driver):
        self.driver = driver

    def SmartSlidesLogin(self):
        action = webdriver.ActionChains(self.driver)

        firstLevelMenu = self.driver.find_element_by_xpath(locators.LoginButtonXPATH)
        action.move_to_element(firstLevelMenu).perform()
        self.driver.find_element_by_xpath(locators.SmartSlidesLoginMenuItemXPATH).click()

    def pixelluLogin(self, login, passw):
        self.driver.find_element_by_name(locators.LoginPageUserNameName).send_keys(login)
        self.driver.find_element_by_name(locators.LoginPageUserPasswordName).send_keys(passw)
        self.driver.find_element_by_xpath(locators.LoginPageUserLoginBtnXPATH).click()

    def pixelluLogout(self):
        action = webdriver.ActionChains(self.driver)

        firstLevelMenu = self.driver.find_element_by_xpath(locators.UserProfileIconXPATH)
        action.move_to_element(firstLevelMenu).perform()
        self.driver.find_element_by_xpath(locators.LogoutMenuXPATH).click()