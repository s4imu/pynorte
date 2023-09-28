import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Fixture para iniciar o navegador antes dos testes
@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Substitua pelo driver do seu navegador
    yield driver
    driver.quit()  # Fecha o navegador após o teste

def test_addToCart(browser):
    browser.get("https://www.saucedemo.com/")
    assert "Swag Labs" in browser.title # verificar se acessou o site corretamente
   
    usernameInput = browser.find_element(By.NAME, "user-name")  # Use o método By.NAME
    passwordInput = browser.find_element(By.XPATH, '//*[@id="password"]') # Use o método By.Xpath
    loginButton = browser.find_element(By.ID, 'login-button')
    usernameInput.send_keys("standard_user")
    passwordInput.send_keys("secret_sauce") 
    loginButton.click()
    
    backpack = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    backpack.click()
    productPageTitle = browser.find_element(By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')

    assert "Sauce Labs Backpack" in productPageTitle.text