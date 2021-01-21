from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class VagasPage(BasePage):
    """
    Coodesh Vagas Page class that hold elements
    and functionalities to Coodesh Vagas page only
    """

    tv_category = By.XPATH, '//*[@id="content"]/div[1]/div/form/div[1]/div[1]/span'
    et_search_vaga = By.XPATH, '//*[@id="content"]/div[1]/div/form/div[1]/div[2]/div/input'
    bt_find = By.XPATH, '//*[@id="content"]/div[1]/div/form/div[3]/button'
    tv_company = By.XPATH, '//*[@id="content"]/div[2]/div/div/div/div[2]/div[1]/div/ul/li[1]/a/span'
    lk_vaga = By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div/div[2]/div[1]/div/h1/a'
    lk_selected_vaga = By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div/div[2]/div[1]/div/h1/a'

    def __init__(self, driver):
        super().__init__(driver)

    def is_in_screen_vagas(self):
        self.assert_elem_text(self.tv_category, 'Categoria:')

    def visit_vagas(self):
        self.visit('https://beta.coodesh.com/vagas')

    def search_for_vaga(self, text):
        self.click(self.et_search_vaga)
        self.send_text(self.et_search_vaga, text)

    def click_on_find(self):
        self.click(self.bt_find)

    def has_vagas_grupo_mc_contigo(self, company):
        self.assert_elem_text(self.tv_company, company)

    def select_vaga(self, text):
        self.select_vaga_by_text(text)
