from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from url_links import UrlLinks


class TestTransferFromPersonalAccount:

    def test_transfer_from_personal_account_to_constructor(self, driver, log_in_account):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_PERSONAL_ACCOUNT_FORM)))
        driver.find_element(*TestLocators.SEARCH_CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_CONSTRUCTOR_FORM)))
        assert driver.find_element(*TestLocators.SEARCH_CONSTRUCTOR_HEADER).text == 'Соберите бургер'

    def test_transfer_from_personal_account_to_logo(self, driver, log_in_account):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_PERSONAL_ACCOUNT_FORM)))
        driver.find_element(*TestLocators.SEARCH_LOGO).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_CONSTRUCTOR_FORM)))
        assert UrlLinks.site_main_page in driver.current_url