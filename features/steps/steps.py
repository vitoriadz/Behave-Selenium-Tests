from behave import given, when, then
from selenium import webdriver
from tests.user_registration_tests import FormPage
import time

@given("that the user is on the form page")
def step_given_user_on_form_page(context):
    context.driver = webdriver.Chrome()
    context.form_page = FormPage(context.driver)
    context.form_page.open()

@when('the user fills in the form with valid data')
def step_when_user_fills_form_with_valid_data(context):
    context.form_page.fill_full_form("Maria", "Vitoria", "mariavitoriadz@gmail.com", "9998363845", "NCR")
    time.sleep(5)

@then('the form is displayed a success message in the terminal')
def step_then_form_submitted_successfully(context):
    confirmation_message = context.form_page.get_confirmation_message()
    assert confirmation_message is not None
    print("O formulário foi enviado com sucesso!")

@when('the user fills in the form with the name blank')
def step_when_user_fills_form_with_blank_name(context):
    context.form_page.fill_full_form("", "Vitoria", "mariavitoriadz@gmail.com", "9998363845", "NCR")
    time.sleep(5)

@then('the form submission fails due to blank name')
def step_then_form_submission_fails_due_to_blank_name(context):
    confirmation_message = context.form_page.get_confirmation_message()
    assert confirmation_message is None
    print("O envio do formulário não pôde ser efetuado, o campo obrigatório 'nome' está em branco!")

@when('the user fills out the form with the last name blank')
def step_when_user_fills_form_with_blank_lastname(context):
    context.form_page.fill_full_form("Maria", "", "mariavitoriadz@gmail.com", "9998363845", "NCR")
    time.sleep(5)

@then('the form submission fails due to blank last name')
def step_then_form_submission_fails_due_to_blank_lastname(context):
    confirmation_message = context.form_page.get_confirmation_message()
    assert confirmation_message is None
    print("O envio do formulário não pôde ser efetuado, o campo obrigatório 'sobrenome' está em branco!")

@when('the user fills out the form with an invalid email')
def step_when_user_fills_form_with_invalid_email(context):
    context.form_page.fill_full_form("Maria", "Vitoria", "mariavitoriadz", "9998363845", "NCR")
    time.sleep(5)

@then('the form submission fails due to invalid email')
def step_then_form_submission_fails_due_to_invalid_email(context):
    confirmation_message = context.form_page.get_confirmation_message()
    assert confirmation_message is None
    print("O envio do formulário não pôde ser efetuado, o campo 'email' não está no formato adequado!")

@when('the user fills in the form with an invalid number')
def step_when_user_fills_form_with_invalid_number(context):
    context.form_page.fill_full_form("Maria", "Vitoria", "mariavitoriadz", "98363845", "NCR")
    time.sleep(5)

@then('the form submission fails due to invalid number')
def step_then_form_submission_fails_due_to_invalid_number(context):
    confirmation_message = context.form_page.get_confirmation_message()
    assert confirmation_message is None
    print("O envio do formulário não pôde ser efetuado, o campo 'número' não está no formato adequado!")