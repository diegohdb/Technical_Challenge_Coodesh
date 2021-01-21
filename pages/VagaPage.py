from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class VagaPage(BasePage):
    """
    Coodesh Specific Vaga Page class that hold elements
    and functionalities to a specific Vaga page only
    """

    tv_vaga_name = By.XPATH, '//*[@id="content"]/div[1]/div/div/div[2]/div/div[1]/h1'
    bt_enroll = By.XPATH, '//*[@id="content"]/div[1]/div/div/div[2]/div/div[2]/div/div/button'
    tv_modal = By.CSS_SELECTOR, 'body > div.fade.apply-modal.modal.show > div > div > div.bg-light.py-3.px-5.modal-header > div'

    def __init__(self, driver):
        super().__init__(driver)

    def is_in_screen_vaga(self, vaga_name):
        self.assert_elem_text(self.tv_vaga_name, vaga_name)

    def click_enroll(self):
        self.click(self.bt_enroll)

    def is_modal_opened(self):
        self.assert_elem_text(self.tv_modal, 'Candidatar-se')
