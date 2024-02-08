import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from url_links import UrlLinks


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(UrlLinks.site_main_page)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def log_in_account(driver):
    driver.find_element(*TestLocators.SEARCH_LOGIN_IN_ACC_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))

    driver.find_element(*TestLocators.SEARCH_INPUT_LOGIN).send_keys("krivova5810@ya.ru")
    driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys("1234567")
    driver.find_element(*TestLocators.SEARCH_ENTER_BUTTON).click()
    return log_in_account