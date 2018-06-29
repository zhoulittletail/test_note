from selenium.webdriver.common.by import By
from base.base_action import Base_Action
class NetWorkPage(Base_Action):
    more_button = By.XPATH ,"//*[contains(@text,'更多')]"
    mobile_network_button = By.XPATH,"//*[contains(@text,'移动网络')]"
    first_choose_button = By.XPATH,"//*[contains(@text,'首选网络类型')]"
    network_2g_button = By.XPATH,"//*[contains(@text,'2G')]"
    network_3g_button = By.XPATH,"//*[contains(@text,'3G')]"

    # def __init__(self,driver):
    #     self.driver = driver

    def click_more(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.click(self.more_button)

    def click_move_network(self):
        self.click(self.mobile_network_button)


    def click_first_choose(self):
        self.click(self.first_choose_button)

    def click_2g(self):
        self.click(self.network_2g_button)

    def click_3g(self):
        self.click(self.network_3g_button)

