import unittest
from selenium import webdriver
from Pages.HomePage import HomePage
from Pages.VagaPage import VagaPage
from Pages.VagasPage import VagasPage


class TestBase(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.driver.quit()


class Tests(TestBase):

    def setUp(self):
        super().setUp()
        self.home = HomePage(self.driver)
        self.vagas = VagasPage(self.driver)
        self.vaga = VagaPage(self.driver)

    def test_load_home_page(self):
        self.home.visit_home()
        self.home.has_vagas()

    def test_navigate_to_vagas(self):
        self.home.visit_home()
        self.home.click_on_vagas()
        self.vagas.is_in_screen_vagas()

    def test_search_vagas(self):
        self.vagas.visit_vagas()
        self.vagas.search_for_vaga("Grupo MContigo S.L")
        self.vagas.click_on_find()
        self.vagas.has_vagas_grupo_mc_contigo("Grupo MContigo S.L")

    def test_open_vaga(self):
        self.vagas.visit_vagas()
        self.vagas.search_for_vaga("Grupo MContigo S.L")
        self.vagas.click_on_find()
        self.vagas.select_vaga("Desenvolvedor(a) Fullstack Angular 8 Part-Time")
        self.vaga.is_in_screen_vaga("Desenvolvedor(a) Fullstack Angular 8 Part-Time")

    def test_enroll(self):
        self.vagas.visit_vagas()
        self.vagas.select_vaga("Desenvolvedor(a) Fullstack Angular 8 Part-Time")
        self.vaga.click_enroll()
        self.vaga.is_modal_opened()


if __name__ == '__main__':
    unittest.main()
