from selenium import webdriver
from datetime import datetime
import unittest
import HtmlTestRunner

#local
from pages import GooglePage
from pages import PixelluPage
from locators import locators

class pixelluTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/Projects/personal/pixelu/webdrivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.search = GooglePage.GooglePage(cls.driver)
        cls.pixellu = PixelluPage.PixelluPage(cls.driver)

    def test_1_success_Login_Test(self):
        self.driver.get("http://google.com")
        self.driver.save_screenshot('.//reports//screenshots//google_screenshot_' + str(datetime.today().strftime("%d%m%Y%H%M")) + '.png')
        self.search.GoogleSearch("Pixellu")
        self.driver.save_screenshot('./reports/screenshots/google_result_screenshot_' + str(datetime.today().strftime("%d%m%Y%H%M")) + '.png')
        self.search.GoogleClickFound("Pixellu - Software for Album Design")

        self.driver.find_element_by_xpath(locators.PixelluMainPageXPATH)
        self.driver.save_screenshot('./reports/screenshots/pixellu_screenshot_' + str(datetime.today().strftime("%d%m%Y%H%M")) + '.png')

        self.pixellu.SmartSlidesLogin()
        self.driver.find_element_by_name(locators.LoginPageUserNameName)
        self.driver.save_screenshot('./reports/screenshots/smartslide_login_screenshot_' + str(datetime.today().strftime("%d%m%Y%H%M")) + '.png')
        self.pixellu.pixelluLogin("pixellu.at.task+5@gmail.com", "cxJ7YP2J")

        self.assertEqual(True, self.driver.find_element_by_xpath(locators.LogoutMenuXPATH).is_enabled())
        self.driver.save_screenshot('./reports/screenshots/loggedin_screenshot_' + str(datetime.today().strftime("%d%m%Y%H%M")) + '.png')
        self.pixellu.pixelluLogout()

    def test_2_unsuccess_Login_Test(self):
        self.pixellu.pixelluLogin("pixellu.at.task+5@gmail.com", "cxJ7YP2")
        self.driver.save_screenshot('./reports/screenshots/incorrect_login_screenshot_' + str(datetime.today().strftime("%d%m%Y%H%M")) + '.png')
        self.assertEqual(True, self.driver.find_element_by_xpath(locators.IncorrectLoginXPATH).is_enabled())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../reports/"))