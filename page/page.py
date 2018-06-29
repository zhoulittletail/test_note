from page.display_page import DisPlayPage
from page.network_page import NetWorkPage
class Page():
    def __init__(self,driver):
        self.driver = driver
    @property  #  可以把一个函数当作属性来使用（调用的时候直接.就可以不需要加括号）
    def display(self):
        return DisPlayPage(self.driver)

    @property
    def network(self):
        return NetWorkPage(self.driver)