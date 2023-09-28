import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def login(browser):
    browser.get("https://www.saucedemo.com/")
   
    usernameInput = browser.find_element(By.NAME, "user-name")  # Use o método By.NAME
    passwordInput = browser.find_element(By.XPATH, '//*[@id="password"]') # Use o método By.Xpath
    loginButton = browser.find_element(By.ID, 'login-button')
    usernameInput.send_keys("standard_user")
    passwordInput.send_keys("secret_sauce") 
    loginButton.click()

def add_product_cart(browser):
    backpack = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    backpack.click()

    addToCartButton = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    cartButton = browser.find_element(By.CLASS_NAME, "shopping_cart_link")

    addToCartButton.click()
    cartButton.click()


# Fixture para iniciar o navegador antes dos testes
@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Substitua pelo driver do seu navegador
    yield driver
    driver.quit()  # Fecha o navegador após o teste

# Teste de Login
def test_login(browser):
    login(browser)

    productsPageTitle = browser.find_element(By.CLASS_NAME, "title")

    assert "Products" in productsPageTitle.text

def test_addToCart(browser):
    product = "Sauce Labs Backpack"
    login(browser)
    add_product_cart(browser)

    titleProductInCart = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')

    assert product in titleProductInCart.text

def test_checkout(browser):

    name = "Symon"
    surname = "Barreto"
    zip_code = "69099-100"

    login(browser)
    add_product_cart(browser)

    checkout_button = browser.find_element(By.ID, 'checkout')
    checkout_button.click()

    information_title_page = browser.find_element(By.CLASS_NAME, "title")

    assert "Checkout: Your Information" in information_title_page.text

    first_name_input = browser.find_element(By.ID, 'first-name')
    last_name_input = browser.find_element(By.ID, 'last-name')
    zip_code_input = browser.find_element(By.ID, 'postal-code')

    first_name_input.send_keys(name)
    last_name_input.send_keys(surname)
    zip_code_input.send_keys(zip_code)

    continue_button = browser.find_element(By.ID, "continue")

    continue_button.click()

    overview_title_page = browser.find_element(By.CLASS_NAME, "title")

    assert "Checkout: Overview" in overview_title_page.text

    finish_button = browser.find_element(By.ID, "finish")

    finish_button.click()

    finish_title_page = browser.find_element(By.CLASS_NAME, "title")

    assert "Checkout: Complete!" in finish_title_page.text

    ending_message = browser.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2')

    assert "Thank you for your order!" in ending_message.text