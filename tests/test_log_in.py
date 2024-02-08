from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from url_links import UrlLinks


class TestLogIn:

    def test_login_in_main_page(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((TestLocators.SEARCH_LOGIN_IN_ACC_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_LOGIN_IN_ACC_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))

        driver.find_element(*TestLocators.SEARCH_INPUT_LOGIN).send_keys("krivova5808@ya.ru")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys("1234567")
        driver.find_element(*TestLocators.SEARCH_ENTER_BUTTON).click()
        assert UrlLinks.site_main_page in driver.current_url

    def test_login_in_personal_account(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))
        driver.find_element(*TestLocators.SEARCH_INPUT_LOGIN).send_keys("krivova5808@ya.ru")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys("1234567")
        driver.find_element(*TestLocators.SEARCH_ENTER_BUTTON).click()
        assert UrlLinks.site_main_page in driver.current_url

    def test_login_in_recover_password(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))
        driver.find_element(*TestLocators.SEARCH_RECOVER_PASSWORD_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))
        driver.find_element(*TestLocators.SEARCH_ENTER_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))
        driver.find_element(*TestLocators.SEARCH_INPUT_LOGIN).send_keys("krivova5808@ya.ru")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys("1234567")
        driver.find_element(*TestLocators.SEARCH_ENTER_BUTTON).click()
        assert UrlLinks.site_main_page in driver.current_url

    def test_login_in_registration_page(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))
        driver.find_element(*TestLocators.SEARCH_REGISTRATION_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))
        driver.find_element(*TestLocators.SEARCH_ENTER_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))
        driver.find_element(*TestLocators.SEARCH_INPUT_LOGIN).send_keys("krivova5808@ya.ru")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys("1234567")
        driver.find_element(*TestLocators.SEARCH_ENTER_BUTTON).click()
        assert UrlLinks.site_main_page in driver.current_url
