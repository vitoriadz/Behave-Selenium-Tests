from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import unittest

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class FormPage(BasePage):
    URL = "https://demoqa.com/automation-practice-form"

    def open(self):
        self.driver.get(self.URL)

    def fill_full_form(self, first_name, last_name, email, number, location):
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)
        self.driver.find_element(By.ID, "userEmail").send_keys(email)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.ID, 'gender-radio-2'))
        self.driver.find_element(By.ID, "userNumber").send_keys(number, Keys.TAB)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.ID, 'hobbies-checkbox-2'))
        self.driver.find_element(By.ID, "react-select-3-input").send_keys(location, Keys.TAB)
        self.driver.find_element(By.ID, "react-select-4-input").send_keys("Noida", Keys.TAB)
        self.driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.ENTER)

    def get_confirmation_message(self):
        try:
            return self.driver.find_element(By.ID, "example-modal-sizes-title-lg").text
        except NoSuchElementException:
            return None

class TestFormPractice(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.form_page = FormPage(self.driver)

    def test_full_form_submission(self):
        self.form_page.open()
        self.form_page.fill_full_form("Maria", "Vitoria", "mariavitoriadz@gmail.com", "9998363845", "NCR")
        sleep(5)
        confirmation_message = self.form_page.get_confirmation_message()
        self.assertIsNotNone(confirmation_message)
        print("O formulário foi enviado com sucesso!")

    def test_blank_name_field(self):
        self.form_page.open()
        self.form_page.fill_full_form("", "Vitoria", "mariavitoriadz@gmail.com", "9998363845", "NCR")
        sleep(5)
        confirmation_message = self.form_page.get_confirmation_message()
        self.assertIsNone(confirmation_message)
        print("O envio do formulário não pôde ser efetuado, o campo obrigatório 'nome' está em branco!")

    def test_blank_lastname_field(self):
        self.form_page.open()
        self.form_page.fill_full_form("Maria", "", "mariavitoriadz@gmail.com", "9998363845", "NCR")
        sleep(5)
        confirmation_message = self.form_page.get_confirmation_message()
        self.assertIsNone(confirmation_message)
        print("O envio do formulário não pôde ser efetuado, o campo obrigatório 'sobrenome' está em branco!")

    def test_invalid_email_field(self):
        self.form_page.open()
        self.form_page.fill_full_form("Maria", "Vitoria", "mariavitoriadz", "9998363845", "NCR")
        sleep(5)
        confirmation_message = self.form_page.get_confirmation_message()
        self.assertIsNone(confirmation_message)
        print("O envio do formulário não pôde ser efetuado, o campo 'email' não está no formato adequado!")

    def test_invalid_number_field(self):
        self.form_page.open()
        self.form_page.fill_full_form("Maria", "Vitoria", "mariavitoriadz@gmail.com", "98363845", "NCR")
        sleep(5)
        confirmation_message = self.form_page.get_confirmation_message()
        self.assertIsNone(confirmation_message)
        print("O envio do formulário não pôde ser efetuado, o campo 'número' não está no formato adequado!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()