from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class HomePage(BasePage):
    """
    Coodesh Home Page class that hold elements
    and functionalities to Coodesh Home page only
    """

    lk_vagas = By.CSS_SELECTOR, 'div[id="navBar"] a[href="/vagas"]'

    def __init__(self, driver):
        super().__init__(driver)

    def visit_home(self):
        self.visit('https://beta.coodesh.com/')

    def has_vagas(self):
        self.assert_elem_text(self.lk_vagas , 'Vagas')

    def click_on_vagas(self):
        self.click(self.lk_vagas)
