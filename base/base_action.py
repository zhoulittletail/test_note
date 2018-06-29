from selenium.webdriver.support.wait import WebDriverWait
class Base_Action():
    def __init__(self,driver):
        self.driver = driver

    def click(self,feature):
        self.find_element(feature).click()


    def input(self,feature,text):
        self.find_element(feature).send_keys(text)

    def find_element(self,feature):
        return self.driver.find_element(feature[0], feature[1])