'''from selenium import webdriver
from tests.user_registration_tests import FormPage
import time

def before_all(context):
    context.driver = webdriver.Chrome()
    context.form_page = FormPage(context.driver)

def after_all(context):
    context.driver.quit()
'''