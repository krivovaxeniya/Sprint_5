import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def log_in_account(driver):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

    driver.find_element(By.NAME, "name").send_keys("krivova5810@ya.ru")
    driver.find_element(By.NAME, "Пароль").send_keys("1234567")
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    return log_in_account