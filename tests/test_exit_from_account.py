from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from url_links import UrlLinks


class TestExitFromAccount:

    def test_exit_from_personal_account(self, driver, log_in_account):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((TestLocators.SEARCH_EXIT_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))
        assert driver.current_url == UrlLinks.authorization_page