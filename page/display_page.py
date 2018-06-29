from selenium.webdriver.common.by import By
from base.base_action import Base_Action

class DisPlayPage(Base_Action):
    display_button = By.XPATH,"//*[contains(@text,'显示')]"
    serch_button = By.ID,"com.android.settings:id/search"
    input_button = By.ID,"android:id/search_src_text"
    back_button = By.CLASS_NAME,"android.widget.ImageButton"


    # def __init__(self,driver):
    #     self.driver = driver

    def click_display(self):
        self.click(self.display_button)

    def click_serch(self):
        # self.find_element(self.serch_button).click()
        self.click(self.serch_button)
    def input_keyword(self,text):
        # self.find_element(self.input_button).send_keys("hello")
        self.input(self.input_button,text)
    def click_back(self):
        # self.find_element(self.back_button).click()
        self.click(self.back_button)
